# Directed Weighted Graph-PY<br>
![gr](https://user-images.githubusercontent.com/73124928/104851371-47d45500-58fd-11eb-8787-29f8c39fd230.png)

<strong><em> Author: Eden  Shemesh</em></strong><br>
This Project is part of OOP course in Ariel university.<br>
The implementation of the Directed Weighted Graph includes:<br>
3-Class: 
<ul>
<li>Vertex</li>
<li>DiGraph </li>
<li>Graph_Algo</li>
</ul>

2 Junit Tests:
<ul>
<li>TestDiGraph</li>
<li>TestGraphAlgo</li>
</ul>.<br>

### Main Classes and Methods:<br>
##### <strong>Vertex class<strong>:

Methods | Description | Complexity
--- | --- | ---
**addNeighbor** | **Add the information about connection between vertexes into the dictionary connectedTo** | **O(1)**
**getNi_key** | **Return the vertex's neighbors keys** | **O(1)**
**getNi_dict** | **Return the vertex's neighbors dict** | **O(1)**
**get_edge_Weight** | **Return the weight of the edge between self and nbr (two vertices)** | **O(1)**
**remove_ni** | **Remove from the dictionary "connectedTo" the element key** | **O(1)**.<br>


##### <strong>DiGraph<strong>:<br>
Methods | Description 
--- | --- | 
`add_node` | `Adds a node to the graph` 
`add_edge` | `Adds an edge to the graph.` 
`get_all_v` | `return a dictionary of all the nodes in the Graph(node_id, node_data)` 
`e_size` | `Returns the number of edges in this graph.` 
`v_size` | `Returns the number of vertices in this graph` 
`get_node` | `Returns the node that associated with the initial key.` 
`all_in_edges_of_node` | `Returns a dictionary of all the nodes connected to (into) node_id(other_node_id, weight).` 
`all_out_edges_of_node` | `Return a dictionary of all the nodes connected from node_id (other_node_id, weight).` 
`remove_node` | `Removes a node from the graph.` 
`remove_edge` | `Removes an edge from the graph.` 
`reverse_graph` | `Reversed all the edges in the graph.` 

##### <strong>Graph_Algo<strong>:<br>
Methods | Description 
--- | --- | 
*get_graph* | *Return the underlying graph of which this class works* 
*save_to_json* | *Adds a node to the graph*
*load_from_json* | *Saves the graph in JSON format to a file* 
*shortest_path* | *Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm* 
*connected_component* | *Finds the Strongly Connected Component(SCC) that node id1 is a part of.* 
*connected_components* | *Finds all the Strongly Connected Component(SCC) in the graph.* 
*plot_graph* | *Plots the graph.* 

### Scc connected_components:<br>
In the TestGraphAlgo there is test method of: " connected_components " AND "connected_component",<br>
of the graph below:<br>
![SSC](https://user-images.githubusercontent.com/73124928/104851506-0d1eec80-58fe-11eb-9c25-ccb50ab8d142.png)<br>
### Shortest_path:<br>
In the TestGraphAlgo there is test method of: "  shortest_path ",<br>
shortest_path from v0 to v4 is :6 <br>
path :[V0 V1 V2 V3 V4] <br>
![pic3](https://user-images.githubusercontent.com/73124928/104851745-8703a580-58ff-11eb-8811-406e5c1d5176.png)



 







