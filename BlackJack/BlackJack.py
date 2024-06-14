import random, time

try:
    main_file = open("mainBJ.txt", "a")
except:
    main_file = open("mainBJ.txt", "w")
    main_file.close()
    main_file = open("mainBJ.txt", "a")

def register(file):
    detail_loop = True

    temp_list = file.read().splitlines()

    username = ""
    password = ""
    score = 0

    while detail_loop:
        username = input("Please enter new username")
        password = input("Please enter new password")

        if username not in temp_list:
            detail_loop = False
        else:
            print("Username not avaliable")
            detail_loop = True

    file.write("\n".join([username, password, score]))
    file.write("\n")
    file.close()

    print("New account created!")
    time.sleep(2)

    user_details = [username, password, score]

    return user_details

    
def login(username, password, file):
    logged_in = False

    user_details = []

    logins_list = []
    temp_list = file.read().splitlines()
    temp_list2 = []

    for i in range(len(temp_list)):
        temp_list2.append(temp_list[i])
        if len(temp_list2) == 3:
            logins_list.append(temp_list2)
            temp_list2 = []

    

    file.close()

    for i in range(len(logins_list)):
        if logins_list[i][0] == username and logins_list[i][1] == password:
            user_details.append(logins_list[i][0])
            user_details.append(logins_list[i][1])
            user_details.append(logins_list[i][2])
            logged_in = True
            break

    if logged_in == True:
        print("You have logged in!")
    else:
        print("Your details are not known")

    return user_details

def main_menu(file):
    valid = False
    
    while valid != True:
        print("Please login or Register")
        print("1. Login")
        print("2. Register")
        user_choice = input("")

        try:
            int(user_choice)
            if int(user_choice) < 0 or int(user_choice) > 2:
                raise "Invalid Choice"
        except:
            print("Invalid Choice")
            valid = False
        else:
            valid = True
        
    if int(user_choice) == 1:
        user_details = login(file)
    else:
        user_details = register(file)
    
    print("Game Begining")

    return user_details
    
def blackjack():
    game_loop = True
    score = 0

    card_types = ["Hearts", "Diamonds", "Spades", "Clubs"]
    card_names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    cards = []
    avaliable_cards = []
    used_cards = []
    user_cards = []
    cm_cards = []

    for i in range(len(card_types)):
        for x in range(len(card_names)):
            cards.append(card_names[x]+" of "+card_types[i])
    
    for i in range(len(cards)):
        if "Ace" in cards[i]:
            avaliable_cards.append([cards[i], card_values[0]])
        elif "2" in cards[i]:
            avaliable_cards.append([cards[i], card_values[1]])
        elif "3" in cards[i]:
            avaliable_cards.append([cards[i], card_values[2]])
        elif "4" in cards[i]:
            avaliable_cards.append([cards[i], card_values[3]])
        elif "5" in cards[i]:
            avaliable_cards.append([cards[i], card_values[4]])
        elif "6" in cards[i]:
            avaliable_cards.append([cards[i], card_values[5]])
        elif "7" in cards[i]:
            avaliable_cards.append([cards[i], card_values[6]])
        elif "8" in cards[i]:
            avaliable_cards.append([cards[i], card_values[7]])
        elif "9" in cards[i]:
            avaliable_cards.append([cards[i], card_values[8]])
        elif "10" in cards[i]:
            avaliable_cards.append([cards[i], card_values[9]])
        elif "Jack" in cards[i]:
            avaliable_cards.append([cards[i], card_values[10]])
        elif "Queen" in cards[i]:
            avaliable_cards.append([cards[i], card_values[11]])
        elif "King" in cards[i]:
            avaliable_cards.append([cards[i], card_values[12]])



    while game_loop:
        print("\n\n\n")
        



user_details = main_menu(main_file)

score = blackjack()