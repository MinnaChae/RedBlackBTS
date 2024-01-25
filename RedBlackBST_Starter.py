"""
Minna Chae
TCSS 503
HW1: RedBlackBST
"""


class RedBlackBST:
    """ A Python Implementation of a Red-Black Binary Search Tree
    """
    class RedBlackNode:
        """Basic node representing the Key/Value and color of a link/node.
        """
        def __init__(self, key, value):
            """Returns a newly created `RedBlackNode` initiated to be a "Red" link.
            :param key: The unique, comparable object by which to retrieve the desired value.
            :param value: The value in which to store in the `RedBlackBST` object.
            """
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.parent = None
            self.is_red = True  # NEW NODES ARE ALWAYS RED IN THIS IMPLEMENTATION TO DEFAULT THEM TO BE SO.

        def __str__(self):
            """Returns a string representation of a node, including the ids and colors of its left and right links.
            The pattern used is: `(left.key)<-[Red|Black]--(node.key)--[Red|Black]->(right.key)
            If either left or right nodes are blank, the key is `None` and the link color defaults to `Black`.

            :return: String representation of the desired node.
            """
            l_node = "None" if self.left is None else self.left.key
            l_link = "Black" if self.left is None or not self.left.is_red else " Red "
            r_node = "None" if self.right is None else self.right.key
            r_link = "Black" if self.right is None or not self.right.is_red else " Red "
            p_node = "None" if self.parent is None else self.parent.key
            p_link = " Red " if self.is_red else "Black"
            return f"({l_node})<--[{l_link}]--({self.key})--[{r_link}]-->({r_node}) [Parent: ({p_node})]"
            # return f"({l_node})<--[{l_link}]--({self.key})--[{r_link}]-->({r_node})"

    def __init__(self):
        """Creates an empty `RedBlackBST` (Red-Black Binary Search Tree)
        """
        self.root = None

### THE FOLLOWING THREE METHOD STUBS REQUIRE COMPLETION FOR ASSIGNMENT

    def insert_i(self, key, value):
        """Inserts the proper value using an iterative method of traversal.
        Assumes the key provided is a comparable object, and assumes uniqueness.  If the `Key` already exists in the
        structure, the provided value will overwrite the previous value for this key.
        :param key: The unique, comparable object by which to retrieve the desired value.
        :param value: The value in which to store in the `RedBlackBST`
        :return: `None`
        """

        insert_node = RedBlackBST.RedBlackNode(key, value)

        # SPECIAL CASE ROOT IS EMPTY.
        if self.root is None:
            self.root = insert_node
            self.root.is_red = False
            return

        # FIND WHERE TO INSERT (TRAVERSING LEFT AND RIGHT) - bubble down
        curr = self.root
        while curr:
            if insert_node.key < curr.key:
                if curr.left is None:
                    curr.left = insert_node
                    insert_node.parent = curr
                curr = curr.left
            elif insert_node.key > curr.key:
                if curr.right is None:
                    curr.right = insert_node
                    insert_node.parent = curr
                curr = curr.right
            else:
                curr.value = value
                break

        # ONCE INSERTED, TRAVERSE UP CURR.PARENT - bubble up
            #Rotate Node
        temp = curr

        while temp:
            parent_node = temp.parent
            if self._right_is_red(temp) and not self._left_is_red(temp):
                if parent_node is None:
                    temp = self._rotate_left_i(temp)
                    self.root = temp
                elif parent_node.left == temp:
                    temp = self._rotate_left_i(temp)
                    parent_node.left = temp
                else:
                    temp = self._rotate_left_i(temp)
                    parent_node.right = temp
            if self._left_left_is_red(temp):
                if temp.parent is None:
                    temp = self._rotate_right_i(temp)
                    self.root = temp
                elif parent_node.left == temp:
                    temp = self._rotate_right_i(temp)
                    parent_node.left = temp
                else:
                    temp = self._rotate_right_i(temp)
                    parent_node.right = temp
            if self._left_is_red(temp) and self._right_is_red(temp):
                self._flip_colors(temp)
            if self.root == temp:
                break
            temp = temp.parent
        self.root.is_red = False

    def _rotate_left_i(self, node):
        """Perform a `rotation_left` around the node provided.  Return the new root of newly rotated local cluster.
        :param node: The node around which to rotate.
        :return: The new root that exists as a result of the rotation.
        """
        #node is curr.parent
        x = node.right
        #changing pointers
        node.right = x.left
        if x.left is not None:
            x.left.parent = node
        x.left = node
        x.parent = node.parent
        node.parent = x
        x.is_red = node.is_red
        node.is_red = True

        return x

    def _rotate_right_i(self, node):
        """Perform a `rotation_right` around the node provided.  Return the new root of newly rotated local cluster.
        :param node: The node around which to rotate.
        :return: The new root that exists as a result of the rotation.
        """

        x = node.left

        node.left = x.right
        if x.right is not None:
            x.right.parent = node
        x.right = node
        x.parent = node.parent
        node.parent = x
        x.is_red = node.is_red
        node.is_red = True

        return x

