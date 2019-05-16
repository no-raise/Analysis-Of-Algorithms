import numpy
import heapq
from collections import defaultdict


def create_graph_weighted(data):
    graph = defaultdict(list)
    for s, d, w in data:
        graph[s].append([d, w])
        graph[d].append([s, w])

    return graph


def create_graph(data):
    graph = defaultdict(list)
    for s, d in data:
        graph[s].append(d)

    return graph


def dfs_recursive(v, visited, parent):
    global has_cycle
    visited[v] = True

    for child in graph_dfs[v]:
        if not visited[child]:
            dfs_recursive(child, visited, v)
        else:
            if parent != child:
                has_cycle = True
                break


def djikstras_shortest_path(origin, g):

    visited = set()
    dist = [numpy.inf for i in graph_djikstra.keys()]
    dist[origin] = 0
    queue = [(0, origin, ())]

    while queue:

        pre_cost, parent_node, path = heapq.heappop(queue)

        if parent_node not in visited:
            visited.add(parent_node)
            path += (parent_node,)

            if parent_node == g:
                return pre_cost, path

            for neighbours in graph_djikstra[parent_node]:
                current_node = neighbours[0]
                cost_to_node = neighbours[1] + pre_cost
                if dist[current_node] > cost_to_node:
                    dist[current_node] = cost_to_node

                heapq.heappush(queue, (cost_to_node, current_node, path))

    return numpy.inf


input_dfs = [
    [0, 1],
    [0, 2],
    [1, 0],
    [1, 3],
    [1, 2],
    [2, 1],
    [2, 0],
    [2, 4],
    [3, 1],
    [4, 2]

]


input_djikstra = [
    [0, 1, 3],
    [0, 2, 1],
    [1, 2, 4],
    [1, 3, 2],
    [2, 3, 3],
    [4, 0, 6]
]


if __name__ == "__main__":
    # Code for DFS
    graph_dfs = create_graph(input_dfs)
    has_cycle = False
    V = len(graph_dfs)
    num_cc = 0
    visited = [False] * V

    for i in graph_dfs.keys():
        if not visited[i]:
            dfs_recursive(i, visited, -1)
            num_cc += 1

    if has_cycle:
        print("Cycle was detected in the graph.")
    else:
        print("No Cycles were detected in the graph.")
    print("Number of connected components = {}\n".format(num_cc))

    # Code for Djikstras
    graph_djikstra = create_graph_weighted(input_djikstra)

    source = 4
    target = 3
    cost, path = djikstras_shortest_path(source, target)
    path_string  = "{}".format(source)

    print("Cost from {} to {} = {}".format(source, target, cost))
    for node in range(1, len(path)):
        path_string += ("-->{}".format(node))

    print(path_string)





