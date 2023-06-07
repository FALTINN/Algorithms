def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_code = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_code = node
    return lowest_cost_code


def get_way(parent):
    if parent == "start":
        return "start < "
    else:
        way = get_way(parents[parent]) + parent
        return way + ' < ' if parent != 'fin' else way


def create_graph():
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["start"]["c"] = 1
    graph["a"] = {}
    graph["a"]["fin"] = 1
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5
    graph["c"] = {}
    graph["c"]["fin"] = 3
    graph["fin"] = {}
    return graph


def create_costs(infinity):
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["c"] = 1
    costs["fin"] = infinity
    return costs


def create_parents():
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["c"] = "start"
    parents["fin"] = None
    return parents


graph = create_graph()
infinity = float("inf")
costs = create_costs(infinity)
parents = create_parents()
processed = []
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print(costs["fin"])
print(get_way("fin"))