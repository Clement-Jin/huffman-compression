# huffman-compression
A demo of Huffman coding, realised in Python

Basic Algorithm:
1. Classes:
    i. An node object that has:
        a. Value of letter
        b. Frequency of letter
    ii. A Branch node object that has:
        a. 2 nodes stored as children in the branch node. These could be node objects described in 0.i, or other branch nodes.
        Make sure to identify which has the binary value 0 and which has the value 1, ie. the left/right sides of the tree branch.
            0. Use .left and .right perhaps? 
        b. The frequency of that node: the sum of frequencies of the child nodes. 
    
2. Count frequencies of each letter and add to a list. 
3. Perform the following loop:
    i. Take the 2 nodes of smallest frequency and make them a branch node.
    ii. Remove those 2 nodes, and add the new branch node to that list.
    iii. Repeat until only 1 Branch node remains, at which point break. 
4. The final branch node left in the list is the huffman tree. 

5. Make dictionary of binary values corresponding to each letter. 
    Mabye try writing this feature into the nodes themselves? 
