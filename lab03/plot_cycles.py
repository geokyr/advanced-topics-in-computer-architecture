#!/usr/bin/env python

import sys, os
import itertools, operator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def get_params_from_basename(basename):
	tokens = basename.split('.')
	lock_type = tokens[0].replace('d', '')
	n_threads = int(tokens[1].split('-')[0].split('_')[1])
	grain_size = int(tokens[1].split('-')[1].split('_')[1])
	return (lock_type, n_threads, grain_size)

def get_time_from_output_file(output_file):
	time = -999
	fp = open(output_file, "r")
	line = fp.readline()
	while line:
		if line.strip().startswith("Cycles"):
			time = float(line.split()[2])
		line = fp.readline()

	fp.close()
	return time

def get_tuples_by_lock_type(tuples):
	ret = []
	
	tuples_sorted = sorted(tuples, key=operator.itemgetter(0, 1))
	
	for key,group in itertools.groupby(tuples_sorted,operator.itemgetter(0)):
		ret.append((key, zip(*map(lambda x: x[1:], list(group)))))
	return ret

if len(sys.argv) < 2:
	print("usage:", sys.argv[0], "<output_directories>")
	sys.exit(1)

results_tuples = {}

for dirname in os.listdir(sys.argv[1]):
	if dirname.endswith("/"):
		dirname = dirname[0:-1]
	basename = os.path.basename(dirname)
	output_file = sys.argv[1] + "/"  + dirname + "/sim.out"

	(lock_type, n_threads, grain) = get_params_from_basename(basename)
	time = get_time_from_output_file(output_file)
	results_tuples.setdefault(grain, []).append((lock_type, n_threads, time))

for (grain_size, res_tuples) in results_tuples.items():
	markers = ['.', 'o', 'v', '*', 'D']
	fig, ax = plt.subplots()
	plt.grid(True)
	ax.set_xlabel(r"$Number\ of\ Threads$", fontsize=14)
	ax.set_ylabel(r"$Cycles$", fontsize=14)

	i = 0
	print(res_tuples)
	tuples_by_lock_type = get_tuples_by_lock_type(res_tuples)


	for tuple in tuples_by_lock_type:
		print(tuple)
		lock_type = tuple[0]
		tuple_list = list(tuple[1])
		nthread_axis = tuple_list[0]
		time_axis = tuple_list[1]
		print("time ", lock_type, nthread_axis, time_axis)
		x_ticks = 2**np.arange(0, len(time_axis))

		ax.plot(x_ticks, time_axis, linewidth=1, label=str(lock_type), marker=markers[i%len(markers)])
		i = i + 1

	x_labels = map(str, x_ticks) 
	ax.xaxis.set_ticks(x_ticks)
	ax.xaxis.set_ticklabels(x_labels)
	
	box = ax.get_position()
	lgd = ax.legend(ncol=1, loc='upper left', bbox_to_anchor=(0, 0.9), prop={'size':10})
	plt.title('Grain Size: ' + str(grain_size))
	output_base = '/graphs/sniper/'
	output = output_base + 'grain-' + str(grain_size) + '.png'
	print("Saving: " 	+ output)
	plt.savefig(output, bbox_extra_artists=(lgd,), bbox_inches='tight')
