#!/usr/bin/env python

import numpy as np
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

outputDir = "/home/george/adv-ca/parsec-3.0/parsec_workspace/graphs/4-1/"
outFilesDir = "/home/george/adv-ca/parsec-3.0/parsec_workspace/outputs/4-1/"

total, conditionalNotTaken, conditionalTaken, unconditional, calls, returns = 0, 0, 0, 0, 0, 0
instructions = []
benches = []

for outFile in os.listdir(outFilesDir):
    print("outFile", outFile)
    fp = open(outFilesDir + outFile)

    benchName = outFile.split('/')[-1]
    titleTokens = benchName.split('.')
    title = titleTokens[0] + '.' + titleTokens[1]
    benches.append(title)

    line = fp.readline()
    while line:
        line = line.strip()
        tokens = line.split()
        if line.startswith("Total Instructions:"):
            total = float(tokens[2])
        elif line.startswith("Total-Branches"):
            totalBranches = float(tokens[1])
        elif line.startswith("Conditional-Taken-Branches:"):
            conditionalTaken = float(tokens[1])
        elif line.startswith("Conditional-NotTaken"):
            conditionalNotTaken = float(tokens[1])
        elif line.startswith("Unconditional-Branches"):
            unconditional = float(tokens[1])
        elif line.startswith("Calls"):
            calls = float(tokens[1])
        elif line.startswith("Returns"):
            returns = float(tokens[1])
        line = fp.readline()

    conditionalTaken = (conditionalTaken / totalBranches) * 100
    conditionalNotTaken = (conditionalNotTaken / totalBranches) * 100
    unconditional = (unconditional / totalBranches) * 100
    calls = (calls / totalBranches) * 100
    returns = (returns / totalBranches) * 100
    instructions.append(total)

    labels = ['Conditional-Taken ('+"{:.2f}".format(conditionalTaken)+'%)',
        'Conditional-NotTaken ('+"{:.2f}".format(conditionalNotTaken)+'%)',
        'Unconditional ('+"{:.2f}".format(unconditional)+'%)',
        'Calls ('+"{:.2f}".format(calls)+'%)',
        'Returns ('+"{:.2f}".format(returns)+'%)']

    sizes = [conditionalTaken, conditionalNotTaken, unconditional, calls, returns]

    fig = plt.figure()
    ax = plt.subplot(111)
    plt.axis('equal')

    radius = 0.75
    colors = ['#173F5F','#ED553B', '#3CAEA3', '#20639B', '#F6D55C']
    wedges, texts = plt.pie(sizes, radius=radius, colors=colors, wedgeprops=dict(width=0.4), startangle=180)
    bbox_props = dict(boxstyle="square,pad=0.1", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
            bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = radius*np.sin(np.deg2rad(ang))
        x = radius*np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})

    percentage = float(totalBranches)/total*100
    stats = 'Total Branches: ' + str(int(totalBranches)) + " - {:.2f}% ".format(percentage)  + "of total instructions"
    plt.title(stats, fontsize=12)
    plt.suptitle(title, fontsize=16, fontweight="bold")

    box = ax.get_position()
    ax.legend(wedges, labels, loc='center left', bbox_to_anchor=(1, 0.5))

    plt.savefig(outputDir + title.replace('.', '-') + '.png', bbox_inches="tight", pad_inches=0.3)

plt.figure()
fig, ax = plt.subplots()
ax.grid(axis='x')
ax.set_axisbelow(True)
matplotlib.axes.Axes.ticklabel_format(ax, axis='x', style='sci', useMathText=True)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_color('darkgray')
ax.spines['left'].set_visible(True)
ax.spines['left'].set_color('darkgray')

y_pos = np.arange(len(benches))

matplotlib.axes.Axes.tick_params(ax, colors='dimgray')
p = ax.barh(y_pos, instructions, height=0.4, align='center', color='#29ccbb')
ax.set_yticks(y_pos)
ax.set_yticklabels(benches)
ax.invert_yaxis()
ax.set_xlabel('Total Instructions', color='dimgray')
ax.set_title('Total Instructions', color='k')

plt.savefig(outputDir + "total.png",bbox_inches="tight", pad_inches=0.3)