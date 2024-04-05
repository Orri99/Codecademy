
def newline(number_of_lines=1):
    print("\n" * number_of_lines)

def starting_message():
    newline(2)
    print("--------------------------------------------------------------------")
    print("|                                                                  |")
    print("|              Welcome to Orri's book recommendations              |")
    print("|                                                                  |")
    print("--------------------------------------------------------------------")
    newline(2)
    print("You can look up book titles, author names or genres and we'll help")
    print("you find a book to your liking.")
    newline()
    print("Please wait a momemt while the data loads.")
    newline()

def list_page(result_list, current_page, number_of_pages, searched_item):
    newline()
    for index in range(len(result_list)):
        item_number = index+1 + 10*(current_page-1)
        print(f"{item_number}. " + result_list[index])
    newline()
    print(f"Page {current_page}/{number_of_pages}")
    newline()
    if searched_item == "looking at author or genre":
        print(f"If any of these titles interest you please type their corresponding number,")
    else:
        print(f"If any of these results are the {searched_item} you are looking for,\nor if any of them interest you please type their corresponding number,")
    if current_page < number_of_pages:
        print("if you want to see more results type \"next\",")
    if current_page > 1:
        print("if you want to go back to previous results type \"back\",")
    return input("if not type anything else: ").lower()

def print_book(selected_book, selection_list, lengths, genres): 

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    newline()
    print(selected_book["title"])
    newline()
    print("By "+ selected_book["author"])
    newline()
    print("Rating: " + selected_book["rating"])
    newline()

    selection_item = 0
    if lengths[0] is not (0 or None):
        print("This book is part of a series, here are some other titles in the same series: ")
        for index in range(0,lengths[0]):
            print(str(selection_item+1) + ". " + selection_list[selection_item])
            selection_item += 1
    newline()

    if lengths[1] is not (0 or None):
        print("Here is are the top rated books by the same author: ")
        for index in range(0,lengths[1]):
            print(str(selection_item+1) + ". " + selection_list[selection_item])
            selection_item += 1
    newline()

    if lengths[2] is not (0 or None):
        print("Here are the top rated books in the same genres:")
        for idx in range(2, len(lengths)):
            newline()
            print("For the genre \"" + genres[idx-2][0] + "\":")
            for index in range(0,lengths[idx]):
                print(str(selection_item+1) + ". " + selection_list[selection_item])
                selection_item += 1
    newline()

    print("If you want to take a closer look at any of these titles type in their respective number,")
    user_input = input("otherwise type anything else: ")
    try:
        selected = int(user_input)
        selected -= 1
        if selected >= 0 and selected < selection_item:
            return selected
        else:
            return None
    except:
        return None
            