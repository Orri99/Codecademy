import csv
import math
from hashmap import Hashmap
from prints import newline, starting_message, list_page

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

def search_for_item(hashed_data, data_list, searched_item):

    searching = True
    while searching:
        newline()
        user_input = input(f"Please type the name of the {searched_item} your are looking for: ")

        #item_data = hashed_data.retrieve(user_input)
        #if item_data is not None:
            #return item_data
    
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
                    if selected < len(possible_items):
                        return hashed_data.retrieve(possible_items[selected-1])
                    else:
                        newline()
                        print("It seems that did not result in what you were looking for.")
                        searching = keep_searching()
                except:
                    if current_page < number_of_pages and user_input == "next":
                        current_page += 1
                    elif current_page > 1 and user_input == "back":
                        current_page -= 1
                    else:
                        newline()
                        print("It seems that did not result in what you were looking for.")
                        searching = keep_searching()


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
    if user_input == "book title":
        print(search_for_item(hashedBooks, searchListBooks, "book title"))
        user_active = keep_searching()
    elif user_input == "author":
        print(search_for_item(hashedAuthors, searchListAuthors, "author/s"))
        user_active = keep_searching()
    elif user_input == "genre":
        print(search_for_item(hashedGenres, searchListGenres, "genre"))
        user_active = keep_searching()
    elif user_input == "quit":
        user_active = False
    else:
        user_input = input("I didn't quite catch that, please type your choice again: ").lower()
