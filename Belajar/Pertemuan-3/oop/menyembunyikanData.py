class Counter:
    __secret_count = 0
    
    def count(self):
        self.__secret_count += 1
        print(self.__secret_count)

counter = Counter()
counter.count()
counter.count()
# print(counter.__secret_count) # Eror : AttributeError: 'Counter' object has no attribute '__secret_count'