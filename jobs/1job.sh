#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=24:00:00
#SBATCH --job-name=Petrogas
#SBATCH --partition=htc
#SBATCH --mail-type=ALL
#SBATCH --mail-user=matias.delgadino@maths.ox.ac.uk
#SBATCH --output=/home/delgadino/Desktop/gas/logs/1-job.out
#SBATCH --error=/home/delgadino/Desktop/gas/logs/1-job.err
#================================================================================
# job created on Fri 9 Oct 18:45:38 BST 2020
module load anaconda3/2019.03
source activate /data/math-gan-pdes/math1656/tensor-env
python /home/delgadino/Desktop/gas/gas.py 21
