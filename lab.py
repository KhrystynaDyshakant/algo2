from collections import deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        visited.add(node)
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited

def find_root(graph):
    for candidate in graph:
        if not any(candidate in bfs(graph, v) for v in graph if v != candidate):
            return candidate
    return -1

def read_graph(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            node = int(parts[0])
            neighbors = [int(x) for x in parts[1:]]
            graph[node] = neighbors
    return graph

def main():
    input_filename = "input.txt"
    output_filename = "output.txt"

    graph = read_graph(input_filename)
    root = find_root(graph)

    with open(output_filename, 'w') as output_file:
        output_file.write(str(root))

if __name__ == "__main__":
    main()