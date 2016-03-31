import random
import math


class BalancedSearchTree(object):
    """
    Balanced Search Tree
    usage: bs.BalancedSearchTree
            call bs.insert to add int to tree
            call bs.insertlist to add a whole list to tree
    :todo: create a better print function for displaying tree
    """
    def __init__(self, size=16):
        self.tree = [-1 for x in range(size)]
        self.size = int(math.pow(2, 1 + math.floor(math.log(size - 1, 2))))     # forces a power of 2 list
        self.root = 1
        self.items = 0
        self.comparisons = 0

    def insert(self, val):
        """

        :param val: value to insert into tree
        :type val: int
        :return: none

        """
        # If list (tree) is empty, put value at root
        if self.tree[self.root] == -1:
            self.tree[self.root] = val
        # loop until you find the location to insert
        # even if you have to extend this list
        else:
            i = self.root
            loop = self.find(val)       # prevents repeated values
            while not loop:
                if val > self.tree[i]:
                    i = self.rightchild(i)
                else:
                    i = self.leftchild(i)

                if i >= self.size:
                    self.extend()
                    self.balance()

                if self.tree[i] == -1:
                    self.tree[i] = val
                    self.items += 1
                    loop = True

    def balance(self, tree=[]):
        """
        :description: balance makes use of the fact we are using a list to store our tree. It sorts the list first,
            then uses the built in insert function to reapply the values in a more balanced order.

        :param tree: list that holds the values of self.tree
        :type tree: list
        :return: none

        """
        if not tree:    # if no list was passed use self.tree
            tree = self.tree
        templist = set(tree)    # remove dupes ie -1
        templist = list(templist)   # recast as list
        templist.sort()     # sort list

        self.tree = [-1 for x in range(self.size)]

        self._balance(0, len(templist)-1, templist)  # get balanced tree back

    def _balance(self, start=0, end=1, list=[]):
        """

        :param start: the starting point of the list to be sorted into a tree
        :type start: int
        :param end: the ending point of a the list to be sorted into a tree
        :type end: int
        :param list:
        :type list: list
        :return: returns nothing
        :rtype: none
        """
        if start > end:     # if start is larger than end get out
            return
        mid = (start + end)//2      # set a mid point and insert it into tree

        self.insert(list[mid])      # insert node into tree

        self._balance(start, mid-1, list)   # recursive calls to gather nodes
        self._balance(mid+1, end, list)

    def insertlist(self, inlist=[]):
        """

        :param inlist: the list to be inserted if no value is given assumes an empty list
        :type inlist: list
        :return: none
        """
        self.balance(inlist)    # calls balance tree to create a new tree from list

    def extend(self):
        """
        :description: extends the size of the list when a value will not fit in current tree
        :return: none
        """
        temp = [-1 for x in range(self.size)]
        self.tree.extend(temp)
        self.size *= 2
        # print('.', end='')

    def find(self, key):
        """

        :param key: the value to be found
        :type key: int
        :return: if the key was found or not
        :rtype: bool
        """
        self.comparisons = 1

        if key == self.tree[self.root]:
            return True
        else:
            i = self.root
            while True:
                if key < self.tree[i]:
                    i = self.leftchild(i)
                else:
                    i = self.rightchild(i)

                if i >= self.size:
                    return False

                if self.tree[i] == -1:
                    return False

                if self.tree[i] == key:
                    return True

                self.comparisons += 1

    def leftchild(self, i):
        return 2 * i

    def rightchild(self, i):
        return 2 * i + 1

    # def printtree(self):
    #     for x in range(int(math.log(self.size, 2))):
    #         for foo in range(pow(x, 2)):
    #             print(self.tree[2*foo], end='')
    #             print('  ', end='')
    #             print(self.tree[2*foo+1], end='')
    #         print(' ')

if __name__ == '__main__':

    random.seed(342345)
    bs = BalancedSearchTree(16)
    for x in range(15):
        bs.insert(x+1)
    print(bs.tree)
    bs.balance()
    print(bs.tree)
    print(bs.find(42))
    # bs.printtree()
    intlist = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11,12,13,14,15]
    bs.insertlist(intlist)
    print(bs.tree)
