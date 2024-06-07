class Graph:
    def __init__(self):
        self.adjacency_list = {}
    def add_edge(self, node1, node2):
        if node1 in self.adjacency_list:
            self.adjacency_list[node1].append(node2)
        else:
            self.adjacency_list[node1] = [node2]
        if node2 in self.adjacency_list:
            self.adjacency_list[node2].append(node1)
        else:
            self.adjacency_list[node2] = [node1]
    def dfs(self, start_node, target_node):
        visited = set()
        stack = []
        stack.append([start_node])
        while stack:
            path = stack.pop()
            current_node = path[-1]
            if current_node == target_node:
                return path
            if current_node not in visited:
                visited.add(current_node)
                neighbors = self.adjacency_list.get(current_node, [])
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append(new_path)
        return None

# Contoh penggunaan
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')
graph.add_edge('E', 'F')
graph.add_edge('E', 'G')
graph.add_edge('F', 'H')
graph.add_edge('G', 'H')
start_node = 'A'
target_node = 'H'
path = graph.dfs(start_node, target_node)
if path:
    print(f"Path from {start_node} to {target_node}: {' -> '.join(path)}")
else:
    print(f"There is no path from {start_node} to {target_node}")
