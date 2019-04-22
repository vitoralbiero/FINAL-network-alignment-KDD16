#!/bin/csh

#$ -pe smp 4           # Specify parallel environment and legal core size
#$ -q long             # Specify queue (use ‘debug’ for development)
#$ -N test_final         # Specify job name

module add matlab

bash exp_final.sh 
