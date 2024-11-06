# Initial value
qsub -q "shared.q@compute-124" -l mem_free="32G",h_vmem="32G" -N chol_4k_noinit -m e -M achin23@jhu.edu -v sampler=cholesky,n=4000,seed=1,thin=1,params=1,init=0 run_gi_simulation.sh

# HBPS tune
qsub -q "shared.q@compute-124" -l mem_free="8G",h_vmem="8G" -N hbps_05 -m e -M achin23@jhu.edu -v sampler=hbps,n=5000,seed=1,thin=1,params=1,init=1,dt=0.5,unit_v=0 run_gi_simulation.sh
qsub -q "shared.q@compute-124" -l mem_free="8G",h_vmem="8G" -N hbps_1  -m e -M achin23@jhu.edu -v sampler=hbps,n=5000,seed=1,thin=1,params=1,init=1,dt=1,unit_v=0 run_gi_simulation.sh
qsub -q "shared.q@compute-124" -l mem_free="8G",h_vmem="8G" -N hbps_15 -m e -M achin23@jhu.edu -v sampler=hbps,n=5000,seed=1,thin=1,params=1,init=1,dt=1.5,unit_v=0 run_gi_simulation.sh
qsub -q "shared.q@compute-124" -l mem_free="8G",h_vmem="8G" -N hbps_2  -m e -M achin23@jhu.edu -v sampler=hbps,n=5000,seed=1,thin=1,params=1,init=1,dt=2,unit_v=0 run_gi_simulation.sh
qsub -q "shared.q@compute-124" -l mem_free="8G",h_vmem="8G" -N hbps_25 -m e -M achin23@jhu.edu -v sampler=hbps,n=5000,seed=1,thin=1,params=1,init=1,dt=2.5,unit_v=0 run_gi_simulation.sh

# HNUTS
qsub -q "shared.q@compute-124" -l mem_free="8G",h_vmem="8G" -N hbps1 -m e -M achin23@jhu.edu -v sampler=hbpsnuts,n=4000,seed=1,thin=1,params=1,init=1,dt=0.1,unit_v=0 run_gi_simulation.sh
qsub -q "shared.q@compute-124" -l mem_free="8G",h_vmem="8G" -N hbps2 -m e -M achin23@jhu.edu -v sampler=hbpsnuts,n=4000,seed=2,thin=1,params=1,init=1,dt=0.1,unit_v=0 run_gi_simulation.sh
qsub -q "shared.q@compute-124" -l mem_free="8G",h_vmem="8G" -N hbps3 -m e -M achin23@jhu.edu -v sampler=hbpsnuts,n=4000,seed=3,thin=1,params=1,init=1,dt=0.1,unit_v=0 run_gi_simulation.sh
qsub -q "shared.q@compute-124" -l mem_free="8G",h_vmem="8G" -N hbps4 -m e -M achin23@jhu.edu -v sampler=hbpsnuts,n=4000,seed=4,thin=1,params=1,init=1,dt=0.1,unit_v=0 run_gi_simulation.sh
qsub -q "shared.q@compute-124" -l mem_free="8G",h_vmem="8G" -N hbps5 -m e -M achin23@jhu.edu -v sampler=hbpsnuts,n=4000,seed=5,thin=1,params=1,init=1,dt=0.1,unit_v=0 run_gi_simulation.sh

# Chol
qsub -q "shared.q@compute-124" -l mem_free="20G",h_vmem="20G" -N chol1 -m e -M achin23@jhu.edu -v sampler=cholesky,n=2000,seed=1,thin=1,params=1,init=1 run_gi_simulation.sh
qsub -q "shared.q@compute-124" -l mem_free="20G",h_vmem="20G" -N chol2 -m e -M achin23@jhu.edu -v sampler=cholesky,n=2000,seed=2,thin=1,params=1,init=1 run_gi_simulation.sh
qsub -q "shared.q@compute-124" -l mem_free="20G",h_vmem="20G" -N chol3 -m e -M achin23@jhu.edu -v sampler=cholesky,n=2000,seed=3,thin=1,params=1,init=1 run_gi_simulation.sh
qsub -q "shared.q@compute-124" -l mem_free="20G",h_vmem="20G" -N chol4 -m e -M achin23@jhu.edu -v sampler=cholesky,n=2000,seed=4,thin=1,params=1,init=1 run_gi_simulation.sh
qsub -q "shared.q@compute-124" -l mem_free="20G",h_vmem="20G" -N chol5 -m e -M achin23@jhu.edu -v sampler=cholesky,n=2000,seed=5,thin=1,params=1,init=1 run_gi_simulation.sh


