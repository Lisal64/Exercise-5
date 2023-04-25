# Exercise 1


def selection_sort(numbers: list):
    for i in range(0, len(numbers) - 1):
        maxi = i  # saving a current maximum value
        for j in range(i + 1, len(numbers)):  # starting at one position further - to compare go to the very back
            if numbers[maxi] > numbers[j]:
                maxi = j
        temp = numbers[maxi]
        # need to use the original location that loops from the start,
        # not everything would be compared otherwise
        numbers[maxi] = numbers[i]
        numbers[i] = temp
    return numbers

# Exercise 2


def binary_search(text: list, target: str):  # need to make it work for texts still
    text.sort()  # only works for sorted lists - maybe more efficient if we sort it once outside the function
    first = 0
    last = len(text) - 1
    found = False

    while first <= last and not found:  # if they are the same we found our target
        mid = (first + last) // 2  # two slashes automatically return an integer
        middle = text[mid]  # need to tell it explicitly what to do in each case
        # if I just specified the case of it being bigger, it wouldn't find it if it was smaller
        if middle > target:
            last = mid - 1
        elif middle < target:
            first = mid + 1
        else:
            found = True
    return middle

# Exercise 3


class Node:  # implementing buckets in form of linked lists, so I need a node-class
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class HashTable:

    def __init__(self, size: int):
        self.size = size
        self.buckets = [None for i in range(size)]  # adding an empty list to every index in our hash table

    # Exercise 4
    def __my_hash(self, key):
        if isinstance(key, str):  # checking the type of input I get
            # using *2 to get a wider amount of values, otherwise it might just be all 1
            hash_key = (len(key) * 2) % self.size
            return hash_key
        if isinstance(key, int):
            hash_key = (key * 2) % self.size
            return hash_key

    # Exercise 5

    def put(self, key, data):
        hash_value = self.__my_hash(key)  # calculating the hash key
        node = self.buckets[hash_value]
        if node is None:  # if that bucket is empty, the node is stored at the first position
            self.buckets[hash_value] = Node(key, data)  # storing the value and key as a node
            return
        while node is not None:  # if there is something in that list
            if node.key == key:  # if the same key is used, the list is updated
                node.data = data
                return
            else:  # in case of collision - loop through the bucket to store it at the next None-value
                previous = None
                while node is not None:  # while there is data in the bucket
                    previous = node  # setting the previous value
                    node = node.next  # setting the pointer to the next node
                previous.next = Node(key, data)  # creating the next node based on the values put in
        return

    # Exercise 6

    def get(self, key):
        hash_value = self.__my_hash(key)  # calculating the hash key
        node = self.buckets[hash_value]
        # have to use a loop because of the collisions
        while node is not None:
            if node.key == key:
                return node.data
            node = node.next
        else:
            return None
        