# Prufer-s-Decoding-Algorithm
Python Implementation Of Prufer's Decoding Algorithm

Prufer's Decoding Algorithm is used to take in a sequence of vertices that are used to reconstruct a tree that the sequence is supposed to represent. 

The algorithm works as follows:
-A degree list that starts with 1 for every vertex. The degree list size equals to the size of the vertex plus 2.
-Go through the sequence and add 1 to the index that the vertex in the sequence corresponds to.
  EX. Vertex in the sequence is 4 so add 1 to the degree list at index 4.
-Once after going through the sequence and adding up all the degrees for each vertex, find the index where you find the first 1 in the degree list. Pair the index with the first vertex in the sequence and subtract the degree count that corresponds to the index and the first vertex. This pairing results in the first edge in the tree.
-Repeat the previous step with the next vertex in the sequence. Keep going until the whole sequence has been exhausted. These will result in the rest of the edges of the trees.
-After that, there will only be two indexes in the degree list with the value of 1. The pairing of these two will result in the final edge in the tree and the algorithm is done.


How to run the program:
1. Open the program into an environment that can execute python code and run it with the command: python PrufersDecodingAlgorithm.py
2. Enter the size of the sequence that the algorithm will work on.
3. One by one, enter the vertices (which is represented as a number) in the sequence.

After entering the final vertex in the sequence into the program, the script will run and it will return a list of lists where each sublist represents one edge between two vertices. All edges together makes the tree the sequence represents.
