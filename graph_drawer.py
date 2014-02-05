# -*- coding: utf-8 -*-
"""
Created on Wed Feb 05 14:47:14 2014

@author: wy
"""




def output_to_pajek(graph,filename = 'result.net'):
    table = {}
    vs = list(graph.vs)
    es = list(graph.es)
    f = file(filename,'w')
    print >>f,r'*Vertices %d'%len(vs)
    for i in range(len(vs)):
        print >>f,r'%d "%s"'%(i+1,repr(vs[i]))
        table[vs[i]] = i + 1
    print >>f,r'*edges'
    for e in es:
        v,w = e.getVertex()
        s = r'%d %d %d'%(table[v],table[w],e.value)
        print >>f,s
    f.close()
    
def output_directed_to_pajek(start,filename = 'directed.net'):
    table = {}
    visited = set()
    vs = ''
    es = ''
    fringe = start
    while(len(fringe)):
        new_fringe = set()
        for v in fringe:
            table.setdefault(v,len(table)+1)
            if not v in visited:
                vs += '%d "%s"\n'%(table[v],repr(v))
                visited.add(v)
            edges = v.getEdges()
            for v2 in edges:
                if v2 in visited:
                    continue
                table.setdefault(v2,len(table)+1)
                es += '%d %d %f\n'%(table[v2],table[v],edges[v2].getValue())
                new_fringe.add(v2)
        fringe = new_fringe
        
    
    
    
    
    f = file(filename,'w')
    print >>f,'*Vertices %d'%len(table)
    print >>f,vs
    print >>f,'*Arcs'
    print >>f,es
    f.close()
        
    













