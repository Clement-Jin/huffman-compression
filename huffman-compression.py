# HUFFMAN CODING DEMO

import math, os

class Character:

    @staticmethod
    def generate_characters(string, mono_case=True):
        """generates a list of Character objects for a given string
        if `mono_case` is True, all characters will be converted to lowercase."""
        
        if mono_case:
            string = string.lower()
    
        chars = set(string)
        character_nodes = []

        for char in chars:
            char_freq = string.count(char) 
            new_node = Character(char, char_freq)
            character_nodes.append(new_node)

        return sorted(character_nodes, key=lambda x: x.frequency, reverse=False) # in ascending order of frequency

    def __repr__(self):
        return f'`{self.letters}` : {self.frequency}'


    def __init__(self, letters, frequency):
        self.letters = letters
        self.frequency = frequency
        self.parent_node = None
    def set_parent_node(self, parent_node):
        self.parent_node = parent_node

class Node:

    def __repr__(self):
        return f'child letters: {self.letters} ----- combined frequency: {self.frequency}'

    def __init__(self, left_node, right_node):
        self.left_node = left_node
        self.right_node = right_node
        self.frequency = left_node.frequency + right_node.frequency
        self.letters = left_node.letters + right_node.letters # this is very important. It stores what letters are children under the current node. 

    @staticmethod

    def generate_huffman_dict(character_nodes, include_tree=False):

        character_values = {node.letters : '' for node in character_nodes}

        nodes = character_nodes

        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.frequency, reverse=False) # in ascending order of frequency
            left, right = nodes[0:2] # the 2 least frequent nodes 
            
            # building the ultimate path/binary value for each character. ie. if it's on the left side of a node, it will have a `0`, and vice versa.
            # These are backwards, so will need to be reversed
            for l_letter in left.letters:
                character_values[l_letter] += '0' # 0 is for the left

            for r_letter in right.letters:
                character_values[r_letter] += '1' # 1 is for right

            # replace left and right nodes with a new parent node encapsulating them both
            new_node = Node(left, right)
            nodes.append(new_node)
            del nodes[0:2] # delete those nodes from the list

        # the single node left in the list at the end of the loop is the final huffman tree
        if len(nodes) == 1:
            huffman_tree = nodes[0]
        else:
            raise ValueError(f'Tree Build Error: ended up with more than node, instead got {len(nodes)}')
        
        # reversing the path values of `character_values`
        reverse = lambda x : x[::-1] # reverses any string
        character_values = {key : reverse(value) for key, value in character_values.items()} # reversing the values of all binary paths

        # returning values based on the `include_tree` parameter in the function
        if include_tree:
            return character_values, huffman_tree
        return character_values

    
    def compress(raw_string, mono_case=True):
        """if `mono_case` is True, all letters will be converted to lowercase"""

        if mono_case:
            raw_string = raw_string.lower()

        character_nodes = Character.generate_characters(raw_string)
        huffman_dict = Node.generate_huffman_dict(character_nodes)
        
        encoded = ''
        for char in raw_string:
            encoded += huffman_dict[char]
        
        print(f'normal file size: {len(raw_string)*7} bits (with normal 7-bit ascii)\ncompressed file size: {len(encoded)} bits\ncompressed size was {len(encoded)/(len(raw_string)*7) * 100}%')
        return encoded
                

if __name__ == '__main__':
    uncompressed = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nunc odio, cursus id consectetur id, condimentum at dui. Proin vel feugiat libero. Ut quis est augue."
    compressed = Node.compress(uncompressed)
    # print(compressed)