########### THE BELOW METHODS ARE FOR STUDENT USE AND CAN BE USED AS IS IN THE INTERATIVE IMPLEMENTATION

    def _flip_colors(self, node):
        """Using the provided `node`, set both child linacks to black, and set the parent link to `Red`.
        :param node: The node for which the child colors and parent link should have their colors flipped.
        :return: None
        """
        node.is_red = True
        node.left.is_red = False
        node.right.is_red = False

    def _right_is_red(self, node):
        """Indicates whether the link to the right of the provided node is currently Red.
        :param node: The node of which the right link is viewed for redness.
        :return: `True` if `node.right` is red, `False` otherwise.
        """
        if node.right is None:
            return False
        else:
            return node.right.is_red

    def _left_is_red(self, node):
        """Indicates whether the link to the left of the provided node is currently Red.
        :param node: The node of which the left link is viewed for redness.
        :return: `True` if `node.left` is red, `False` otherwise.
        """
        if node.left is None:
            return False
        else:
            return node.left.is_red

    def _left_left_is_red(self, node):
        """Indicates whether there exists to consecutive left red links from the given node.
        :param node: The node from which to interrogate the left and left.left nodes for redness.
        :return: `True` if `node.left` is red and 'node.left.left` is red.  `False` otherwise.
        """
        if node is None:
            return False
        else:
            return self._left_is_red(node) and self._left_is_red(node.left)

    def search(self, key):
        """Search for the desired Key.
        Uses binary search to locate and return the Value at the provided Key.  If the Key is not found, `search` will
        return `None`, otherwise will return the Value stored at the key provided.
        :param key: The unique key by which to retrieve the desired value.  Must be comparable.
        :return: The Value at the Key provided, if the Key is not found, `search` will return `None`
        """
        n = self._node_search(key)
        return n.value if n is not None else None

    def _node_search(self, key):
        """ Searches for the desired key and returns the `RedBlackNode` associated to that key.

        :param key: The unique key by which to retrieve the desired value.  Must be comparable.
        :return: The `RedBlackNode` at the Key provided, if the Key is not found, `_node_search` will return `None`
        """
        curr = self.root

        while True:
            if curr is None:
                return None
            elif curr.key == key:
                return curr
            elif curr.key > key:
                curr = curr.left
            else:
                curr = curr.right


