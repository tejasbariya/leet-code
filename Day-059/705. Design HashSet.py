class MyHashSet(object):

    def __init__(self):
        self.set = {}

    def getHash(self, key):
        return key % 9
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        func = self.getHash(key)
        if func not in self.set:
            self.set[func] =  []
        if not self.contains(key):
            self.set[func].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        func = self.getHash(key)
        if self.contains(key):
            for i in range(len(self.set[func])):
                if self.set[func][i] == key:
                    self.set[func].pop(i)
                    break
            if self.set[func] == []:
                self.set.pop(func)
                return 

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        func = self.getHash(key)
        if func in self.set:
            if key in self.set[func]:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)