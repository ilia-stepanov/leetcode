class RBNode:
    def __init__(self, key, value):
        self.key = key
        self.values = [value]
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'RED'  # New nodes are red by default


class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None, None)
        self.NIL.color = 'BLACK'
        self.root = self.NIL

    def insert(self, key, value):
        new_node = RBNode(key, value)
        new_node.left = new_node.right = new_node.parent = self.NIL

        parent = None
        curr = self.root

        while curr != self.NIL:
            parent = curr
            if new_node.key < curr.key:
                curr = curr.left
            elif new_node.key > curr.key:
                curr = curr.right
            else:
                curr.values.append(value)
                return  # Key exists, append value

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'RED'
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'RED':
                    node.parent.color = uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'RED':
                    node.parent.color = uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.left_rotate(node.parent.parent)
        self.root.color = 'BLACK'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def reverse_inorder(self, node, result):
        if node == self.NIL:
            return
        self.reverse_inorder(node.right, result)
        result.append((node.key, node.values))
        self.reverse_inorder(node.left, result)

class FrequencyRBMap:
    def __init__(self):
        self.tree = RedBlackTree()

    def insert(self, freq, num):
        self.tree.insert(freq, num)

    def get_descending(self):
        result = []
        self.tree.reverse_inorder(self.tree.root, result)
        return result


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.values = []  # Store associated values (e.g., nums with this frequency)
        self.left = None
        self.right = None
        self.height = 1  # New nodes are initially added at height 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key, value):
        # 1. Perform normal BST insert
        if not root:
            node = AVLNode(key)
            node.values.append(value)
            return node

        if key < root.key:
            root.left = self.insert(root.left, key, value)
        elif key > root.key:
            root.right = self.insert(root.right, key, value)
        else:
            # Equal key, append value
            root.values.append(value)
            return root

        # 2. Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Get balance factor
        balance = self.get_balance(root)

        # 4. Balance the tree
        # Case 1: Left Left
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Case 2: Right Right
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Case 3: Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4: Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def reverse_inorder(self, node, result):
        if not node:
            return
        self.reverse_inorder(node.right, result)
        result.append((node.key, node.values))
        self.reverse_inorder(node.left, result)


# Expose as a class with AVL insert and reverse traversal
class FrequencyAVLMap:
    def __init__(self):
        self.tree = AVLTree()
        self.root = None

    def insert(self, freq, num):
        self.root = self.tree.insert(self.root, freq, num)

    def get_descending(self):
        result = []
        self.tree.reverse_inorder(self.root, result)
        return result


class TreeNode:
    def __init__(self, key):
        self.key = key            # frequency
        self.values = []          # list of nums with this frequency
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        def _insert(node, key, value):
            if not node:
                new_node = TreeNode(key)
                new_node.values.append(value)
                return new_node
            if key < node.key:
                node.left = _insert(node.left, key, value)
            elif key > node.key:
                node.right = _insert(node.right, key, value)
            else:
                node.values.append(value)
            return node

        self.root = _insert(self.root, key, value)

    def reverse_inorder(self):
        result = []
        def _traverse(node):
            if not node:
                return
            _traverse(node.right)
            result.append((node.key, node.values))
            _traverse(node.left)
        _traverse(self.root)
        return result  # sorted by key descending


class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, value):
        self.heap.append(value)
        self._sift_up()

    def _swap(self, new_position, old_position):
        self.heap[old_position], self.heap[new_position] = self.heap[new_position], self.heap[old_position]



    def pop(self):
        if not self.heap:
            return None
        self._swap(0, self.size() - 1)
        item = self.heap.pop()
        self._sift_down()
        return item

    def _sift_up(self):
        added_value_index = len(self.heap) - 1
        added_value = self.heap[added_value_index][0]
        
        while True:
            parent_index = (added_value_index - 1) // 2
            parent_value = self.heap[parent_index][0]
            if added_value >= parent_value or added_value_index == 0:
                break
            self._swap(parent_index, added_value_index)
            added_value_index = parent_index


    def _sift_down(self):
        parent = 0
        size = self.size()
        while True:
            left_child = 2 * parent + 1
            right_child = 2 * parent + 2
            smallest = parent

            if left_child < size and self.heap[left_child][0] < self.heap[smallest][0]:
                smallest = left_child
            if right_child < size and self.heap[right_child][0] < self.heap[smallest][0]:
                smallest = right_child

            if smallest == parent:
                break

            self._swap(parent, smallest)
            parent = smallest
    

    def size(self):
        return len(self.heap)

    def to_list(self):
        return [item[1] for item in self.heap]


class Solution:
    def topKFrequentUsingMinHeap(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies manually
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Step 2: Use custom MinHeap to keep top k
        heap = MinHeap()
        for num, freq in freq_map.items():
            heap.push((freq, num))
            if heap.size() > k:
                heap.pop()

        # Step 3: Extract result
        return heap.to_list()
    

    def topKFrequentUsingBucketSort(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for (val, freq) in freq_map.items():
            buckets[freq].append(val)
        i = len(nums)
        result = []
        while k > 0:
            if buckets[i]:
                k -= len(buckets[i])
                result.extend(buckets[i])
            i -= 1
        return result


    def quickSelectSort(self, ls, left, right, k):
        if left >= right:
            return

        pivot_value = ls[right][1]
        pivot_index = right
        store_index = left

        for i in range(left, right):
            if pivot_value > ls[i][1]:
                ls[store_index], ls[i] = ls[i], ls[store_index]
                store_index += 1
        ls[store_index], ls[pivot_index] = ls[pivot_index], ls[store_index]
        

        if k == store_index:
            return
        elif k > store_index:
            self.quickSelectSort(ls, store_index + 1, right, k)
        elif k < store_index:
            self.quickSelectSort(ls, left, store_index - 1, k)


    def topKFrequentUsingQuickSelectSort(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        ls = list(freq_map.items())
        self.quickSelectSort(ls, 0, len(ls) - 1, len(ls) - k)
        return [item[0] for item in ls[-k:]]
        

    def topKFrequentSortByFrequency(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        ls = list(freq_map.items())
        ls.sort(key=lambda x: x[1])
        result = []
        for i in range(1, k+1):
            result.append(ls[-i][0])
        return result

    def topKFrequentUsingUnbalancedTreeMap(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Step 2: Insert into custom TreeMap
        tree = TreeMap()
        for num, freq in freq_map.items():
            tree.insert(freq, num)

        # Step 3: Traverse in descending frequency order and collect top k
        result = []
        for freq, values in tree.reverse_inorder():
            result.extend(values)
            if len(result) >= k:
                return result[:k]


    def topKFrequentUsingAVLTreeMap(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Insert into AVL Tree
        tree_map = FrequencyAVLMap()
        for num, freq in freq_map.items():
            tree_map.insert(freq, num)

        # Get top k frequent elements
        result = []
        for freq, values in tree_map.get_descending():
            result.extend(values)
            if len(result) >= k:
                break

        return result[:k]


    def topKFrequentUsingRedBlackTreeMap(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Frequency count
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Step 2: Insert into Red-Black Tree
        rb_map = FrequencyRBMap()
        for num, freq in freq_map.items():
            rb_map.insert(freq, num)

        # Step 3: Collect top K frequent elements (in descending order)
        result = []
        for freq, values in rb_map.get_descending():
            result.extend(values)
            if len(result) >= k:
                break

        return result[:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.topKFrequentUsingRedBlackTreeMap(nums, k)

