from collections import deque


def search_queue(name: str, graph):
    search_queue = deque()
    print(graph[name])
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        print(person)
        print(search_queue)
        if not(person in searched):
            if person == name:
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def create_graph():
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["tom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["tom"] = []
    graph["jonny"] = ["you"]
    return graph


graph = create_graph()
print(search_queue("you", graph))

