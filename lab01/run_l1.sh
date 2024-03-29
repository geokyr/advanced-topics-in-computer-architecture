#!/bin/bash

## Modify the following paths appropriately
PARSEC_PATH=/home/george/adv-ca/parsec-3.0/
PIN_EXE=/home/george/adv-ca/pin-3.23-98579-gb15ab7903-gcc-linux/pin
PIN_TOOL=/home/george/adv-ca/advcomparch-ex1-helpcode/pintool/obj-intel64/simulator.so

CMDS_FILE=/home/george/adv-ca/parsec-3.0/parsec_workspace/cmds_simlarge.txt
outDir="./outputs/L1"

export LD_LIBRARY_PATH=$PARSEC_PATH/pkgs/libs/hooks/inst/amd64-linux.gcc-serial/lib/

## Triples of <cache_size>_<associativity>_<block_size>
CONFS="32_4_64 32_8_32 32_8_64 32_8_128 64_4_64 64_8_32 64_8_64 64_8_128 128_8_32 128_8_64 128_8_128"

L2size=1024
L2assoc=8
L2bsize=128

TLBe=64
TLBa=4
TLBp=4096

L2prf=0

BENCHMARKS="blackscholes bodytrack canneal fluidanimate freqmine rtview swaptions streamcluster"

for bench in $BENCHMARKS; do
	cmd=$(cat ${CMDS_FILE} | grep "$bench")

	for conf in $CONFS; do

	## Get parameters
    	L1size=$(echo $conf | cut -d'_' -f1)
    	L1assoc=$(echo $conf | cut -d'_' -f2)
		L1bsize=$(echo $conf | cut -d'_' -f3)

		outFile=$(printf "%s.dcache_cslab.L1_%04d_%02d_%03d.out" $bench ${L1size} ${L1assoc} ${L1bsize})
		outFile="$outDir/$outFile"

		pin_cmd="$PIN_EXE -t $PIN_TOOL -o $outFile -L1c ${L1size} -L1a ${L1assoc} -L1b ${L1bsize} -L2c ${L2size} -L2a ${L2assoc} -L2b ${L2bsize} -TLBe ${TLBe} -TLBp ${TLBp} -TLBa ${TLBa} -L2prf ${L2prf} -- $cmd"
		time $pin_cmd
	done
done