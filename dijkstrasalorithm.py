import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_edge(self, u, v, weight):
        if u not in self.vertices:
            self.vertices[u] = []
        self.vertices[u].append((v, weight))

    def dijkstra(self, start):
        visited = {}
        distance = {vertex: float('infinity') for vertex in self.vertices}
        distance[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_vertex in visited:
                continue

            visited[current_vertex] = True

            for neighbor, weight in self.vertices[current_vertex]:
                distance_to_neighbor = current_distance + weight

                if distance_to_neighbor < distance[neighbor]:
                    distance[neighbor] = distance_to_neighbor
                    heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))

        return distance

def main():
    g = Graph()
    g.add_edge('A', 'B', 2)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 7)
    g.add_edge('C', 'E', 3)
    g.add_edge('D', 'E', 1)
    g.add_edge('E', 'D', 2)

    start_vertex = 'A'
    shortest_distances = g.dijkstra(start_vertex)

    print("Shortest distances from vertex", start_vertex)
    for vertex, distance in shortest_distances.items():
        print(f"To {vertex}: {distance}")

if __name__ == "__main__":
    main()

