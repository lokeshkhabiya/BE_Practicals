# 2. Write a program to implement Huffman Encoding using a greedy strategy.

import heapq
# Node structure for Huffman Tree
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    # Defining less than operator for priority queue comparison
    def __lt__(self, other):
        return self.freq < other.freq
# Function to generate Huffman codes
def generate_codes(root, current_code, codes):
    if root is None:
        return
    if root.char is not None:
        codes[root.char] = current_code
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)
# Function to build Huffman Tree
def build_huffman_tree(frequency):
    heap = []
    # Insert all characters with their frequencies into the heap
    for char, freq in frequency.items():
        heapq.heappush(heap, HuffmanNode(char, freq))
    # Merge nodes until we have one tree
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        # Create a new internal node with the combined frequency
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    # The root of the Huffman Tree
    return heapq.heappop(heap)
# Function to calculate frequency of characters
def calculate_frequency(data):
    frequency = {}

    for char in data:
        if char not in frequency:
            frequency[char] = 0
        frequency[char] += 1
    return frequency
# Huffman Encoding process
def huffman_encoding(data):
    frequency = calculate_frequency(data)
    huffman_tree_root = build_huffman_tree(frequency)
    codes = {}
    generate_codes(huffman_tree_root, "", codes)
    # Encode the input data
    encoded_data = "".join([codes[char] for char in data])
    return encoded_data, huffman_tree_root
# Huffman Decoding process
def huffman_decoding(encoded_data, huffman_tree_root):
    decoded_data = ""
    current_node = huffman_tree_root
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.left is None and current_node.right is None:
            decoded_data += current_node.char
            current_node = huffman_tree_root
    return decoded_data
# Driver code
if __name__ == "__main__":
    data = "huffman encoding example"
    encoded_data, huffman_tree_root = huffman_encoding(data)
    print(f"Encoded Data: {encoded_data}")
    decoded_data = huffman_decoding(encoded_data, huffman_tree_root)
    print(f"Decoded Data: {decoded_data}")