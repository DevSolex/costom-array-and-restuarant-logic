class Array:
    
    def __init__(self, array=[]):
        self.array = []

    def append(self, value):
        self.array += [value]

    def insert(self, index, value):
        if index <=len(self.array):
            first = self.array[:index]
            last = self.array[index:]
            self.array = first + [value] + last


    def remove(self, value):
        i = 0
        for item in self.array:
            if item == value:
                del self.array[i]
            i += 1

#    def pop(self):
        del self.array[-1]

    def pop(self, index=-1):
        if index == -1:
            del self.array[-1]
        else:
            del self.array[index]

    def __str__(self):
        return str(self.array)

# Array = Array()


# Array.append(2)
# print(Array.array)
# Array.append('solex')
# Array.append(4)
# Array.append(9)
# print(Array.array)
# # Array.insert(4,'solo')
# # print(Array.array)
# # Array.remove(2)
# # print(Array.array)
# Array.pop(2)
# print(Array.array)
# # Array.pop()
# # print(Array.array)