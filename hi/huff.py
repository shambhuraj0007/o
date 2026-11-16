
# Import required libraries
import heapq
from collections import Counter

# Create a Node class for the Huffman tree
class Node:
    def __init__(self, char, freq):
        self.char = char       # Store character
        self.freq = freq       # Store frequency
        self.left = None       # Left child
        self.right = None      # Right child

    # Compare nodes based on frequency
    def __lt__(self, other):
        return self.freq < other.freq


# Function to generate Huffman codes
def huffman_encoding(text):

    # Count frequency of each character
    frequency = Counter(text)

    # Create an empty priority queue
    heap = []

    # Insert characters into the heap
    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    # Combine nodes until one node remains
    while len(heap) > 1:

        # Remove two nodes with minimum frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Create a new internal node
        new_node = Node(None, left.freq + right.freq)

        # Connect left and right children
        new_node.left = left
        new_node.right = right

        # Insert the new node into the heap
        heapq.heappush(heap, new_node)

    # The remaining node is the root
    root = heap[0]

    # Dictionary to store Huffman codes
    codes = {}

    # Function to generate binary codes
    def generate_codes(node, code):

        # Check if node is a leaf node
        if node.char is not None:
            codes[node.char] = code or "0"
            return

        # Left side represents 0
        generate_codes(node.left, code + "0")

        # Right side represents 1
        generate_codes(node.right, code + "1")

    # Start generating codes from root
    generate_codes(root, "")

    # Return the generated codes
    return codes


# Accept input from the user
text = input("Enter a string: ")

# Check for empty input
if not text:
    print("Please enter a non-empty string.")

else:
    # Call Huffman encoding function
    codes = huffman_encoding(text)

    # Display Huffman codes
    print("Huffman Codes:")

    for char, code in sorted(codes.items()):
        print(char, ":", code)
