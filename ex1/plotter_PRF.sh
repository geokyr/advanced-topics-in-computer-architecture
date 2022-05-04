#!/bin/bash

# Plotter Script (PRF)
# Install python-matplotlib before running.

# This assumes a directory tree like the following:
# Main Project dir  ${ACA_PATH}
# ├ CSLab code dir  ${HLP_PATH}
# ├ Parsec dir      ${PAR_PATH}
# └ PIN dir         ${PIN_PATH}
# It also assumes that you used the bencher_PRF.sh script for the benchmarks

# ------------------------------------------------
# You should only have to change things below here
# ------------------------------------------------

# Project directory
ACA_PATH="${ACA_PATH:-/home/george/adv-ca}" &> /dev/null

# Main directories
PAR_PATH="${PAR_PATH:-${ACA_PATH}/parsec-3.0}" &> /dev/null

# ------------------------------------------------
# You should only have to change things above here
# ------------------------------------------------

# Workspace paths
WRK_PATH=${PAR_PATH}/parsec_workspace
OUT_PATH=${WRK_PATH}/outputs/PRF

# Benchmark array
declare -a BenchArray=(
        "blackscholes"
        "bodytrack"
        "canneal"
        "fluidanimate"
        "freqmine"
        "rtview"
        "swaptions"
        "streamcluster"
)

# Loop through the available benchmarks
for bench in "${BenchArray[@]}"; do
    python3 graph_PRF.py ${bench} ${OUT_PATH}/${bench}*
    mv PRF.png ./graphs/PRF/PRF_${bench}.png
done
