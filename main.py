#!/usr/bin/env python
import numpy as np
import pdb
import itertools
import sys
import matplotlib.pyplot as plt

def fourier_curve(x,theta):
    base_functions = [lambda x : x[0]/2, 
                      lambda x : x[1]*np.sin (1.*theta), 
                      lambda x : x[2]*np.cos (1.*theta), 
                      lambda x : x[3]*np.sin (2.*theta)]
    curve = np.zeros(len(theta))
    for f in base_functions:
        curve = curve + f(x)
    return curve


def plot_permut(l,data,n):
    """ Plot a single permutation of a fourier curve """
    
    theta = np.linspace(-np.pi,np.pi,100)
    
    plt.figure(1)
    sp = plt.subplot(4,6,n+1)
    sp.tick_params(axis='both',  labelsize=2)
    plt.title(str(l), fontsize=8)

    for s in data[10:30]:
        x = [s[l[0]],s[l[1]],s[l[2]],s[l[3]]]
        sp.plot(theta, fourier_curve(x,theta), 'r')

    for s in data[60:80]:
        x = [s[l[0]],s[l[1]],s[l[2]],s[l[3]]]
        sp.plot(theta, fourier_curve(x,theta), 'b')

    for s in data[110:130]:
        x = [s[l[0]],s[l[1]],s[l[2]],s[l[3]]]
        sp.plot(theta, fourier_curve(x,theta), 'g')

    plt.ylim([-10,20])
    plt.xlim([-np.pi,np.pi])


def main():
    cols  = [0,1,2,3]
    data  = np.loadtxt('iris.csv', usecols=cols, delimiter=',')
    perms = list(itertools.permutations(cols))
    
    for n in range(len(perms)):
        print "%2d)  Permutation - %s" % (n, str(perms[n]))
        plot_permut(perms[n], data, n)

    plt.show()


# Entry point
if __name__ == "__main__":
    sys.exit(main())