#BPS
qsub -q "shared.q@compute-124" -l mem_free="8G",h_vmem="8G" -N bps_dt15_rr001 -m e -M achin23@jhu.edu -v sampler=bps,n=3000,seed=1,thin=1,params=1,init=1,dt=1.5,unit_v=0,rr=0.01 run_gi_simulation.sh
qsub -q "shared.q@compute-124" -l mem_free="8G",h_vmem="8G" -N bps_dt15_rr001 -m e -M achin23@jhu.edu -v sampler=bps,n=3000,seed=2,thin=1,params=1,init=1,dt=1.5,unit_v=0,rr=0.01 run_gi_simulation.sh
qsub -q "shared.q@compute-124" -l mem_free="8G",h_vmem="8G" -N bps_dt15_rr001 -m e -M achin23@jhu.edu -v sampler=bps,n=3000,seed=3,thin=1,params=1,init=1,dt=1.5,unit_v=0,rr=0.01 run_gi_simulation.sh
qsub -q "shared.q@compute-124" -l mem_free="8G",h_vmem="8G" -N bps_dt15_rr001 -m e -M achin23@jhu.edu -v sampler=bps,n=3000,seed=4,thin=1,params=1,init=1,dt=1.5,unit_v=0,rr=0.01 run_gi_simulation.sh
qsub -q "shared.q@compute-124" -l mem_free="8G",h_vmem="8G" -N bps_dt15_rr001 -m e -M achin23@jhu.edu -v sampler=bps,n=3000,seed=5,thin=1,params=1,init=1,dt=1.5,unit_v=0,rr=0.01 run_gi_simulation.sh


# BPS tune
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt01_rr0005 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=0.1,unit_v=0,rr=0.005 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt01_rr001 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=0.1,unit_v=0,rr=0.01 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt01_rr005 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=0.1,unit_v=0,rr=0.05 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt01_rr01 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=0.1,unit_v=0,rr=0.1 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt01_rr02 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=0.1,unit_v=0,rr=0.2 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt01_rr04 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=0.1,unit_v=0,rr=0.4 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt01_rr06 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=0.1,unit_v=0,rr=0.6 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt01_rr08 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=0.1,unit_v=0,rr=0.8 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt01_rr1  -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=0.1,unit_v=0,rr=1   run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt01_rr12  -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=0.1,unit_v=0,rr=1.2   run_gi_simulation.sh

qsub -l mem_free="8G",h_vmem="8G" -N bps_dt05_rr0005 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=0.5,unit_v=0,rr=0.005 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt05_rr001 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=0.5,unit_v=0,rr=0.01 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt05_rr005 -m e -M achin23@jhu.edu -v sampler=bps,n=5000,seed=1,thin=1,params=1,init=1,dt=0.5,unit_v=0,rr=0.05 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt05_rr01 -m e -M achin23@jhu.edu -v sampler=bps,n=5000,seed=1,thin=1,params=1,init=1,dt=0.5,unit_v=0,rr=0.1 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt05_rr02 -m e -M achin23@jhu.edu -v sampler=bps,n=5000,seed=1,thin=1,params=1,init=1,dt=0.5,unit_v=0,rr=0.2 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt05_rr04 -m e -M achin23@jhu.edu -v sampler=bps,n=5000,seed=1,thin=1,params=1,init=1,dt=0.5,unit_v=0,rr=0.4 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt05_rr06 -m e -M achin23@jhu.edu -v sampler=bps,n=5000,seed=1,thin=1,params=1,init=1,dt=0.5,unit_v=0,rr=0.6 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt05_rr08 -m e -M achin23@jhu.edu -v sampler=bps,n=5000,seed=1,thin=1,params=1,init=1,dt=0.5,unit_v=0,rr=0.8 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt05_rr1  -m e -M achin23@jhu.edu -v sampler=bps,n=5000,seed=1,thin=1,params=1,init=1,dt=0.5,unit_v=0,rr=1   run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt05_rr12  -m e -M achin23@jhu.edu -v sampler=bps,n=5000,seed=1,thin=1,params=1,init=1,dt=0.5,unit_v=0,rr=1.2   run_gi_simulation.sh

