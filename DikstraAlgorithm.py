graph = {}
graph["start"] = {} 
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph['a'] = {}
graph['a']['fin']= 1
graph['b'] = {}
graph['b']['fin']= 5
graph["b"]["a"] = 3

graph['fin'] = {}



infinity = float('inf')

costs = {}

costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity



parents = {}
parents['a'] = "start"
parents['b'] = "start"
parents["fin"]= None

'''print(graph)
print(costs)
print(parents)'''

processed = []

#function to find the lowest cost

def lowest_cost_node(costs):
    lowest_cost = infinity
    closest_node = None
    
    for i in costs:
        if costs[i] < lowest_cost and i not in processed:
            
            lowest_cost = costs[i]
            closest_node = i
    return closest_node
    
            
    
    
    
node = lowest_cost_node(costs) #start with the closest

#we found the lowest cost node above

#find the neighbors

while node is not None:
    neighbors = graph[node].keys()
    
    #find cost of neighbors
    for n in neighbors:
        cost = graph[node][n]
        
        if cost + costs[node] < costs[n]:#update costs table & update parents table
            costs[n] = cost + costs[node]
            parents[n] = node
    processed.append(node)
    
    node=lowest_cost_node(costs)
            
        
        
print(costs)
print(parents)








#add the node to processed list


#find lowest node again
node = lowest_cost_node(costs)





        

    
    
        
    
