class Item:
    #libraryitem
    count = 0
    totalduration = 0
    def __init__(self, t, d):
        self.title = t
        self.duration = d  #time to complete 
        Item.total_items()
        Item.total_duration(self.duration)
    @classmethod
    def total_items(cls):
        cls.count += 1 
    
    @classmethod
    def total_duration(cls, d):
        cls.totalduration += d
        
    @staticmethod
    def info():
        print(f"You have borrowed {Item.count} library items and total duration in hours {Item.totalduration}")
        
class DVD(Item):
    def __init__(self, t, d, g, dr):
        super().__init__(t,d)
        self.genre = g
        self.director = dr
    def __str__(self):
       return f"You have borrowed a {self.genre} DVD directed by {self.director}"
    
class Book(Item):
    def __init__(self, t, d, a, s):
        super().__init__(t,d)
        self.author = a
        self.subject = s
    def __repr__(self):
        return f"Book Title: {self.title} \n Subject: {self.subject} \n Author: {self.author}"
    
if __name__ == '__main__':
    b1 = Book("ABC",2,"BumbleBee","English")
    b2 = Book("123",3,"Numbers","Math")
    d1 = DVD("Avengers",2,"Sci-fi","Alex")
    d2 = DVD("Wednesday",20,"Horror","Tim Burton")
    
    Item.info()
    print(str(d2))
    print(repr(b1))
    print(d1)
    #repr(b2)
    
    d = {'a':1,"b":2, 'cd':3}
    b = reversed(d)
    print(d)
    print(dict(zip(list(b),d.values())))
    #d.reverse()
    #print(d)
    c = dict(reversed(d.items()))
    print(c)