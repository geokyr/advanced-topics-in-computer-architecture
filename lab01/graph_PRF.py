# Plotting Code (PRF)
# You shouldn't run this directly, run plotter_PRF.sh instead.
# Dependencies: python, matplotlib, numpy

import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x_Axis = []
ipc_Axis = []
mpki_Axis = []

for outFile in sys.argv[2:]:
    fp = open(outFile)
    line = fp.readline()
    while line:
        tokens = line.split()
        if (line.startswith("Total Instructions: ")):
            total_instructions = int(tokens[2])
        elif (line.startswith("IPC:")):
            ipc = float(tokens[1])
        elif (line.startswith("L2_prefetching")):
            l2_prf = int(tokens[3].split(')')[0])
        elif (line.startswith("L2-Total-Misses")):
            l2_total_misses = int(tokens[1])
            l2_miss_rate = float(tokens[2].split('%')[0])
            mpki = l2_total_misses / (total_instructions / 1000.0)

        line = fp.readline()

    fp.close()

    prfConfigStr = '{}'.format(l2_prf)
    print(prfConfigStr)
    x_Axis.append(prfConfigStr)
    ipc_Axis.append(ipc)
    mpki_Axis.append(mpki)

print(x_Axis)
print(ipc_Axis)
print(mpki_Axis)

fig, ax1 = plt.subplots()
ax1.grid(True)
ax1.set_xlabel("Prefetching n")

xAx = np.arange(len(x_Axis))
ax1.xaxis.set_ticks(np.arange(0, len(x_Axis), 1))
ax1.set_xticklabels(x_Axis, rotation=45)
ax1.set_xlim(-0.5, len(x_Axis) - 0.5)
ax1.set_ylim(min(ipc_Axis) - 0.05 * min(ipc_Axis), max(ipc_Axis) + 0.05 * max(ipc_Axis))
ax1.set_ylabel("$IPC$")
line1 = ax1.plot(ipc_Axis, label="IPC", color="red",marker='x')

ax2 = ax1.twinx()
ax2.xaxis.set_ticks(np.arange(0, len(x_Axis), 1))
ax2.set_xticklabels(x_Axis, rotation=45)
ax2.set_xlim(-0.5, len(x_Axis) - 0.5)
ax2.set_ylim(min(mpki_Axis) - 0.05 * min(mpki_Axis), max(mpki_Axis) + 0.05 * max(mpki_Axis))
ax2.set_ylabel("$MPKI$")
line2 = ax2.plot(mpki_Axis, label="L2D_MPKI", color="green",marker='o')

lns = line1 + line2
labs = [l.get_label() for l in lns]

plt.title(str(sys.argv[1]))
plt.suptitle("IPC vs MPKI")
lgd = plt.legend(lns, labs)
lgd.draw_frame(False)
plt.savefig("PRF.png",bbox_inches="tight")