########### THE BELOW SECTION IS ONLY FOR REFERENCE AS A FUNCTIONING RECURSIVE IMPLEMENTATION

    def insert_r(self, key, value):
        """Insert the provided `value` at the provided `key` in the `RedBlackBST` using a recursive method `_put()`.
        Assumes the key provided is a comparable object, and assumes uniqueness.  If the `Key` already exists in the
        structure, the provided value will overwrite the previous value for this key.

        :param key: The unique, comparable object by which to retrieve the desired value.
        :param value: The value in which to store in the `RedBlackBST`
        :return: `None`
        """

        self.root = self._put_r(self.root, key, value)
        self.root.is_red = False

    def _put_r(self, node, key, value):
        """A recursive call to insert a new value into the structure using the standard Red-Black insertion rules.
        Base Case: The Node provided is None, in which case, create a new `RedBlackNode` and return.
        Recursive Case: If the insertion key is equal to node.key. replace the value and return (special case).  If the
        insertion key is less than node.key, recursively _put into node.left, otherwise recursively _put into node.right

        After the base case if found, recursively check for necessary rotations and color flips.

        :param node: The `RedBlackNode` into which a _put is attempted.
        :param key: The desired key to insert into the `RedBlackBST`
        :param value: The desired value to store at the provided `key`.
        :return: Returns the parent node from the level of recursion that has been executed.
        """
        if node is None:
            return RedBlackBST.RedBlackNode(key, value)

        if key < node.key:
            node.left = self._put_r(node.left, key, value)
        elif key > node.key:
            node.right = self._put_r(node.right, key, value)
        else:
            node.value = value

        if self._right_is_red(node) and not self._left_is_red(node):
            node = self._rotate_left_r(node)
        if self._left_left_is_red(node):
            node = self._rotate_right_r(node)
        if self._left_is_red(node) and self._right_is_red(node):
            self._flip_colors(node)

        return node

    def _rotate_left_r(self, node):
        """Perform a `rotation_left` around the node provided.  Return the new root of newly rotated local cluster.
        :param node: The node around which to rotate.  Does NOT manage parent links and cannot be used for iterative
        insertion method
        :return: The new root that exists as a result of the rotation.
        """
        x = node.right
        node.right = x.left
        x.left = node
        x.is_red = node.is_red
        node.is_red = True
        return x

    def _rotate_right_r(self, node):
        """Perform a `rotation_right` around the node provided.  Return the new root of newly rotated local cluster.
        :param node: The node around which to rotate.
        :return: The new root that exists as a result of the rotation.
        """
        x = node.left
        node.left = x.right
        x.right = node
        x.is_red = node.is_red
        node.is_red = True
        return x

    def pre_order_recursive(self, node, result=None):
        if result is None:
            result = []
        if node is not None:
            result.append(node)
            self.pre_order_recursive(node.left, result)
            self.pre_order_recursive(node.right, result)
        return result

    def in_order_recursive(self, node, result=None):
        if result is None:
            result = []
        if node is not None:
            self.in_order_recursive(node.left, result)
            result.append(node)
            self.in_order_recursive(node.right, result)
        return result

########### END RECURSIVE SECTION


def test_bst(bst):
    bst.insert_i(1, 'one')
    r = bst.search(1)

    result = "PASSED" if r == 'one' else f"FAILED, expected 'one', received {r}"
    print(f"Test Inserting Single Value...{result}")

    tests = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in tests:
        try:
            bst.insert_i(i, i)
            print(f"Insertion of {i} passed (no exception thrown).")
        except Exception as e:
            print(f"Insertion of {i} failed. Exception thrown: {e}")
    for i in tests:
        try:
            r = bst.search(i)
            result = "PASSED" if r == i else f"FAILED, expected {i}, received {r}"
            print(f"Search for {i}: {result}")
        except Exception as e:
            print(f"Search for {i} failed. Exception thrown: {e}")

    bst.insert_i(100, 'one-hundred')
    bst.insert_i(100, 'one hundred')
    r = bst.search(100)
    result = "PASSED" if r == 'one hundred' else f"Failed, expected 'one hundred', received {r}"
    print(f"Test repeat Keys: {result}")

