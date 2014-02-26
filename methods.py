# -*- coding: utf-8 -*-
"""
Created on Thu Feb 06 13:13:57 2014

@author: wy
"""

import scipy.optimize as op
import numpy as np
from graph import sigmoid

def downhill(nn,data,label):
    #doesn't work.
    def costfunc(x,nn,data,label):
        x = list(x)[:]
        for e in nn.es:
            e.setValue(x.pop())
        cost = 0.0
        for i in range(len(data)):
            result = nn.active(data[i])
            cost += (result - np.array(label[i]))**2
        print 'cost = %f'%cost
        return cost
        
    op.fmin(costfunc,[np.random.random() for i in range(len(nn.es))],args = (nn,data,label))
    
    
    
    
    
def bp(nn,dl,learningRate):
    #doesn't work,either.   
    def getDerivative(v):
        if v.func == sum:
            return 1
        if v.func == sigmoid:
            fx = v.active()
            return (1-fx)*fx
        if v.func == None:
            return v.active()
            
            
            
    def change_value(v,error,learningRate):
        edges = v.getEdges()
        for v1 in edges:
            change_value(v1,error*edges[v1].getValue(),learningRate)
        for vertex,edge in edges.items():
            value = edge.getValue()
            value += learningRate*getDerivative(vertex)*vertex.active()
            edge.setValue(value)
            
    
    errRate = 0.0
    for d,l in dl:
        result = nn.active(d)
        errors = result-np.array(l)
        ve = zip(nn.outputVertex,errors)
        for vertex,err in ve:
            change_value(vertex,err,learningRate)
        errRate += abs(sum(errors)*1.0/sum(result))
        
    return errRate/len(dl)
    
def bp_method(nn,data,label,learningRate = 1,ep = 0.01):
    dl = zip(data,label)
    errRate = float('inf')
    while(errRate>ep):
        np.random.shuffle(dl)
        errRate = bp(nn,dl,learningRate)
        print 'errRate = %f'%errRate
    
    
    
    
    
    
    
    
        
            