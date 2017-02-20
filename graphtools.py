


#takes in a starting point and a graph represented as a dictionary
def distancesfrom(entry,graph):
    visited =[entry]
    distances = {key:-1 for key in graph.keys()}
    distances[entry] = 0
    while(len(visited )< len(graph)):
        visitedbefore = len(visited );
        for unconnected in filter(lambda x: distances[x]==-1,graph.keys()):
            connected = list(filter(lambda x: unconnected in graph[x],visited))
            if len(connected) == 0: #if we haven't found a path yet we skip this iteration
                continue        
            shortest = min(connected,key=lambda x :distances[x])
            distances[unconnected] = distances[shortest] + 1
            visited.append(unconnected)
        if len(visited) <= visitedbefore: # if we didn't find more connections this iteration 
            return distances #graph is unconnected so return what we have so far
    return distances
        
def getpath(start,end,graph,distances ={}): #coded for two-way graphs only
    if len(distances) == 0: #if distances not provided
        distances = distancesfrom(start,graph)
    if distances[end] <0:
        return [] #return empty list if there is no path
    path = []
    iterator = end
    while(len(path) < (distances[end]+1)):        
        path.append(iterator)
        iterator = min(graph[iterator],key=lambda x:distances[x])
    path.reverse()
    return path

def distancesfromset(graph,subset):#breaks if unconnected
    if len(subset) <= 0:
        return {}
    distances = {point: 0 for point in subset}
    for node in filter(lambda x:x not in subset,graph.keys()):
        individualdistances = distancesfrom(node,graph)
        closestmember = min(subset,key=lambda x:individualdistances[x])
        distances[node] = individualdistances[closestmember]
    return distances    
    
        
    
    

#Test
if __name__ == '__main__':
    mgraph = {}
    mgraph['a']=('b','c')
    mgraph['b']=('a','c','d')
    mgraph['c']=('a','b','d','e')
    mgraph['d']=('b','c','e')
    mgraph['e']=('c','d','f')
    mgraph['f']=('e')
    mgraph['g']=() #disconnected
    START = 'a'
    print (distancesfrom('a',mgraph))
    print (distancesfrom('b',mgraph))
    print (distancesfrom('c',mgraph))
    print (getpath('a','d',mgraph))
    print (getpath('b','f',mgraph))
    print (getpath('a','g',mgraph))


                            
    

