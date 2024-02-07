import csv
from hashmap import Hashmap
from prints import newline, starting_message

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
        
        elif len(possible_items) <= 10:
            newline()
            print("A few results were found:")
            for index in range(len(possible_items)):
                print(str(index+1) + ". " + possible_items[index])
            newline()
            user_input = input(f"If any of these results are the {searched_item} you are looking for,\nor if any of them interest you please type their corresponding number,\nif not type anything else: ")
            try:
                selected = int(user_input)
                if selected < len(possible_items):
                    return hashed_data.retrieve(possible_items[selected-1])
            except:
                newline()
                print("It seems that did not result in what you were looking for.")
            searching = keep_searching()

        else:
            newline()
            print("That search term was a bit vague, please try to be a bit more specifc.")
            searching = keep_searching()

starting_message()

with open('books_1.Best_Books_ever.csv', encoding="utf8") as books_csv:
    books_list = csv.DictReader(books_csv, delimiter=',')
    for book in books_list:

        book["genres"] = genre_string_to_list(book["genres"])
        
        hashedBooks.assign(book["title"], book)
        searchListBooks.add(book["title"])
        #if book["title"] not in searchListBooks:
            #searchListBooks.append(book["title"])
        
        title_and_rating = [book["title"], book["rating"]]

        books_by_author = hashedAuthors.retrieve(book["author"])
        if books_by_author is None:
            books_by_author = []

        books_by_author.append(title_and_rating)
        hashedAuthors.assign(book["author"],books_by_author)
        searchListAuthors.add(book["author"])
        #if book["author"] not in searchListAuthors:
        #    searchListAuthors.append(book["author"])

        for genre in book["genres"]:
            if genre != "":
                books_in_genre = hashedGenres.retrieve(genre)
                if books_in_genre is None:
                    books_in_genre = []

                books_in_genre.append(title_and_rating)
                hashedGenres.assign(genre,books_in_genre)
                searchListGenres.add(genre)
                #if genre not in searchListGenres:
                #    searchListGenres.append(genre)

searchListBooks = list(searchListBooks)
searchListAuthors = list(searchListAuthors)
searchListGenres = list(searchListGenres)

print("Ok lets get started, are you looking for a book title, an author or a genre?")
user_input = input("Answer: ").lower()
user_active = True

while user_active:
    if user_input == "book title":
        pass
    elif user_input == "author":
        pass
    elif user_input == "genre":
        print(search_for_item(hashedGenres, searchListGenres, "genre"))
        user_active = keep_searching()
    elif user_input == "quit":
        user_active = False
    else:
        user_input = input("I didn't quite catch that, please type your choice again: ").lower()
