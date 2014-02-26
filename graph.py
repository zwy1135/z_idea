# -*- coding: utf-8 -*-
"""
Created on Tue Feb 04 17:51:20 2014

@author: wy
"""
import numpy as np


def sigmoid(x):
    x = np.sum(x)
    return 1./(np.e**-x + 1)  


class Graph(object):
    def __init__(self,vs = [],es = []):
        self.vs = set()
        self.es = set()
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)
            
    def add_vertex(self,v):
        self.vs.add(v)
        
    def remove_vertex(self,v):
        self.vs.remove(v)
        for v1 in self.vs:
            v1.removeEdge(v)
        
    def add_edge(self,e):
        self.es.add(e)
        v,w = e.getVertex()
        v.setEdge(w,e)
        w.setEdge(v,e)
    
    def remove_edge(self,e):
        try:
            self.es.remove(e)
        except:
            pass
        v,w = e.getVertex()
        v.removeEdge(w)
        w.removeEdge(v)
        
        
class DirectedGraph(Graph):
    def add_edge(self,e,s):
        self.es.add(e)
        v,w = e.getVertex()
        if v==s:
            v.setEdge(w,e)
            
        else:
            w.setEdge(v,w)
            
    
        
            
            
class Vertex(object):
    def __init__(self,label = '',func = sigmoid):
        self.label = label
        self.func = func
        self.value = 0.0
        self.edges = {}
        self.isupdated = False
        self.__str__ == self.__repr__
        
    def __repr__(self):
        return "Vertex %s"%self.label
            
        
    def setEdge(self,w,e):
        self.edges[w] = e
        
    def removeEdge(self,w):
        try:        
            del self.edges[w]
        except:
            pass
            #print 'Nothing to delete.'
            
    def getEdges(self):
        return self.edges
    
    
        
    def active(self):
        if self.func == None or self.isupdated:
            return self.value
        pairs = self.edges.items()
        para = [p[0].active()*p[1].getValue() for p in pairs]
        self.value = self.func(para)
        self.isupdated = True
        return self.value

    def update(self,value = None):
        if not value == None:
            self.value = value
        else:
            self.active() 
        
    
        
        
class Edge(object):
    def __init__(self,v1,v2,value = 1):
        self.edge = tuple([v1,v2])
        self.value = value
        self.__str__ == self.__repr__
        
    def __repr__(self):
        return "Edge(%s,%s)"%(repr(self.edge[0]),repr(self.edge[1]))
        
    def getVertex(self):
        return self.edge
        
    def setValue(self,value):
        self.value = value
        
    def getValue(self):
        return self.value
        
    
    
    
    
class SmallWorldGraph(Graph):
    def __init__(self,num,k,p):
        Graph.__init__(self)
        #add vertex
        for i in range(num):
            self.add_vertex(Vertex(str(i)))
        
        
        #构造正则图
        vs = list(self.vs)
        for i in range(num):
            for j in range(1,k + 1):
                idx = i+j
                if idx >= num:
                    idx -= num
                self.add_edge(Edge(vs[i],vs[idx]))
                
                
        #随机连边
        removelist = []
        for e in self.es:
            if np.random.random()<p:
                #print '<'
                removelist.append(e)
        for e in removelist:
            self.remove_edge(e)
            v1,v2 = np.random.choice(vs,2,replace = False)
            self.add_edge(Edge(v1,v2))
            
            
        
           
def findPathLength(s,t):
    fringe = [s]
    length = 0
    visited = set()
    while(len(fringe)):
        length += 1
        new_fringe = set()
        for v in fringe:
            for v1 in v.edges:
                if v1 == t:
                    return length
                if v1 in visited:
                    continue
                new_fringe.add(v1)
            visited.add(v)
        fringe = new_fringe
    return None
    
def findAverLength(graph):
    total = 0.0
    count = 0
    notfound = 0
    vs = list(graph.vs)
    for i in range(len(vs)):
        for j in range(1,len(vs)):
            l = findPathLength(vs[i],vs[j])
            if l == None:
                notfound +=1
                continue
            total += l
            count += 1
    return total/count,count,total,notfound
    
    
    
    
        
    
    
    
                  

        
        
if __name__=="__main__":
    sw = SmallWorldGraph(30,3,0.5)
    vs = sw.vs
    del sw
    print vs
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        