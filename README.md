# Code for Section 5.2 of "MCMC using bouncy Hamiltonian dynamics: A unifying framework for Hamiltonian Monte Carlo and piecewise deterministic Markov process samplers" by Chin and Nishimura 2024

## Setting up BayesBridge
This code is a fork of the [BayesBridge](https://github.com/OHDSI/bayes-bridge) software, modified with the Hamiltonian Bouncy Particle Sampler of Chin et al. 

1. Clone the repo: `git clone git@github.com:chinandrew/gi_bleed_hbps.git`
2. Enter the cloned directory and install `bayesbridge`: `cd gi_bleed_hbps; pip install .`


## Running BayesBridge
### Set data and initial position
1. Place data as a pickled (matrix, vector) tuple of (design matrix, response) in `simulation/gi_bleed_Xy.p`.
	- The data used in the paper are extracted from the proprietary HIPAA-compliant Merative MarketScan Research Databases. Our data extraction tool and cohort definitions are openly available online at https://github.com/aki-nishimura/anticoagulant-study-cohorts; they can be used to extract the same data sets by any researchers who have purchased a license to the Merative databases.
2. If desired, put an initial location in `simulation/init.p`. This should be in the form of a pickled output from a previous run. Alternativley, this can be a tuple containin a dict with a `"coef"` key leading to an array of the initial state, e.g. `({'coef': np.random.normal(size=(p,1))},)`.

### Run sampler
From the home directory, run
```python simulation/run_gi_simulation.py $sampler $n $seed $thin $params $init $dt $unit_v $rr```

with the following arguments:
- `$sampler`:Use one of `bps`, `hbps`, `hbpsnuts`, or `cholesky` (Polya-Gamma sampler).
- `$n`: Number of samplers to generate.
- `$seed`: Random seed.
- `$thin`: Amount of samples to thin. 1 is no thinning, 2 removes every other sample, 3 removes every 3rd sample, etc.
- `$params`: `1`,`2`,or `3` depending on number of parameters to save. `1` saves the coefficients, global scale, and local scales. `2` adds the log densities. `3` saves everything.
- `$init`: `1` or `0`. `1` Initializes samples at the provided location. Otherwise defaults to bayesbridge alternative.
- `$dt`: Travel time or base step size if using NUTS. Not needed for Polya-Gamma.
- `$unit_v`: `1` to use unit velocities or `0` to use normally distributed. Was set to `0` for simulations.
- `$rr`: Refresh rate for BPS.

An example settings use for the best BPS run would be `sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=1.5,unit_v=0,rr=0.01`.

This will create the output as a pickled file with name `f"{hostname}_{sampler}_gi_{n}_seed{seed}_thin{thin}_params{params_int}_init{bool(init_int)}"` plus additional information on `dt`, `unit_v`, and `rr` depending on the sampler in the current directory, with `hostname` derived from your machine's name.