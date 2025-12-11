import heapq

# Based on https://www.youtube.com/watch?v=wU6udHRIkcc
class DisjointSet:
    def __init__(self, size):
        self.parent = [-1] * size
    
    def find(self, i):
        j = i
        while self.parent[j] >= 0:
            j = self.parent[j]

        # Collapsing find
        if j != i:
            self.parent[i] = j

        return j
    
    def union(self, i, j):
        i_root = self.find(i)
        j_root = self.find(j)

        if i_root == j_root:
            return -self.parent[i_root]
        
        if self.parent[i_root] <= self.parent[j_root]:
            self.parent[i_root] += self.parent[j_root]
            self.parent[j_root] = i_root
            return -self.parent[i_root]
        else:
            self.parent[j_root] += self.parent[i_root]
            self.parent[i_root] = j_root
            return -self.parent[j_root]

def read_input(file):
    boxes = []
    
    with open(file, "r") as f:    
        for line in f:
            x, y, z = map(int, line.strip().split(','))
            boxes.append((x, y, z))
          
    return boxes

def part1(input_file):
    boxes = read_input(input_file)
    num_boxes = len(boxes)
    max_heap = [] 

    for i in range(num_boxes):
        x1, y1, z1 = boxes[i]
        for j in range(i + 1, num_boxes):
            x2, y2, z2 = boxes[j]
            dist = ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)**0.5
            if len(max_heap) < 1000:
                # Simulate a max heap by negating the distances
                heapq.heappush(max_heap, (-dist, i, j))
            else:
                # Only store the 1000 smallest distances
                heapq.heappushpop(max_heap, (-dist, i, j))

    ds = DisjointSet(num_boxes)

    for _, i, j in max_heap:
        ds.union(i, j)

    ans = 1
    for neg_size in sorted(ds.parent)[:3]:
        ans *= (-neg_size)
    
    return ans

def part2(input_file):
    boxes = read_input(input_file)
    num_boxes = len(boxes)
    distances = [] 

    for i in range(num_boxes):
        x1, y1, z1 = boxes[i]
        for j in range(i + 1, num_boxes):
            x2, y2, z2 = boxes[j]
            dist = ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)**0.5
            distances.append((dist, i, j))
    
    ds = DisjointSet(num_boxes)

    heapq.heapify(distances)
    while True:
        _, i, j = heapq.heappop(distances)
        circuit_size = ds.union(i, j)
        if circuit_size == num_boxes:
            return boxes[i][0] * boxes[j][0]

print(part1("input.txt"))
print(part2("input.txt"))