# _______________Create a class _________________
# CLass = Data + Behaviour(MEthod / function)

# __________Parent Book_________________

class Book: 
    def __init__ (self, author, title, Quantity):
        self.title = title
        self.author = author
        self.Quantity = Quantity

# _______________Method_________________

    def display_info(self):
        print(f"author: {self.author}, Title of Book: {self.title}, Quantity: {self.Quantity}")


# _______________Child Book____________

class Novel(Book): # extends 
    def __init__ (self, author, title, Quantity, pages):
        super().__init__(author, title, Quantity)
        self.pages = pages


    def display_info(self):
        print(f"author: {self.author}, Title of Book: {self.title}, Quantity: {self.Quantity}, Pages: {self.pages}")


############################ Consumer Side ###################       

# _______________Create Object using contructor _________________

book1 = Book('AaMna', 'Python for beginners','9')
book2 = Book('Fatima', 'Web & Mobile Application for beginners','10')
book3 = Novel('Elif Shafak', 'The Forty Rules of Love', '11', '333')


#____________ Print________________

print(book1.author)
(book1.display_info())
(book2.display_info())
(book3.display_info())