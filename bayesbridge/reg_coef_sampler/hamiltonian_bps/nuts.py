import math

import numpy as np

from .dynamics import draw_velocity, draw_inertia
from .hbps_dynamics import HBPSDynamics
from ..hamiltonian_monte_carlo.util import warn_message_only


class HBPSNoUTurnSampler:

    def __init__(self, f, warning_requested=True):
        """
        Parameters
        ----------
        f: callable
            Return the log probability and gradient evaluated at q.
        mass: None, numpy 1d array, or callable
        """
        self.f = f
        self.dynamics = HBPSDynamics()
        self.warning_requested = warning_requested

    def generate_next_state(self, dt, q, logp=None, grad=None, p=None, inertia=None,
                            max_tree_height=10, hamiltonian_error_tol=100, unit_v=False):
        if logp is None or grad is None:
            logp, _ = self.f(q, loglik_only=True)

        if p is None:
            p = draw_velocity(len(q), unit_v)
        if inertia is None:
            inertia = draw_inertia()

        bouncef = self.dynamics.next_bounce_time(self.f, None, q, p, inertia, -logp)
        bounceb = self.dynamics.next_bounce_time(self.f, bouncef, q, -p, inertia, -logp)
        grad = (bouncef, 0, bounceb, 0)
        logp_joint = self.dynamics.compute_hamiltonian(logp, p, inertia)
        logp_joint_threshold = logp_joint - np.random.exponential()
        # Slicing variable in the log-scale.

        tree = _TrajectoryTree(
            self.dynamics, self.f, dt, q, p, inertia, logp, grad, logp_joint, logp_joint,
            logp_joint_threshold, hamiltonian_error_tol
        )
        directions = 2 * (np.random.rand(max_tree_height) < 0.5) - 1
        # Pre-allocation of random directions is unnecessary, but makes the code easier to test.
        tree, final_height, last_doubling_rejected, maxed_before_u_turn \
            = self._grow_trajectory_till_u_turn(tree, directions)
        q, p, inertia, logp, grad = tree.sample

        if self.warning_requested:
            self._issue_warnings(
                tree.instability_detected, maxed_before_u_turn, max_tree_height
            )

        info = {
            'logp': logp,
            'grad': grad,
            'ave_accept_prob': tree.ave_accept_prob,
            'ave_hamiltonian_error': tree.ave_hamiltonian_error,
            'num_bounces': tree.n_bounces + 2,
            'tree_height': final_height,
            'u_turn_detected': tree.u_turn_detected,
            'instability_detected': tree.instability_detected,
            'last_doubling_rejected': last_doubling_rejected
        }
        return q, info

    def _issue_warnings(
            self, instability_detected, maxed_before_u_turn, max_height):

        if instability_detected:
            warn_message_only(
                "Numerical integration became unstable while simulating a "
                "NUTS trajectory."
            )
        if maxed_before_u_turn:
            warn_message_only(
                'The trajectory tree reached the max height of {:d} before '
                'meeting the U-turn condition.'.format(max_height)
            )
        return

    @staticmethod
    def _grow_trajectory_till_u_turn(tree, directions):

        height = 0  # Referred to as 'depth' in the original paper, but arguably the
        # trajectory tree is built 'upward' on top of the existing ones.
        max_height = len(directions)
        trajectory_terminated = False
        while not trajectory_terminated:
            doubling_rejected \
                = tree.double_trajectory(height, directions[height])
            # No transition to the next half of trajectory takes place if the
            # termination criteria are met within the next half tree.

            height += 1
            trajectory_terminated \
                = tree.u_turn_detected or tree.instability_detected or (height >= max_height)
            maxed_before_u_turn \
                = height >= max_height and (not tree.u_turn_detected)

        return tree, height, doubling_rejected, maxed_before_u_turn