qsub -l mem_free="8G",h_vmem="8G" -N bps_dt1_rr0005 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=1,unit_v=0,rr=0.005 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt1_rr001 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=1,unit_v=0,rr=0.01 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt1_rr005 -m e -M achin23@jhu.edu -v sampler=bps,n=2500,seed=1,thin=1,params=1,init=1,dt=1,unit_v=0,rr=0.05 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt1_rr01 -m e -M achin23@jhu.edu -v sampler=bps,n=2500,seed=1,thin=1,params=1,init=1,dt=1,unit_v=0,rr=0.1 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt1_rr02 -m e -M achin23@jhu.edu -v sampler=bps,n=2500,seed=1,thin=1,params=1,init=1,dt=1,unit_v=0,rr=0.2 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt1_rr04 -m e -M achin23@jhu.edu -v sampler=bps,n=2500,seed=1,thin=1,params=1,init=1,dt=1,unit_v=0,rr=0.4 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt1_rr06 -m e -M achin23@jhu.edu -v sampler=bps,n=2500,seed=1,thin=1,params=1,init=1,dt=1,unit_v=0,rr=0.6 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt1_rr08 -m e -M achin23@jhu.edu -v sampler=bps,n=2500,seed=1,thin=1,params=1,init=1,dt=1,unit_v=0,rr=0.8 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt1_rr1  -m e -M achin23@jhu.edu -v sampler=bps,n=2500,seed=1,thin=1,params=1,init=1,dt=1,unit_v=0,rr=1   run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt1_rr12  -m e -M achin23@jhu.edu -v sampler=bps,n=2500,seed=1,thin=1,params=1,init=1,dt=1,unit_v=0,rr=1.2   run_gi_simulation.sh


qsub -l mem_free="8G",h_vmem="8G" -N bps_dt15_rr0005 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=1.5,unit_v=0,rr=0.005 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt15_rr001 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=1.5,unit_v=0,rr=0.01 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt15_rr005 -m e -M achin23@jhu.edu -v sampler=bps,n=2000,seed=1,thin=1,params=1,init=1,dt=1.5,unit_v=0,rr=0.05 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt15_rr01 -m e -M achin23@jhu.edu -v sampler=bps,n=2000,seed=1,thin=1,params=1,init=1,dt=1.5,unit_v=0,rr=0.1 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt15_rr02 -m e -M achin23@jhu.edu -v sampler=bps,n=2000,seed=1,thin=1,params=1,init=1,dt=1.5,unit_v=0,rr=0.2 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt15_rr04 -m e -M achin23@jhu.edu -v sampler=bps,n=2000,seed=1,thin=1,params=1,init=1,dt=1.5,unit_v=0,rr=0.4 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt15_rr06 -m e -M achin23@jhu.edu -v sampler=bps,n=2000,seed=1,thin=1,params=1,init=1,dt=1.5,unit_v=0,rr=0.6 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt15_rr08 -m e -M achin23@jhu.edu -v sampler=bps,n=2000,seed=1,thin=1,params=1,init=1,dt=1.5,unit_v=0,rr=0.8 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt15_rr1  -m e -M achin23@jhu.edu -v sampler=bps,n=2000,seed=1,thin=1,params=1,init=1,dt=1.5,unit_v=0,rr=1   run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt15_rr12  -m e -M achin23@jhu.edu -v sampler=bps,n=2000,seed=1,thin=1,params=1,init=1,dt=1.5,unit_v=0,rr=1.2   run_gi_simulation.sh

