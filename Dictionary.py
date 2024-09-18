class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Dictionary:
    def __init__(self, size):
        self.table = [None] * 23
        self.size = size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % 23

    def insert(self, key, value):
        hash_value = self.hash_function(key)
        if self.table[hash_value] is None:
            self.table[hash_value] = Node(key, value)
        else:
            p = self.table[hash_value]
            while p is not None:
                if p.key == key:
                    p.value = value
                    return
                if p.next is None:
                    break
                p = p.next
            p.next = Node(key, value)

    def get(self, key):
        hash_value = self.hash_function(key)
        p = self.table[hash_value]
        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
        return None


vietnamese_to_english = Dictionary(23)

vietnamese_to_english.insert("xin chào", "hello")
vietnamese_to_english.insert("cảm ơn", "thank you")
vietnamese_to_english.insert("tạm biệt", "goodbye")
vietnamese_to_english.insert("yêu", "love")
vietnamese_to_english.insert("bạn", "friend")

print(vietnamese_to_english.get("xin chào"))
print(vietnamese_to_english.get("cảm ơn"))
print(vietnamese_to_english.get("tạm biệt"))
print(vietnamese_to_english.get("yêu"))
print(vietnamese_to_english.get("bạn"))

print(vietnamese_to_english.get("không tồn tại"))  # Expected output: None