def test_bst_2(my_bst, recur_bst, kvs_to_insert):
    for kv in kvs_to_insert:
        key, value = kv
        recur_bst.insert_r(key, value)

    for kv in kvs_to_insert:
        key, value = kv
        my_bst.insert_i(key, value)

    tree_recur = recur_bst.pre_order_recursive(recur_bst.root)
    tree_my = my_bst.pre_order_recursive(my_bst.root)
    different = ""
    different_count = 0
    same = ""
    same_count = 0
    total = 0
    print("Printing Test")
    for i in range(len(tree_recur)):
        total +=1
        # testing key
        if tree_recur[i].key == tree_my[i].key:
            # print(f"Key Same: Expected {tree_recur[i].key} and got {tree_my[i].key}")
            same += f"Key Same: Expected {tree_recur[i].key} and got {tree_my[i].key}"
            same_count += 1
        else:
            # print(f"Key Different: Expected {tree_recur[i].key} but got {tree_my[i].key}")
            different += f"Key Different: Expected {tree_recur[i].key} but got {tree_my[i].key}"
            different_count +=1

        # testing value
        if tree_recur[i].value == tree_my[i].value:
            # print(f"Value Same: Expected {tree_recur[i].value} and got {tree_my[i].value}")
            same += f" | Value Same: Expected {tree_recur[i].value} and got {tree_my[i].value}"
            same_count += 1
        else:
            # print(f" | Value Different: Expected {tree_recur[i].value} but got {tree_my[i].value}")
            different += f" | Value Different: Expected {tree_recur[i].value} but got {tree_my[i].value}"
            different_count += 1
        # testing left and color
        if tree_recur[i].left:
            if tree_recur[i].left.is_red:
                recur_color = "red"
            else:
                recur_color = "black"
            if tree_my[i].left.is_red:
                my_color = "red"
            else:
                my_color = "black"

            if tree_recur[i].left.key == tree_my[i].left.key and tree_recur[i].left.is_red == tree_my[i].left.is_red:
                # print(f"Left Same: Expected {tree_recur[i].left.key} {recur_color} and got {tree_my[i].left.key} {my_color}")
                same += f" | Left Same: Expected {tree_recur[i].left.key} {recur_color} and got {tree_my[i].left.key} {my_color}"
                same_count += 1

            else:
                # print(f"Left Different: Expected {tree_recur[i].left.key} {recur_color} and got {tree_my[i].left.key} {my_color}")
                different += f" | Left Different: Expected {tree_recur[i].left.key} {recur_color} and got {tree_my[i].left.key} {my_color}"
                different_count += 1
            # testing right and color
        if tree_recur[i].right:
            if tree_recur[i].right.is_red:
                recur_color = "red"
            else:
                recur_color = "black"
            if tree_my[i].right.is_red:
                my_color = "red"
            else:
                my_color = "black"
            if tree_recur[i].right.key == tree_my[i].right.key and tree_recur[i].right.is_red == tree_my[
                i].right.is_red:
                # print(f"Left Same: Expected {tree_recur[i].left.key} {recur_color} and got {tree_my[i].left.key} {my_color}")
                same += f" | Right Same: Expected {tree_recur[i].right.key} {recur_color} and got {tree_my[i].right.key} {my_color}"
                same_count += 1
            else:
                # print(f"Left Different: Expected {tree_recur[i].left.key} {recur_color} and got {tree_my[i].left.key} {my_color}")
                different += f" | Right Different: Expected {tree_recur[i].right.key} {recur_color} and got {tree_my[i].right.key} {my_color}"
                different_count += 1
        if same != "":
            print(same)
        if different != "":
            print(different)
        same = ""
        different = ""
    if same_count != 0:
        print(f'Passed {same_count}/{same_count+different_count} tests \n')
    if different_count != 0:
        print(f'Failed {different_count}/{same_count+different_count} tests \n')

if __name__ == "__main__":
    bst = RedBlackBST()
    kvs_to_insert = [(1, 'one'),
                     (2, 'two'),
                     (3, 'three'),
                     (4, 'four'),
                     (5, 'five'),
                     (6, 'six'),
                     (7, 'seven'),
                     (8, 'eight'),
                     (9, 'nine'),
                     (10, 'ten'),
                     (11, 'ele')]

    my_bst = RedBlackBST()
    recur_bst = RedBlackBST()
    test_bst_2(my_bst, recur_bst, kvs_to_insert)

    kvs_to_insert2 = [(1, 'one'),
                     (2, 'two'),
                     (3, 'three'),
                     (4, 'four'),
                     (5, 'five')]

    my_bst2 = RedBlackBST()
    recur_bst2 = RedBlackBST()
    test_bst_2(my_bst2, recur_bst2, kvs_to_insert2)

    kvs_to_insert3 = [('ab', 1),
                     ('bc', 2),
                     ('cd', 3),
                     ('de', 4),
                     ('ef', 5)]
    my_bst3 = RedBlackBST()
    recur_bst3 = RedBlackBST()
    test_bst_2(my_bst3, recur_bst3, kvs_to_insert3)

    kvs_to_insert4 = [('one', 5),
                     ('two', 4),
                     ('three', 3),
                     ('four', 2),
                     ('five', 1)]
    my_bst4 = RedBlackBST()
    recur_bst4 = RedBlackBST()
    test_bst_2(my_bst4, recur_bst4, kvs_to_insert4)

    kvs_to_insert5 = [(10, 'c'),
                    (9, 'a'),
                    (8, 'z'),
                    (7, 'y'),
                    (6, 'x'),
                    (5, 'c'),
                    (4, 'a'),
                    (3, 'z'),
                    (2, 'y'),
                    (1, 'x')]
    my_bst5 = RedBlackBST()
    recur_bst5 = RedBlackBST()
    test_bst_2(my_bst5, recur_bst5, kvs_to_insert5)


