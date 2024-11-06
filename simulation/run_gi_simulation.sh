module load conda
source activate env
source activate env
cd bayes-bridge
python simulation/run_gi_simulation.py $sampler $n $seed $thin $params $init $dt $unit_v $rr
