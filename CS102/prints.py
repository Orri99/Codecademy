
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
    print(f"If any of these results are the {searched_item} you are looking for,\nor if any of them interest you please type their corresponding number,")
    if current_page < number_of_pages:
        print("if you want to see more results type \"next\",")
    if current_page > 1:
        print("if you want to go back to previous results type \"back\",")
    return input("if not type anything else: ").lower()