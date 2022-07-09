#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --time=00:15:00

module load anaconda
module load cuda
python pytorch_mnist.py
