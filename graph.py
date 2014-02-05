# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:04:45 2014

@author: wy
"""

import numpy as np
import scipy as sp

class Graph(dict):
    def __init__(self,vs= [],es = []):
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)
            
    def add_vertex(self,v):
        #self[v] = {}
        self.setdefault(v,{})
        
    def add_edge(self,e):
        v,w = e.getVertex()        
        self[v][w] = e
        self[w][v] = e
        
class DirectedGraph(Graph):
    def add_edge(self,e,s):
        v,w = e.getVertex()
        if v == s:        
            self[v][w] = e
        else:
            self[w][v] = e
        
        
        
class Vertex(object):
    def __init__(self,label = '',func = sum ):
        self.label = label
        self.func = func
        self.value = 0
        self.__str__ == self.__repr__
        
    def __repr__(self):
        return "Vertex %s"%self.label
        
    
    def active(self,para):
        return self.func(para)
        
    def update(self,para):
        self.value = self.func(para)
        
class Edge(object):
    def __init__(self,v1,v2,value = 1):
        self.edge = tuple([v1,v2])
        self.value = value
        
    def __repr__(self):
        return "Edge(%s,%s)"%(repr(self.edge[0]),repr(self.edge[1]))
        
    __str__ =__repr__
    
    def getVertex(self):
        return self.edge
    
    
    
    
    
    
class SmallWorldGraph(object):
    def __init__(self,num,k,p):
        self.vs = set()
        self.es = set()
        
        
        #加入节点
        for i in range(num):
            self.vs.add(Vertex(str(i),sigmoid))
            
        
        #构造正则图  
        vs = list(self.vs)          
        for i in range(num):
            for j in range(1,k + 1):
                idx = i+j
                if idx>=num:
                    idx -= num
                
                self.es.add(Edge(vs[i],vs[idx]))
                
        #随机连边
        removelist = []
        for e in self.es:
            if np.random.random()<p:
                removelist.append(e)
                
        for e in removelist:
            self.es.remove(e)
            i1,i2 = np.random.randint(0,num,2)
            self.es.add(Edge(vs[i1],vs[i2]))
            
        self.graph = Graph(self.vs,self.es)
        
        
        
        
def findPathLength(graph,v1,v2):
    distance = 0
    visited = set()
    fring = set([v1])
    if v1 == v2:
        return 0
    while 1:
        newfring = set()
        distance += 1
        for v in fring:
            for nv in graph[v].keys():
                if nv == v2:
                    return distance
                if not nv in visited:
                    newfring.add(nv)
                    visited.add(nv)
        fring = newfring
        if len(fring)==0:
            return None
            
def findAverLength(graph):
    vs = graph.keys()
    distances = []
    count = 0.0
    nf = 0.0
    for i in range(len(vs)):
        for j in range(len(vs)):
            count += 1
            dis = findPathLength(graph,vs[i],vs[j])
            if dis:
                distances.append(dis)
            else:
                nf += 1.0
    return np.sum(distances)*1.0/len(distances),nf/count
    
    
    
def sigmoid(x):
    x = np.sum(x)
    return 1./(np.e**-x + 1.)
    

                
                
        
def buildDirectedGraph(ugraph,o_vertexs):
        dgraph = DirectedGraph()
        fringe = o_vertexs
        visited = set()
        while(len(fringe)):
            new_fringe = set()
            for v in fringe:
                dgraph.add_vertex(v)
                for v2 in ugraph[v]:
                    if v2 in visited:
                        continue
                    new_fringe.add(v2)
                    dgraph.add_vertex(v2)
                    e = ugraph[v][v2]
                    dgraph.add_edge(e,v)
                visited.add(v)
            fringe = new_fringe
        
        return dgraph        
        
        
    
    
    
    
if __name__ == "__main__":
    #v = Vertex('v')
    #w = Vertex("w")
    #e = Edge(v,w)
    #g = Graph([v,w],[e])
    
    #print g
    sw = SmallWorldGraph(30,3,0.4)
    #print sw.graph
#    vs = list(sw.vs)
#    for v1 in vs:
#        for v2 in vs:
#            print v1,v2
#            print findPathLength(sw.graph,v1,v2)
    dgraph = buildDirectedGraph(sw.graph,np.random.choice(list(sw.vs),3,replace = False))
    print findAverLength(sw.graph)
    
        
    
        
        