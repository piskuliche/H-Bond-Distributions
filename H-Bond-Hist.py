#!/usr/env python

# This is a python code meant for calculating the Hydrogen Bond Distributions
# This program needs to be run after Mesele's Hydrogen Bond Calculation Code.
# This program allows interactivity - Plots the Histograms with command line arguments.



import os, math, sys
import numpy as np
import argparse
import matplotlib.pyplot as plt
from argparse import RawTextHelpFormatter,SUPPRESS

#Argument parser section
parser = argparse.ArgumentParser(description='''Calculates histograms for each type of hydrogen bond structure in Methanol.''', formatter_class=RawTextHelpFormatter)

parser.add_argument('-start',   help="Line number corresponding to start of average. 0 to go from SOF+2", default=int(0))
parser.add_argument('-end',   help="Line number corresponding to end of average. 0 to go to EOF",default=int(0))
parser.add_argument('-plot', help="What to plot: [0] All [1] lliner, [2] ring, [3] branch, [4] cluster", default=int(0))
parser.add_argument('-bins', help="Binning Options: #,auto,fd,doane,scott,rice,sturges,sqrt",default=int(10))
parser.add_argument('-save', help="[0] for False [1] for True", default=int(0))
args=parser.parse_args();

skip_SOF=int(args.start)
skip_EOF=int(args.end)
showplot=int(args.plot)
try:
    histbins=int(args.bins)
except ValueError:
    histbins=str(args.bins)
    pass #It was a string not an int.
savedata=int(args.save)

data_lliner = np.genfromtxt('lliner.dat', usecols=(1), skip_header=(2+skip_SOF), skip_footer=skip_EOF)
data_ring = np.genfromtxt('ring.dat', usecols=(1), skip_header=(2+skip_SOF), skip_footer=skip_EOF)
data_branch = np.genfromtxt('branch.dat', usecols=(1), skip_header=(2+skip_SOF), skip_footer=skip_EOF)
data_cluster = np.genfromtxt('cluster.dat', usecols=(1), skip_header=(2+skip_SOF), skip_footer=skip_EOF)

if showplot == 1:
    plt.hist(data_lliner, bins=histbins, normed=True)
    if savedata == 1:
        lliner_hist  = np.histogram(data_lliner, bins=histbins, density=True)
        a=open('lliner.hist', 'wb')
        for i in range(0,len(lliner_hist[1])-1):
            a.write(str(lliner_hist[1][i]) + " " + str(lliner_hist[0][i])+"\n")
        a.close()
    plt.show()
elif showplot == 2:
    plt.hist(data_ring, bins=histbins, normed=True)
    if savedata == 1:
        ring_hist    = np.histogram(data_ring, bins=histbins, density=True)
        b=open('ring.hist', 'wb')
        for i in range(0,len(ring_hist[1])-1):
            b.write(str(ring_hist[1][i]) + " " + str(ring_hist[0][i])+"\n")
        b.close
    plt.show()
elif showplot == 3:
    plt.hist(data_branch, bins=histbins, normed=True)
    if savedata == 1:
        branch_hist  = np.histogram(data_branch, bins=histbins, density=True)
        c=open('branch.hist', 'wb')
        for i in range(0,len(branch_hist[1])-1):
            c.write(str(branch_hist[1][i]) + " " + str(branch_hist[0][i])+"\n")
        c.close
    plt.show()
elif showplot == 4:
    plt.hist(data_cluster, bins=histbins, normed=True)
    if savedata == 1:
        cluster_hist = np.histogram(data_cluster, bins=histbins, density=True)
        d=open('cluster.hist', 'wb')
        for i in range(0,len(cluster_hist[1])-1):
            d.write(str(cluster_hist[1][i]) + " " + str(cluster_hist[0][i])+"\n")
        d.close()
    plt.show()
else:
    lliner_hist  = np.histogram(data_lliner, bins=histbins, density=True)
    ring_hist    = np.histogram(data_ring, bins=histbins, density=True)
    branch_hist  = np.histogram(data_branch, bins=histbins, density=True)
    cluster_hist = np.histogram(data_cluster, bins=histbins, density=True)
    # Write out histograms to file:
    a=open('lliner.hist', 'wb')
    b=open('ring.hist', 'wb')
    c=open('branch.hist', 'wb')
    d=open('cluster.hist', 'wb')
    for i in range(0,len(lliner_hist[1])-1):
        a.write(str(lliner_hist[1][i]) + " " + str(lliner_hist[0][i])+"\n")
    a.close()
    for i in range(0,len(ring_hist[1])-1):
        b.write(str(ring_hist[1][i]) + " " + str(ring_hist[0][i])+"\n")
    b.close
    for i in range(0,len(branch_hist[1])-1):
        c.write(str(branch_hist[1][i]) + " " + str(branch_hist[0][i])+"\n")
    c.close
    for i in range(0,len(cluster_hist[1])-1):
        d.write(str(cluster_hist[1][i]) + " " + str(cluster_hist[0][i])+"\n")
    d.close
