import csv
from hashmap import Hashmap

hashedBooks = Hashmap(50000) # List contains 49927, 50000 is a safe number but probably too high
hashedAuthors = Hashmap(50000)
hashedGenres = Hashmap(10000)

with open('books_1.Best_Books_ever.csv', encoding="utf8") as books_csv:
    books_list = csv.DictReader(books_csv, delimiter=',')
    for book in books_list:

        genres = book["genres"]
        genres = genres.replace('[','')
        genres = genres.replace(']','')
        genres = genres.replace('.','')
        genres = genres.replace('\'','')
        book["genres"] = genres.split()
        
        hashedBooks.assign(book["title"], book)
        
        title_and_rating = [book["title"], book["rating"]]

        books_by_author = hashedAuthors.retrieve(book["author"])
        if books_by_author is None:
            books_by_author = []

        books_by_author.append(title_and_rating)
        hashedAuthors.assign(book["author"],books_by_author)

        for genre in book["genres"]:
            books_in_genre = hashedGenres.retrieve(genre)
            if books_in_genre is None:
                books_in_genre = []

            books_in_genre.append(title_and_rating)
            hashedGenres.assign(genre,books_in_genre)

