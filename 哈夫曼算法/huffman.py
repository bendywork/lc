import heapq
from collections import Counter


class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

    def is_leaf(self):
        return self.left is None and self.right is None


class HuffmanCodec:
    def __init__(self):
        self.codes = {}
        self.tree = None

    def build_tree(self, text):
        if not text:
            return None
        freq = Counter(text)
        heap = [HuffmanNode(char=c, freq=f) for c, f in freq.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
            heapq.heappush(heap, merged)

        self.tree = heap[0] if heap else None
        self.codes = {}
        if self.tree:
            self._build_codes(self.tree, "")
        return self.tree

    def _build_codes(self, node, code):
        if node.is_leaf():
            self.codes[node.char] = code if code else "0"
            return
        self._build_codes(node.left, code + "0")
        self._build_codes(node.right, code + "1")

    def encode(self, text):
        if not self.tree:
            self.build_tree(text)
        return "".join(self.codes[c] for c in text)

    def decode(self, encoded):
        if not self.tree:
            return ""
        result = []
        node = self.tree
        for bit in encoded:
            node = node.left if bit == "0" else node.right
            if node.is_leaf():
                result.append(node.char)
                node = self.tree
        return "".join(result)

    def get_stats(self, text):
        original_bits = len(text) * 8
        encoded = self.encode(text)
        encoded_bits = len(encoded)
        compression_ratio = (1 - encoded_bits / original_bits) * 100 if original_bits else 0
        return {
            "original_bits": original_bits,
            "encoded_bits": encoded_bits,
            "compression_ratio": round(compression_ratio, 2),
            "codes": dict(sorted(self.codes.items(), key=lambda x: len(x[1]))),
        }


if __name__ == "__main__":
    text = "abbcccddddeeeee"
    codec = HuffmanCodec()
    tree = codec.build_tree(text)

    print("字符编码表:")
    for char, code in sorted(codec.codes.items()):
        print(f"  '{char}': {code}")

    encoded = codec.encode(text)
    print(f"\n原文: {text}")
    print(f"编码: {encoded}")

    decoded = codec.decode(encoded)
    print(f"解码: {decoded}")
    print(f"验证: {'通过' if decoded == text else '失败'}")

    stats = codec.get_stats(text)
    print(f"\n压缩统计:")
    print(f"  原始大小: {stats['original_bits']} bits")
    print(f"  编码大小: {stats['encoded_bits']} bits")
    print(f"  压缩率: {stats['compression_ratio']}%")
