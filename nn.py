# -*- coding: utf-8 -*-
"""
Created on Tue Feb 04 16:05:46 2014

@author: wy
"""



from nn_type import *
from graph_drawer import *
from methods import *


def buildDirectedGraph(dgraph,start,end):
    fringe = start
    #visited = set()
    while(len(fringe)):
        new_fringe = set()
        for v1 in fringe:
            dgraph.add_vertex(v1)
            edges = v1.getEdges()
            for v2 in edges:
                if not v2 in end:
                    new_fringe.add(v2)
                dgraph.remove_edge(edges[v2])
                dgraph.add_edge(Edge(v1,v2),v1)
        fringe = new_fringe
    for v in end:
        dgraph.add_vertex(v)
    return dgraph
                
            
    
    
    
    
    
    
    

class NN(DirectedGraph):
    def __init__(self,num_in,num_out,num_hide,k,p,ntype = NN_SW):
        DirectedGraph.__init__(self)
        num_hide = max(num_connect*num_in,num_connect*num_out,num_hide)
        UnDirectedGraph = ntype(num_hide,k,p)
        
        
        self.inputVertex = [Vertex('i'+str(i),func = None)for i in range(num_in)]
        self.outputVertex = [Vertex('o'+str(i),func = sum)for i in range(num_out)]
        
        
        
        UnDirectedGraph.addIOVertex(self.inputVertex,self.outputVertex)

                
        buildDirectedGraph(self,self.outputVertex,self.inputVertex)
        
    def active(self,data):
        for v in self.vs:
            v.isupdated = False
        data = data[:]
        data.reverse()
        for v in self.inputVertex:
            v.update(data.pop())
        return [v.active() for v in self.outputVertex]
        
    def fit(self,data,label,method):
        method(self,data,label)
        
        


        

    
            



if __name__=="__main__":
    nn = NN(2,1,20,3,0.5)
    #print findAverLength(nn)
    output_directed_to_pajek(nn.outputVertex)
    data = []
    label = []
    for x in range(1):
        for y in range(1):
            data.append([x,y])
            label.append([x and y])
    #print nn.active([100,100,100])
    nn.fit(data,label,bp_method)

        
        