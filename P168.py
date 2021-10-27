class Bookshelf:
    def __init__(self,name,author,price,publishing_year):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_publishing_year = publishing_year
    
    def add_book(self):
        print('Book Name: ' + self.book_name)
        print('Book Author: ' + self.book_author)
        print('Book Price: ' + self.book_price)
        print('Book was published in: ' + self.book_publishing_year)
        print('Book Added')
     
    def years_since_published(self):
        years_ago_published = 2021 - int(self.book_publishing_year)
        print('This book was published' + str(years_ago_published) + 'ago')
    
Book1 = Bookshelf("Harry Potter and the Philospher's Stone","J.K. Rowling",'1928','1997')
Book1.add_book()
Book1.years_since_published()    