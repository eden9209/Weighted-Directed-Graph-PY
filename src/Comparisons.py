from src.GraphAlgo import GraphAlgo
import networkx as nx
import datetime


def test_time1(file_name: str):
    g_nx = nx.Graph()
    graph = GraphAlgo()
    graph.load_from_json(file_name)
    for i in graph.get_graph().get_all_v().keys():
        g_nx.add_node(i)
    for node in graph.get_graph().get_all_v().values():
        for key, w in graph.get_graph().all_out_edges_of_node(node.getKey()).items():
            g_nx.add_edge(node.getKey(), key, weight=w)
    # nx Dijkstra time :
    nx_start = datetime.datetime.now()
    nx.shortest_path(g_nx, 0, 9)
    nx.shortest_path(g_nx, 9, 0)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("* Networkx time in Dijkstra  is: ", nx_time)
    # nx SCC time :
    nx_start = datetime.datetime.now()
    nx.connected_components(g_nx)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("* Networkx time in SCC is: ", nx_time)
    # my_graph Dijkstra time :
    my_start = datetime.datetime.now()
    graph.shortest_path(0, 9)
    graph.shortest_path(9, 0)
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("* Graph time in Dijkstra  is: ", my_time)
    # my_graph SCC time :
    my_start = datetime.datetime.now()
    graph.connected_components()
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("* Graph time in SCC  is: ", my_time)
    print("#################")


def test_time2(file_name: str):
    g_nx = nx.Graph()
    graph = GraphAlgo()
    graph.load_from_json(file_name)
    for i in graph.get_graph().get_all_v().keys():
        g_nx.add_node(i)
    for node in graph.get_graph().get_all_v().values():
        for key, w in graph.get_graph().all_out_edges_of_node(node.getKey()).items():
            g_nx.add_edge(node.getKey(), key, weight=w)
    # nx Dijkstra time :
    nx_start = datetime.datetime.now()
    nx.shortest_path(g_nx, 30, 95)
    nx.shortest_path(g_nx, 95, 30)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("* Networkx time in Dijkstra  is: ", nx_time)
    # nx SCC time :
    nx_start = datetime.datetime.now()
    nx.connected_components(g_nx)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("* Networkx time in SCC is: ", nx_time)
    # my_graph Dijkstra time :
    my_start = datetime.datetime.now()
    graph.shortest_path(0, 9)
    graph.shortest_path(9, 0)
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("* Graph time in Dijkstra  is: ", my_time)
    # my_graph SCC time :
    my_start = datetime.datetime.now()
    graph.connected_components()
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("* Graph time in SCC  is: ", my_time)
    print("#################")


def test_time3(file_name: str):
    g_nx = nx.Graph()
    graph = GraphAlgo()
    graph.load_from_json(file_name)
    for i in graph.get_graph().get_all_v().keys():
        g_nx.add_node(i)
    for node in graph.get_graph().get_all_v().values():
        for key, w in graph.get_graph().all_out_edges_of_node(node.getKey()).items():
            g_nx.add_edge(node.getKey(), key, weight=w)
    # nx Dijkstra time :
    nx_start = datetime.datetime.now()
    nx.shortest_path(g_nx, 11, 152)
    nx.shortest_path(g_nx, 152, 11)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("* Networkx time in Dijkstra  is: ", nx_time)
    # nx SCC time :
    nx_start = datetime.datetime.now()
    nx.connected_components(g_nx)
    nx_end = datetime.datetime.now()
    nx_time = (nx_end - nx_start)
    print("* Networkx time in SCC is: ", nx_time)
    # my_graph Dijkstra time :
    my_start = datetime.datetime.now()
    graph.shortest_path(11, 152)
    graph.shortest_path(152, 11)
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("* Graph time in Dijkstra  is: ", my_time)
    # my_graph SCC time :
    my_start = datetime.datetime.now()
    graph.connected_components()
    my_send = datetime.datetime.now()
    my_time = (my_send - my_start)
    print("* Graph time in SCC  is: ", my_time)
    print("#################")


if __name__ == '__main__':
    str_1 = "../data/G_10_80_1.json"
    str_2 = "../data/G_100_800_1.json"
    str_3 = "../data/G_1000_8000_1.json"
    str_4 = "../data/G_20000_160000_1.json"
    str_5 = "../data/G_10000_80000_1.json"
    test_time1(str_1)
    test_time2(str_2)
    test_time3(str_3)
    test_time3(str_4)
    test_time3(str_5)
