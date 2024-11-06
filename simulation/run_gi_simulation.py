import pickle
import socket
import sys

from bayesbridge import BayesBridge, RegressionModel, RegressionCoefPrior

with open("/users/achin/bayes-bridge/simulation/compute-124_cholesky_gi_4000_seed1_thin1_params1_initFalse.p", "rb") as f:
    initial = pickle.load(f)[0]['coef'][:, -1]

with open("/users/achin/bayes-bridge/simulation/gi_bleed_Xy.p", "rb") as f:
    X, y = pickle.load(f)

model = RegressionModel(
    y, X, family='logit',
    add_intercept=True, center_predictor=True,
)

prior = RegressionCoefPrior(
    bridge_exponent=.5,
    n_fixed_effect=0,
    # Number of coefficients with Gaussian priors of pre-specified sd.
    sd_for_intercept=float('inf'),
    # Set it to float('inf') for a flat prior.
    sd_for_fixed_effect=1.,
    regularizing_slab_size=2.,
    # Weakly constrain the magnitude of coefficients under bridge prior.
)

bridge = BayesBridge(model, prior)

params_dict = {1: ('coef', 'global_scale', 'logp'),
               2: ('coef', 'global_scale', 'logp', 'local_scale'),
               3: 'all'}

sampler = sys.argv[1]
n = int(sys.argv[2])
seed = int(sys.argv[3])
thin = int(sys.argv[4])
params_int = int(sys.argv[5])
params_to_save = params_dict[params_int]
init_int = int(sys.argv[6])
initial = {'global_scale': .01, 'coef': initial} if init_int else {'global_scale': .01}

try:
    dt = float(sys.argv[7])
except IndexError:
    dt = 1
try:
    unit_v = bool(int(sys.argv[8]))
except IndexError:
    unit_v = False
try:
    rr = float(sys.argv[9])
except IndexError:
    rr = 1.

hostname = socket.gethostname().split(".")[0]

mcmc_output = bridge.gibbs(
    n_iter=n, n_burnin=0, thin=thin,
    init=initial,
    params_to_save=params_to_save,
    coef_sampler_type=sampler,
    seed=seed, dt=dt, rr=rr, unit_v=unit_v)

filename = f"/users/achin/hbps/gi_bleed_sim2/{hostname}_{sampler}_gi_{n}_seed{seed}_thin{thin}_params{params_int}_init{bool(init_int)}"

if sampler == "bps":
    filename += f"_dt{str(dt).replace('.', '-')}_unit_v-{unit_v}_rr{str(rr).replace('.', '-')}.p"
elif sampler == "hbpsnuts" or sampler == "hbps":
    filename += f"_dt{str(dt).replace('.', '-')}_unit_v-{unit_v}.p"
else:
    filename += ".p"

with open(filename, "wb") as f:
    pickle.dump(mcmc_output, f)
