#!/usr/bin/env python
import numpy as np
import pdb
import itertools
import sys
import matplotlib.pyplot as plt


class fp():
    """
    Visualise multidimensional data as a fourier polynomial
    """
    def __init__(self, data, perm, N, mode='NULL'):
        self.data = [data[perm[0]],data[perm[1]],data[perm[2]],data[perm[3]]]
        self.perm = perm
        self.N    = N
        self.mode = mode
        self.x    = np.linspace(-np.pi,np.pi,N)
        self._compute()

    def _compute(self):
        self.poly = np.fft.fft(self.data, self.N)


class manyfp():
    """
    Handler for many visualisation objects
    """
    def __init__(self, data, perm, N, mode='NULL'):

        self.fpObjs = [fp(data[i], perm, N, mode) for i in range(len(data))]


def runPermute(N, perm, data):
    """
    Run a single permutation
    """
    
    setosa     = data[10:30]
    versicolor = data[60:80]
    virginica  = data[110:130]

    setoObj = manyfp(setosa    , perm, N)
    vesiObj = manyfp(versicolor, perm, N)
    virgObj = manyfp(virginica , perm, N)

    #pdb.set_trace()

    plt.figure(1)
    plt.title(str(perm), fontsize=12)
    sp = plt.subplot(1,1,1)
    for i in range(len(setosa)):
        sp.plot(setoObj.fpObjs[i].x, setoObj.fpObjs[i].poly, 'r') 
        sp.plot(vesiObj.fpObjs[i].x, vesiObj.fpObjs[i].poly, 'b') 
        sp.plot(virgObj.fpObjs[i].x, virgObj.fpObjs[i].poly, 'g') 
    plt.xlim([-np.pi,np.pi])

    plt.figure(2)
    plt.title(str(perm), fontsize=12)
    sp = plt.subplot(1,1,1)
    for i in range(len(setosa)):
        sp.plot(np.real(setoObj.fpObjs[i].poly), np.imag(setoObj.fpObjs[i].poly), 'r') 
        sp.plot(np.real(vesiObj.fpObjs[i].poly), np.imag(vesiObj.fpObjs[i].poly), 'b') 
        sp.plot(np.real(virgObj.fpObjs[i].poly), np.imag(virgObj.fpObjs[i].poly), 'g') 
    #plt.xlim([-np.pi,np.pi])
    
    plt.show()



def runManyPermute(N, perms, data):
    """
    Run many permutations
    """
    
    setosa     = data[10:30]
    versicolor = data[60:80]
    virginica  = data[110:130]

    for p in range(len(perms)):
        perm = perms[p]
        
        setoObj = manyfp(setosa    , perm, N)
        vesiObj = manyfp(versicolor, perm, N)
        virgObj = manyfp(virginica , perm, N)

        plt.figure(3)
        plt.title(str(perm), fontsize=8)
        sp = plt.subplot(4,6,p+1)
        for i in range(len(setosa)):
            sp.plot(setoObj.fpObjs[i].x, setoObj.fpObjs[i].poly, 'r') 
            sp.plot(vesiObj.fpObjs[i].x, vesiObj.fpObjs[i].poly, 'b') 
            sp.plot(virgObj.fpObjs[i].x, virgObj.fpObjs[i].poly, 'g') 
        sp.tick_params(axis='both',  labelsize=2)
        plt.xlim([-np.pi,np.pi])

        plt.figure(4)
        plt.title(str(perm), fontsize=8)
        sp = plt.subplot(4,6,p+1)
        for i in range(len(setosa)):
            sp.plot(np.real(setoObj.fpObjs[i].poly), np.imag(setoObj.fpObjs[i].poly), 'r') 
            sp.plot(np.real(vesiObj.fpObjs[i].poly), np.imag(vesiObj.fpObjs[i].poly), 'b') 
            sp.plot(np.real(virgObj.fpObjs[i].poly), np.imag(virgObj.fpObjs[i].poly), 'g') 
        sp.tick_params(axis='both',  labelsize=2)
        #plt.xlim([-np.pi,np.pi])
        
    plt.show()



def main():

    N    = 128
    cols = [0,1,2,3]
    p    = 8
   
    data  = np.loadtxt('iris.csv', usecols=cols, delimiter=',')

    perms = list(itertools.permutations(cols))

    runPermute(N, perms[p], data)
    runManyPermute(N, perms, data)




# Entry point
if __name__ == "__main__":
    sys.exit(main())


