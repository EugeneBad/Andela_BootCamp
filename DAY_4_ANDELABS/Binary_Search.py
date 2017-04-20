class BinarySearch(list):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        list.__init__(self)
        self.length = self.a


        for x in range(self.a):
            self.append(self.b + (x * self.b))

    def search(self, item):
        self.count = 0
        alist = [self.b + (x * self.b)
                 for x in range(self.a)]

        first = 0
        last = len(alist)-1

        if alist[last] == item:
            return {'count': self.count, 'index': last}

        found = False
        while first <= last and not found:

            midpoint = int((first + last) / 2)

            self.index = midpoint
            if alist[midpoint] == item:
                found = True
            else:
                if item < alist[midpoint]:
                    last = midpoint-1
                else:
                    self.count += 1
                    if self.count == 3:
                        return {'count': self.count, 'index': -1}

                    else:
                        first = midpoint+1
        return {'count':self.count, 'index':self.index}