qsub -l mem_free="8G",h_vmem="8G" -N bps_dt2_rr0005 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=2,unit_v=0,rr=0.005 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt2_rr001 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=2,unit_v=0,rr=0.01 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt2_rr005 -m e -M achin23@jhu.edu -v sampler=bps,n=1500,seed=1,thin=1,params=1,init=1,dt=2,unit_v=0,rr=0.05 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt2_rr01 -m e -M achin23@jhu.edu -v sampler=bps,n=1500,seed=1,thin=1,params=1,init=1,dt=2,unit_v=0,rr=0.1 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt2_rr02 -m e -M achin23@jhu.edu -v sampler=bps,n=1500,seed=1,thin=1,params=1,init=1,dt=2,unit_v=0,rr=0.2 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt2_rr04 -m e -M achin23@jhu.edu -v sampler=bps,n=1500,seed=1,thin=1,params=1,init=1,dt=2,unit_v=0,rr=0.4 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt2_rr06 -m e -M achin23@jhu.edu -v sampler=bps,n=1500,seed=1,thin=1,params=1,init=1,dt=2,unit_v=0,rr=0.6 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt2_rr08 -m e -M achin23@jhu.edu -v sampler=bps,n=1500,seed=1,thin=1,params=1,init=1,dt=2,unit_v=0,rr=0.8 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt2_rr1  -m e -M achin23@jhu.edu -v sampler=bps,n=1500,seed=1,thin=1,params=1,init=1,dt=2,unit_v=0,rr=1   run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt2_rr12  -m e -M achin23@jhu.edu -v sampler=bps,n=1500,seed=1,thin=1,params=1,init=1,dt=2,unit_v=0,rr=1.2   run_gi_simulation.sh

qsub -l mem_free="8G",h_vmem="8G" -N bps_dt25_rr0005 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=2.5,unit_v=0,rr=0.005 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt25_rr001 -m e -M achin23@jhu.edu -v sampler=bps,n=10000,seed=1,thin=1,params=1,init=1,dt=2.5,unit_v=0,rr=0.01 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt25_rr005 -m e -M achin23@jhu.edu -v sampler=bps,n=1500,seed=1,thin=1,params=1,init=1,dt=2.5,unit_v=0,rr=0.05 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt25_rr01 -m e -M achin23@jhu.edu -v sampler=bps,n=1500,seed=1,thin=1,params=1,init=1,dt=2.5,unit_v=0,rr=0.1 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt25_rr02 -m e -M achin23@jhu.edu -v sampler=bps,n=1500,seed=1,thin=1,params=1,init=1,dt=2.5,unit_v=0,rr=0.2 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt25_rr04 -m e -M achin23@jhu.edu -v sampler=bps,n=1500,seed=1,thin=1,params=1,init=1,dt=2.5,unit_v=0,rr=0.4 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt25_rr06 -m e -M achin23@jhu.edu -v sampler=bps,n=1500,seed=1,thin=1,params=1,init=1,dt=2.5,unit_v=0,rr=0.6 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt25_rr08 -m e -M achin23@jhu.edu -v sampler=bps,n=1500,seed=1,thin=1,params=1,init=1,dt=2.5,unit_v=0,rr=0.8 run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt25_rr1  -m e -M achin23@jhu.edu -v sampler=bps,n=1500,seed=1,thin=1,params=1,init=1,dt=2.5,unit_v=0,rr=1   run_gi_simulation.sh
qsub -l mem_free="8G",h_vmem="8G" -N bps_dt25_rr12  -m e -M achin23@jhu.edu -v sampler=bps,n=1500,seed=1,thin=1,params=1,init=1,dt=2.5,unit_v=0,rr=1.2   run_gi_simulation.sh

