#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --mem=1000M
#SBATCH --job-name=triton-test
#SBATCH --output=./output/triton-test_%A_%a.out
#SBATCH --array=0-4

case $SLURM_ARRAY_TASK_ID in
   0)  SEED=123 ;;
   1)  SEED=38  ;;
   2)  SEED=22  ;;
   3)  SEED=60  ;;
   4)  SEED=432 ;;
esac

srun python test.py --seed=$SEED > pi_$SEED.json


