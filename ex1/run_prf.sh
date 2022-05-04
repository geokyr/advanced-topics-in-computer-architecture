#!/bin/bash

## Modify the following paths appropriately
PARSEC_PATH=/home/george/adv-ca/parsec-3.0/
PIN_EXE=/home/george/adv-ca/pin-3.22-98547-g7a303a835-gcc-linux/pin
PIN_TOOL=/home/george/adv-ca/advcomparch-ex1-helpcode/pintool/obj-intel64/simulator.so

CMDS_FILE=/home/george/adv-ca/parsec-3.0/parsec_workspace/cmds_simlarge.txt
outDir="./outputs/PRF"

export LD_LIBRARY_PATH=$PARSEC_PATH/pkgs/libs/hooks/inst/amd64-linux.gcc-serial/lib/

## Triples of <cache_size>_<associativity>_<block_size>
CONFS="1 2 4 8 16 32 64"

L1size=32
L1bsize=64
L1assoc=8

L2size=1024
L2bsize=128
L2assoc=8

TLBe=64
TLBa=4
TLBp=4096

L2prf=0

BENCHMARKS="blackscholes bodytrack canneal fluidanimate freqmine rtview swaptions streamcluster"

for BENCH in $BENCHMARKS; do
	cmd=$(cat ${CMDS_FILE} | grep "$BENCH")
for conf in $CONFS; do
	## Get parameters
    L2prf=$conf

	outFile=$(printf "%s.dcache_cslab.PRF_%04d_%02d_%03d.out" $BENCH ${L2prf})
	outFile="$outDir/$outFile"

	pin_cmd="$PIN_EXE -t $PIN_TOOL -o $outFile -L1c ${L1size} -L1a ${L1assoc} -L1b ${L1bsize} -L2c ${L2size} -L2a ${L2assoc} -L2b ${L2bsize} -TLBe ${TLBe} -TLBp ${TLBp} -TLBa ${TLBa} -L2prf ${L2prf} -- $cmd"
	time $pin_cmd
done
done