'''
Design a Library Management System

Problem Statement: Design a basic library management system that allows users to:

Search for books by title, author, or ISBN.
Borrow and return books.
Track whether a book is available or checked out.
Requirements:

Book Management:

Each book has a title, author, ISBN, and availability status.
A method to check if the book is available.
User Management:

Each user can borrow and return books, with a limit on the number of books they can borrow at once (e.g., 5 books).
Library Operations:

A method to search for books by title, author, or ISBN.
A method to update the status of a book (available or checked out) when a user borrows or returns it.



'''


class Book:
    def __init__(self,title,author,ISBN, availability_status):
        self.title = title
        self.author = author 
        self.isbn = isbn 
        self.availability_status = availability_status
    
    def change_status(self, new_status):
        self.availability_status = new_status
    
    def check_availability(self):
        return self.availability_status

class User:
    def __init__(self,id, borrowed_list):
        self.id = id 
        self.borrowed_list = []
    
    def borrow(self,book):
        self.borrowed_list.append(book)
        book.availability_status = "borrowed"
    
    def return_book(self,book):
        self.borrowed_list.remove(book)
        book.availability_status = "available"

class UserManagement():
    def __init__(self,books,ids):
        #creat a list of books that key is book_id and value is an object of Book class 
        self.book_by_id ={}
        #create a list of books that key is book name and value is an object of Book class 
        self.book_by_name ={}
        #create a list of books that key is author and value is an object of Book class 
        self.book_by_author = {}
        self.ids = {}
    
    def search_book_by_id(self,book_id):
        if book_id in self.book_by_id:
            return self.book_by_id[book_id]
    
