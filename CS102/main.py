import csv
import math
from hashmap import Hashmap
from prints import newline, starting_message, list_page, print_book
from sort_algos import bubblesort, mergesort

hashedBooks = Hashmap(10000) # Number picked arbitrarily
hashedAuthors = Hashmap(10000)
hashedGenres = Hashmap(5000)
searchListBooks = set()      #These start of as sets but get changed into lists, a list is needed but a set is created way faster
searchListAuthors = set()
searchListGenres = set()

def genre_string_to_list(genre_string):
    genre_string = genre_string.replace('[','').replace(']','').replace('\'','')
    return genre_string.split(', ')

def keep_searching(first_loop = True):
    newline()
    if first_loop:    
        user_input = input("Would you like to keep searching? [y/n] ").lower()
    else:
        user_input = input("I didn't understand that, please type y or n: ").lower()

    if user_input == "y" or user_input == "yes":
        return True
    elif user_input == "n" or user_input == "no":
        return False
    else:
        return keep_searching(False)

def search_for_item(data_list, searched_item):

    searching = True
    while searching:
        newline()
        user_input = input(f"Please type the name of the {searched_item} your are looking for: ")
    
        possible_items = []
        for index in range(len(data_list)):
            if user_input.lower() in data_list[index].lower():
                possible_items.append(data_list[index])
    
        if len(possible_items) <= 0:
            newline()
            print("No results found.")
            searching = keep_searching()
        
        else: #len(possible_items) <= 10:
            newline()
            if len(possible_items) == 1:
                print("One result was found;")
            else:
                print("A few results were found:")

            print(f"Number of results: {len(possible_items)}")

            number_of_pages = math.ceil(len(possible_items)/10)
            current_page = 1

            selecting_result = True
            while selecting_result:
            
                user_input = list_page(possible_items[10*(current_page-1):10*(current_page)], current_page, number_of_pages, searched_item)
                try:
                    selected = int(user_input)
                    if selected <= len(possible_items):
                        return possible_items[selected-1]
                    else:
                        newline()
                        print("It seems that didn't result in what you were looking for.")
                        selecting_result = keep_searching()
                except:
                    if current_page < number_of_pages and user_input == "next":
                        current_page += 1
                    elif current_page > 1 and user_input == "back":
                        current_page -= 1
                    else:
                        newline()
                        print("It seems that did not result in what you were looking for.")
                        selecting_result = keep_searching()

def show_book(selected_book, book_hashmap, author_hashmap, genre_hashmap): 
     
    selection_list = []
    lengths = []
    genre_list = []

    books_by_current_author = author_hashmap.retrieve(selected_book["author"])
    books_by_current_author = bubblesort(books_by_current_author)

    if len(books_by_current_author) <= 5:
        best_by_author = len(books_by_current_author) - 1 # -1 because the selected book is in there too
    else:
        best_by_author = 5

    for genre in selected_book["genres"]:
        genre_list.append([genre, len(genre_hashmap.retrieve(genre))])
    genre_list = mergesort(genre_list)

    if len(genre_list) < 3:
        best_genres = len(genre_list)
    else:
        best_genres = 3 

    count = 0
    if selected_book["series"] is not None:
        for book in books_by_current_author:
            if book[0] != selected_book["title"] and count < 5:
                current_book = book_hashmap.retrieve(book[0])
                if (current_book["series"][:-3] == selected_book["series"][:-3]) and (current_book != selected_book):
                    selection_list.append(current_book["title"])
                    count += 1
            elif count == 5:
                break
    lengths.append(count)

    count = 0
    for index in range(0,best_by_author+1):
        if count != 5 and books_by_current_author[index][0] != selected_book["title"]:
            selection_list.append(books_by_current_author[index][0])
            count += 1
    lengths.append(count)

    for index in range(0,best_genres):
        count = 0
        books_in_current_genre = genre_hashmap.retrieve(genre_list[index][0])
        books_in_current_genre = mergesort(books_in_current_genre)
        if len(books_in_current_genre) <= 5:
            num_books = len(books_in_current_genre) - 1
        else:
            num_books = 5
        for idx in range(0,num_books+1):
            if count != 5 and books_in_current_genre[idx][0] != selected_book["title"]:
                selection_list.append(books_in_current_genre[idx][0])
                count += 1
        lengths.append(count)

    next_book = print_book(selected_book, selection_list, lengths, genre_list[:best_genres])
    if next_book is not None:
        show_book(book_hashmap.retrieve(selection_list[next_book]), book_hashmap, author_hashmap, genre_hashmap)

