# MultimediaDBMS

Multimedia DBMS team project. Aimed to find a bird sound file in a database which is the most similar to the inputted one, using simplest audio analysis approach.

## Backend quick documentation

### Data

Basically another coat for the original WaveFile class (see wavefile.py).
It contains metadata about dimension count and offers some auxiliary methods useful for the KD-Tree implementation.

Attributes:

- dimension: Number of dimensions of the feature vector.
- content: The corresponding feature vector.
- location: The file's directory (see wavefile.py).
  
Methods:

- get_key(self, layer_id: int) -> List: Return a key as form of a list with self.dimension elements, useful for sorting the vector by a certain priority order.

### compareData(data1: Data, data2: Data, layer_id: int) -> int

Compare 2 Data objects (as comparing their feature vectors).
The priority order is determined by layer_id - to be specific: starts with layer_id, then (layer_id + 1) % dimension, (layer_id + 2) % dimension, and so on.
Return -1, 0 or 1 according to the comparison's result.

### distance(data1: Data, data2: Data, metric: int = 2) -> float

Calculate the distance between the feature vectors of 2 Data objects.
Default metrics used is L-2 (Euclidean distance).

### distance_to_slice(data: Data, cut_layer: tuple(int, float), metric: int= 2) -> float

Calculate the distance between a point (described by the imported Data's feature vector) and a hyperplane described by cut_layer as of following: (cut_dimension, cut_coordinate).
Default metrics used is L-2 (Euclidean distance).

### KDNode

A node containing a Data object.

Attributes:

- data: Data object associated with the node.
- left: Left children, None if not existed.
- right: Right children, None if not existed.
- cut_layer: Hyperplane that defines the split of the data, useful for the KD-Tree.

### KDTree

A k-dimensional binary search tree. The implementing representation is basically a KDNode acting as the root.

Attributes:

- dimension: Number of dimensions of the feature vectors. In other words, the constant "k".
- root: KDNode root node.

Methods:

- build_tree(self, data_list: List[Data], layer_id: int = 0) -> KDNode: Create the tree with the given list of Data objects. This should have the same dimension for all elements.
- search(self, data: WaveFile, tolerance: float = 0.0) -> Data, float: Return the nearest Data in the KD-tree, and the corresponding shortest distance. Here, "tolerance" argument is used to switch the function into approximate nearest search, by ignoring the opposite side if the distance to the cut layer is at least equal to (1 - tolerance) of the current best.
- k_search(self, data: WaveFile, k: int = 5, tolerance: float = 0.0) -> List[Data, float]: Return k nearest Data(s) in the KD-tree. Similar to the above function. "tolerance" argument here acts as opposite denial when the distance to the cut-layer is at least equal to (1 - tolerance) of the current k-th nearest.
