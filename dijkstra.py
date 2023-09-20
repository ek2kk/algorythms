# алгоритм дейкстры для направленных графов

def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra(graph, costs, parents):
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    return costs["end"]


# graph = {"start": {"a": 6, "b": 2}, "a": {"end": 1}, "b": {"a": 3, "end": 5}, "end": None}
graph = {}
graph["start"] = {}
graph["start"]["a"] = 1
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["end"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5
graph["end"] = {}

infinity = float("inf")
costs = {"a": 1, "b": 2, "end": infinity}
parents = {"a": "start", "b": "start", "end": None}

print(dijkstra(graph, costs, parents))
