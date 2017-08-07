# special methods

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    #special method for string representation of object
    def __str__(self):
        return 'Title: {}\nAuthor: {}\nPages: {}'.format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book is destroyed!')

b = Book('Python', 'Jose', 200)
print(b)
print(len(b))
del b
