# -*- coding: utf-8 -*-
"""
Created on Tue Feb 04 16:05:46 2014

@author: wy
"""



from graph_rebuild import *
from graph_drawer import *


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
    def __init__(self,num_in,num_out,num_hide,k,p,ntype = SmallWorldGraph):
        DirectedGraph.__init__(self)
        UnDirectedGraph = ntype(num_hide,k,p)
        
        
        self.inputVertex = [Vertex('i'+str(i),func = None)for i in range(num_in)]
        self.outputVertex = [Vertex('o'+str(i),func = sum)for i in range(num_out)]
        
        
        
        vs = list(UnDirectedGraph.vs)
        
        ivs = np.random.choice(vs,3*num_in,replace = False)
        ovs = [v for v in vs if not v in ivs][:3*num_out]
        
        for v in self.inputVertex+self.outputVertex:
            UnDirectedGraph.add_vertex(v)
        
        for v1 in self.inputVertex:
            for v2 in np.random.choice(ivs,3,replace = False):
                UnDirectedGraph.add_edge(Edge(v1,v2))
                
        for v1 in self.outputVertex:
            for v2 in np.random.choice(ovs,3,replace = False):
                UnDirectedGraph.add_edge(Edge(v1,v2))

                
        buildDirectedGraph(self,self.outputVertex,self.inputVertex)
        
    def active(self,data):
        for v in self.vs:
            v.isupdated = False
        data.reverse()
        for v in self.inputVertex:
            v.update(data.pop())
        for v in self.outputVertex:
            v.update()
        return [v.value for v in self.outputVertex]
        
        


        

    
            



if __name__=="__main__":
    nn = NN(3,1,500,2,0.1)
    #print findAverLength(nn)
    #output_directed_to_pajek(nn.outputVertex)
    print nn.active([100,100,100])

        
        