class _TrajectoryTree():
    """
    Collection of (a subset of) states along the simulated Hamiltonian dynamics
    trajcetory endowed with a binary tree structure.
    """

    def __init__(
            self, dynamics, f, dt, q, p, inertia, logp, grad, joint_logp,
            init_joint_logp, joint_logp_threshold, hamiltonian_error_tol=100.,
            u_turn_criterion='momentum'):

        self.dynamics = dynamics
        self.f = f
        self.dt = dt
        self.joint_logp_threshold = joint_logp_threshold
        self.front_state = (q, p, inertia, grad)
        self.rear_state = (q, p, inertia, grad)
        self.sample = (q, p, inertia, logp, grad)
        self.u_turn_detected = False
        self.min_hamiltonian = -joint_logp
        self.max_hamiltonian = -joint_logp
        self.hamiltonian_error_tol = hamiltonian_error_tol
        self.n_acceptable_state = int(joint_logp > joint_logp_threshold)
        self.n_integration_step = 0
        self.n_bounces = 0
        self.init_joint_logp = init_joint_logp
        self.height = 0
        self.ave_hamiltonian_error = abs(init_joint_logp - joint_logp)
        self.ave_accept_prob = min(1, math.exp(joint_logp - init_joint_logp))
        self.velocity_based_u_turn = (u_turn_criterion == 'velocity')

    @property
    def n_node(self):
        return 2 ** self.height

    @property
    def instability_detected(self):
        fluctuation_along_trajectory = self.max_hamiltonian - self.min_hamiltonian
        return fluctuation_along_trajectory > self.hamiltonian_error_tol

    def double_trajectory(self, height, direction):
        next_tree = self._build_next_tree(
            *self._get_states(direction), height, direction
        )
        no_transition_to_next_tree_attempted \
            = self._merge_next_tree(next_tree, direction, sampling_method='swap')
        return no_transition_to_next_tree_attempted

    def _build_next_tree(self, q, p, inertia, bounces, height, direction):

        if height == 0:
            return self._build_next_singleton_tree(q, p, inertia, bounces, direction)

        subtree = self._build_next_tree(q, p, inertia, bounces, height - 1, direction)
        trajectory_terminated_within_subtree \
            = subtree.u_turn_detected or subtree.instability_detected
        if not trajectory_terminated_within_subtree:
            next_subtree = self._build_next_tree(
                *subtree._get_states(direction), height - 1, direction
            )
            subtree._merge_next_tree(next_subtree, direction, sampling_method='uniform')

        return subtree

    def _build_next_singleton_tree(self, q, p, inertia, bounces, direction):
        q, p, logp, bounces, inertia, num_bounces, = \
            self.dynamics.advance(self.f, self.dt, q, p, inertia, bounces, direction=direction)
        self.n_bounces += num_bounces
        if math.isinf(logp):
            joint_logp = - float('inf')
        else:
            joint_logp = self.dynamics.compute_hamiltonian(logp, p, inertia)
        return self._clone_tree(q, p, inertia, logp, bounces, joint_logp)

    def _clone_tree(self, q, p, inertia, logp, grad, joint_logp):
        """ Construct a tree with shared dynamics and acceptance criteria. """
        return _TrajectoryTree(
            self.dynamics, self.f, self.dt, q, p, inertia, logp, grad, joint_logp, self.init_joint_logp,
            self.joint_logp_threshold, self.hamiltonian_error_tol
        )

    def _merge_next_tree(self, next_tree, direction, sampling_method):

        # Trajectory termination flags from the next tree must be propagated up
        # the call stack, but other states of the tree is updated only if the
        # next tree is accessible from the current tree (i.e. the trajectory
        # did not get terminated within the next tree).

        self.u_turn_detected = self.u_turn_detected or next_tree.u_turn_detected
        self.min_hamiltonian = min(self.min_hamiltonian, next_tree.min_hamiltonian)
        self.max_hamiltonian = max(self.max_hamiltonian, next_tree.max_hamiltonian)
        trajectory_terminated_within_next_tree \
            = next_tree.u_turn_detected or next_tree.instability_detected

        if not trajectory_terminated_within_next_tree:
            self._update_sample(next_tree, sampling_method)
            self.n_acceptable_state += next_tree.n_acceptable_state
            self._set_states(*next_tree._get_states(direction), direction)
            self.u_turn_detected \
                = self.u_turn_detected or self._check_u_turn_at_front_and_rear_ends()
            weight = self.n_node / (self.n_node + next_tree.n_node)
            self.ave_hamiltonian_error \
                = weight * self.ave_hamiltonian_error + (
                    1 - weight) * next_tree.ave_hamiltonian_error
            self.ave_accept_prob \
                = weight * self.ave_accept_prob + (1 - weight) * next_tree.ave_accept_prob
            self.height += 1

        return trajectory_terminated_within_next_tree

    def _update_sample(self, next_tree, method):
        """
        Parameters
        ----------
        method: {'uniform', 'swap'}
        """
        if method == 'uniform':
            n_total = self.n_acceptable_state + next_tree.n_acceptable_state
            sampling_weight_on_next_tree \
                = next_tree.n_acceptable_state / max(1, n_total)
        elif method == 'swap':
            sampling_weight_on_next_tree \
                = next_tree.n_acceptable_state / self.n_acceptable_state
        if np.random.uniform() < sampling_weight_on_next_tree:
            self.sample = next_tree.sample

    def _check_u_turn_at_front_and_rear_ends(self):
        q_front, p_front, _, _ = self._get_states(1)
        q_rear, p_rear, _, _ = self._get_states(-1)
        dq = q_front - q_rear
        if self.velocity_based_u_turn:
            v_front = self.dynamics.convert_to_velocity(p_front)
            v_rear = self.dynamics.convert_to_velocity(p_rear)
            u_turned = (np.dot(dq, v_front) < 0) or (np.dot(dq, v_rear) < 0)
        else:
            u_turned = (np.dot(dq, p_front) < 0) or (np.dot(dq, p_rear) < 0)
        return u_turned

    def _set_states(self, q, p, inertia, grad, direction):
        if direction > 0:
            self.front_state = (q, p, inertia, grad)
        else:
            self.rear_state = (q, p, inertia, grad)

    def _get_states(self, direction):
        if direction > 0:
            return self.front_state
        else:
            return self.rear_state
