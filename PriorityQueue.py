# Cài đặt hàng đợi ưu tiên bằng cấu trúc dữ liệu đống
class PriorityQueue:
    def __init__(self):
        self.items = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return (2 * i) + 1

    def _right_child(self, i):
        return (2 * i) + 2

    def _swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def _heapify_up(self, i):
        parent_i = self._parent(i)
        while i > 0 and self.items[i] > self.items[parent_i]:
            self._swap(i, parent_i)
            i = parent_i

    def _heapify_down(self, i):
        left_child = self._left_child(i)
        right_child = self._right_child(i)
        largest = i
        if left_child < len(self.items) and self.items[left_child] > self.items[largest]:
            largest = left_child
        if right_child < len(self.items) and self.items[right_child] > self.items[largest]:
            largest = right_child

        if largest != i:
            self._swap(i, largest)
            self._heapify_down(largest)

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, val):
        self.items.append(val)
        self._heapify_up(len(self.items) - 1)

    def pop(self):
        max_val = self.items.pop(0)
        self._heapify_down(0)
        return max_val

    def peek(self):
        return self.items[0]


pq = PriorityQueue()
pq.insert(12)
pq.insert(70)
pq.insert(20)
pq.insert(25)
pq.insert(1)
pq.insert(6)
pq.insert(30)

print(f"Phần tử lớn nhất: {pq.peek()}")

while not pq.is_empty():
    print(pq.pop())
