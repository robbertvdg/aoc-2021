from typing import List


def visited_small_cave_twice(route: List[str]):
    lower = [x for x in route if x.islower()]
    return len(lower) != len(set(lower))


def puzzle1(all_connections: List[List[str]], visit_twice=False) -> int:
    distinct_caves = list(set([x for y in all_connections for x in y]))
    connections = [[] for _ in distinct_caves]
    for connection in all_connections:
        connections[distinct_caves.index(connection[0])].append(connection[1])
        connections[distinct_caves.index(connection[1])].append(connection[0])
    distinct_routes = [['start']]
    completed_routes = []
    done = False
    while not done:
        route = distinct_routes.pop()
        cave = route[-1]
        connection_list = connections[distinct_caves.index(cave)]
        for conn in connection_list:
            if conn != "start":
                new_route = route.copy()
                new_route.append(conn)
                if conn == 'end':
                    completed_routes.append(new_route)
                elif conn not in route or conn.isupper() or (visit_twice and not visited_small_cave_twice(route)):
                    distinct_routes.append(new_route)
        if len(distinct_routes) == 0:
            done = True
    return len(completed_routes)


def read_input(path: str) -> List[List[str]]:
    with open(path, "r") as f:
        inputs = f.readlines()
        return [[y.strip() for y in x.split("-")] for x in inputs]


if __name__ == "__main__":
    cave_connections = read_input("./input.txt")
    answer1 = puzzle1(cave_connections)
    answer2 = puzzle1(cave_connections, True)
    print(f"The answer to day 12 puzzle 1: {answer1}")
    print(f"The answer to day 12 puzzle 2: {answer2}")
