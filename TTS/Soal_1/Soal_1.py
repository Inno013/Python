from collections import deque

def find_shortest_path(maze, start, end):
    """Fungsi ini akan mencari jalur terpendek dalam 
    labirin dari titik start ke titik end."""

    def get_valid_neighbors(node):
        x, y = node
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        valid_neighbors = []
        for neighbor in neighbors:
            nx, ny = neighbor
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == '.':
                valid_neighbors.append(neighbor)
        return valid_neighbors

    visited = set()
    queue = deque()
    parent = {}

    queue.append(start)
    visited.add(start)
    found = False

    while queue:
        node = queue.popleft()

        if node == end:
            found = True
            break

        for neighbor in get_valid_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = node

    if found:
        path = []
        current = end
        while current != start:
            path.append(current)
            current = parent[current]
        path.append(start)
        path.reverse()
        return path
    else:
        return []

# Contoh Labirin
maze = [
        ['.', '.', '.', 'X', 'X'],
        ['.', 'X', '.', '.', '.'],
        ['.', 'X', 'X', 'X', '.'],
        ['.', '.', '.', '.', '.'],
        ['X', 'X', 'X', 'X', '.'],
        ['.', '.', '.', '.', '.']
    ]

start = (0, 0)
end = (5, 4)

shortest_path = find_shortest_path(maze, start, end)

if shortest_path:
    print("Jalur terpendek:")
    for node in shortest_path:
        print(node)
else:
    print("Tidak ada jalur yang ditemukan.")