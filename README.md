# DSA Python Implementations

Data structures implemented from scratch in Python for SWE interview prep. Each file has one class plus tests at the bottom.

**Progress: 5/45 implemented**

## Run a file's tests

```bash
python 01_linear/stack.py
```

A passing run prints `<Class>: all tests passed`.

## 01_linear

- [x] `01_linear/dynamic_array.py` - DynamicArray: Resizable array (amortized O(1) append). Use a fixed-size backing list; double capacity when full.
- [ ] `01_linear/singly_linked_list.py` - SinglyLinkedList: Singly linked list with head pointer (add tail for O(1) append).
- [x] `01_linear/doubly_linked_list.py` - DoublyLinkedList: Doubly linked list with sentinel head/tail. Basis for LRU, deque, browser history.
- [x] `01_linear/stack.py` - Stack: LIFO stack (backed by dynamic array or linked list).
- [ ] `01_linear/queue.py` - Queue: FIFO queue (linked list or two-stack implementation).
- [x] `01_linear/deque.py` - Deque: Double-ended queue (doubly linked list or circular array).
- [x] `01_linear/circular_queue.py` - CircularQueue: Fixed-capacity ring buffer with head/tail indices.
- [ ] `01_linear/min_max_stack.py` - MinStack: Stack with O(1) get_min (and variant get_max).
- [ ] `01_linear/monotonic_stack.py` - MonotonicStack: Stack that keeps elements monotonic. Use for next greater element, histogram.
- [ ] `01_linear/monotonic_queue.py` - MonotonicQueue: Deque kept monotonic. Use for sliding window maximum.

## 02_hashing

- [ ] `02_hashing/hash_map.py` - HashMap: Hash table with chaining (then try open addressing). Implement resizing on load factor.
- [ ] `02_hashing/hash_set.py` - HashSet: Set built on your HashMap.
- [ ] `02_hashing/bloom_filter.py` - BloomFilter: Probabilistic membership: false positives possible, no false negatives.
- [ ] `02_hashing/bitset.py` - Bitset: Compact set of ints stored in bits (use int or bytearray).
- [ ] `02_hashing/lru_cache.py` - LRUCache: HashMap + DoublyLinkedList. O(1) get/put.
- [ ] `02_hashing/lfu_cache.py` - LFUCache: HashMap + frequency -> ordered list buckets. O(1) get/put.

## 03_trees

- [ ] `03_trees/binary_tree.py` - BinaryTree: Binary tree node + traversals.
- [ ] `03_trees/bst.py` - BST: Binary search tree.
- [ ] `03_trees/avl_tree.py` - AVLTree: Self-balancing BST via height balance factor and rotations.
- [ ] `03_trees/red_black_tree.py` - RedBlackTree: Self-balancing BST via node colors.
- [ ] `03_trees/treap.py` - Treap: BST by key + heap by random priority.
- [ ] `03_trees/ordered_map.py` - OrderedMap: Sorted key-value map on top of a balanced BST.
- [ ] `03_trees/b_tree.py` - BTree: B-Tree of minimum degree t (database indexing). Later try B+ tree.
- [ ] `03_trees/skip_list.py` - SkipList: Probabilistic layered linked list, O(log n) expected.
- [ ] `03_trees/interval_tree.py` - IntervalTree: Augmented BST storing max endpoint; finds overlapping intervals.
- [ ] `03_trees/merkle_tree.py` - MerkleTree: Hash tree for data integrity; supports proofs.
- [ ] `03_trees/persistent_structures.py` - PersistentList: Versioned immutable structure via path copying (e.g. persistent stack/BST).

## 04_heaps

- [ ] `04_heaps/heap.py` - MinHeap: Binary heap in an array. Parametrize for max-heap / key function.
- [ ] `04_heaps/priority_queue.py` - PriorityQueue: Priority queue on your heap, with decrease_key support (for Dijkstra).
- [ ] `04_heaps/fibonacci_heap.py` - FibonacciHeap: Amortized O(1) insert/decrease-key. Advanced.

## 05_strings

- [ ] `05_strings/trie.py` - Trie: Prefix tree.
- [ ] `05_strings/radix_tree.py` - RadixTree: Compressed trie (Patricia): edges hold strings.
- [ ] `05_strings/suffix_array.py` - SuffixArray: Sorted suffix indices + LCP array (Kasai).
- [ ] `05_strings/suffix_tree.py` - SuffixTree: Suffix tree (Ukkonen, or naive first).
- [ ] `05_strings/inverted_index.py` - InvertedIndex: term -> postings list for document retrieval.

## 06_range_queries

- [ ] `06_range_queries/segment_tree.py` - SegmentTree: Range sum/min queries with point + range updates (lazy propagation).
- [ ] `06_range_queries/fenwick_tree.py` - FenwickTree: Binary indexed tree: prefix sums with updates.
- [ ] `06_range_queries/sparse_table.py` - SparseTable: Static range min/max in O(1) after O(n log n) build.

## 07_graphs

- [ ] `07_graphs/graph_adjacency_list.py` - GraphList: Graph via adjacency list (directed/undirected, weighted).
- [ ] `07_graphs/graph_adjacency_matrix.py` - GraphMatrix: Graph via adjacency matrix (dense graphs).
- [ ] `07_graphs/union_find.py` - UnionFind: Disjoint set union with path compression + union by rank.
- [ ] `07_graphs/dag.py` - DAG: Directed acyclic graph with cycle detection and topological sort.

## 08_spatial

- [ ] `08_spatial/quadtree.py` - QuadTree: 2D spatial partition.
- [ ] `08_spatial/kd_tree.py` - KDTree: k-d tree for nearest neighbor search.
- [ ] `08_spatial/r_tree.py` - RTree: Bounding-rectangle tree for geospatial data.

## No file needed (use Python built-ins)
Arrays/lists, strings, matrices/2D arrays: practice these via problems (two pointers, sliding window, grid DFS/BFS), not custom classes.
