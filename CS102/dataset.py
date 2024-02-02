import csv
from linkedlist import Node, LinkedList
from hashmap import Hashmap

with open('books_1.Best_Books_ever.csv', encoding="utf8") as books_csv:
    books_list = csv.DictReader(books_csv, delimiter=',')
    for book in books_list:
        print(book['title'])
