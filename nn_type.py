# -*- coding: utf-8 -*-
"""
Created on Thu Feb 06 12:57:36 2014

@author: wy
"""

from graph import *
num_connect = 10
class NN_SW(SmallWorldGraph):
    def addIOVertex(self,inputVertex,outputVertex):
        vs = list(self.vs)
        
        ivs = np.random.choice(vs,num_connect*len(inputVertex),replace = False)
        ovs = np.random.choice(vs,num_connect*len(outputVertex),replace = False)
        
        for v in inputVertex+outputVertex:
            self.add_vertex(v)
            
        for v1 in inputVertex:
            for v2 in ivs:
                self.add_edge(Edge(v1,v2))
        
        for v1 in outputVertex:
            for v2 in ovs:
                self.add_edge(Edge(v1,v2))