def show_author(selected_author, book_hashmap, author_hashmap, genre_hashmap):
    
    books_by_current_author = author_hashmap.retrieve(selected_author)
    books_by_current_author = mergesort(books_by_current_author)

    data_list = []
    for book in books_by_current_author:
        data_list.append(book[0])

    if len(data_list) <= 0:
            newline()
            print("No results found.")
        
    else: #len(possible_items) <= 10:
        newline()
        if len(data_list) == 1:
            print("This author has only pubished one book:")
        else:
            print(f"This author has published {len(data_list)} books:")

        number_of_pages = math.ceil(len(data_list)/10)
        current_page = 1

        selecting_result = True
        while selecting_result:
            
            user_input = list_page(data_list[10*(current_page-1):10*(current_page)], current_page, number_of_pages, "looking at author or genre")
            try:
                selected = int(user_input)
                if selected <= len(data_list):
                    show_book(book_hashmap.retrieve(data_list[selected-1]), book_hashmap, author_hashmap, genre_hashmap)
                    selecting_result = False
                else:
                    newline()
                    print("It seems that didn't result in what you were looking for.")
                    selecting_result = False
            except:
                if current_page < number_of_pages and user_input == "next":
                    current_page += 1
                elif current_page > 1 and user_input == "back":
                    current_page -= 1
                else:
                    newline()
                    print("It seems that did not result in what you were looking for.")
                    selecting_result = False

def show_genre(selected_genre, book_hashmap, author_hashmap, genre_hashmap):
    
    books_in_current_genre = genre_hashmap.retrieve(selected_genre)
    books_in_current_genre = mergesort(books_in_current_genre)

    data_list = []
    for book in books_in_current_genre:
        data_list.append(book[0])

    if len(data_list) <= 0:
            newline()
            print("No results found.")
        
    else: #len(possible_items) <= 10:
        newline()
        if len(data_list) == 1:
            print("There is one book in this genre:")
        else:
            print(f"There are {len(data_list)} books in this genre:")

        number_of_pages = math.ceil(len(data_list)/10)
        current_page = 1

        selecting_result = True
        while selecting_result:
            
            user_input = list_page(data_list[10*(current_page-1):10*(current_page)], current_page, number_of_pages, "looking at author or genre")
            try:
                selected = int(user_input)
                if selected <= len(data_list):
                    show_book(book_hashmap.retrieve(data_list[selected-1]), book_hashmap, author_hashmap, genre_hashmap)
                    selecting_result = False
                else:
                    newline()
                    print("It seems that didn't result in what you were looking for.")
                    selecting_result = False
            except:
                if current_page < number_of_pages and user_input == "next":
                    current_page += 1
                elif current_page > 1 and user_input == "back":
                    current_page -= 1
                else:
                    newline()
                    print("It seems that did not result in what you were looking for.")
                    selecting_result = False

starting_message()

with open('books_1.Best_Books_ever.csv', encoding="utf8") as books_csv:
    books_list = csv.DictReader(books_csv, delimiter=',')
    for book in books_list:

        book["genres"] = genre_string_to_list(book["genres"])
        
        hashedBooks.assign(book["title"], book)
        searchListBooks.add(book["title"])
        
        title_and_rating = [book["title"], book["rating"]]

        books_by_author = hashedAuthors.retrieve(book["author"])
        if books_by_author is None:
            books_by_author = []

        books_by_author.append(title_and_rating)
        try:
            hashedAuthors.assign(book["author"],books_by_author)
        except:
            print("Failed")

        searchListAuthors.add(book["author"])

        for genre in book["genres"]:
            if genre != "":
                books_in_genre = hashedGenres.retrieve(genre)
                if books_in_genre is None:
                    books_in_genre = []

                books_in_genre.append(title_and_rating)
                hashedGenres.assign(genre,books_in_genre)
                searchListGenres.add(genre)

searchListBooks = list(searchListBooks)
searchListAuthors = list(searchListAuthors)
searchListGenres = list(searchListGenres)

print("Ok lets get started, are you looking for a book title, an author or a genre?")
user_input = input("Answer: ").lower()
user_active = True

while user_active:
    if user_input == "book":
        found_book = search_for_item(searchListBooks, "book")
        show_book(hashedBooks.retrieve(found_book), hashedBooks, hashedAuthors, hashedGenres)
        user_active = keep_searching()
    elif user_input == "author":
        found_author = search_for_item(searchListAuthors, "author/s")
        show_author(found_author, hashedBooks, hashedAuthors, hashedGenres)
        user_active = keep_searching()
    elif user_input == "genre":
        found_genre = search_for_item(searchListGenres, "genre")
        show_genre(found_genre, hashedBooks, hashedAuthors, hashedGenres)
        user_active = keep_searching()
    elif user_input == "quit":
        user_active = False
    else:
        user_input = input("I didn't quite catch that, please type your choice again: ").lower() 