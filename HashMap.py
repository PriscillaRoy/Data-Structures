
class HashMap:
    def __init__(self):
        self.size = 5
        self.map = [None] * self.size

    def get_hash(self, key):
        hash_index = 0
        for char in str(key):
            hash_index+= ord(char)
        hash_index%=self.size
        return(hash_index)

    def add(self, key, value):

        hash_value = self.get_hash(key)

        key_value = [key, value]

        if self.map[hash_value] is None:
            self.map[hash_value] = list([key_value])
            return True
        else:
            for k_v in self.map[hash_value]:
                if k_v[0] == key:
                    k_v[1] = value
                    return True
            self.map[hash_value].append(key_value)
            return True

    def delete(self, key):

        hash_value = self.get_hash(key)
        if self.map[hash_value] is None:
            return False
        else:
            for i in range(0, len(self.map[hash_value])):
                if self.map[hash_value][i][0] == key:
                    self.map[hash_value].pop(i)
                    return True


    def get(self, key):
        hash_value = self.get_hash(key)
        if self.map[hash_value] is None:
            return False
        else:
            for i in range(0, len(self.map[hash_value])):
                if self.map[hash_value][i][0] == key:
                    return self.map[hash_value][i][1]

    def print(self):
        for data in self.map:
            if data is not None:
                print (str(data))


h = HashMap()

h.add("Carrots", 19)
h.print()