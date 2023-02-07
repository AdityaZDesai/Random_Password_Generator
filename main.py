import random

def generate_password(max):
    char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
    upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = [0,1,2,3,4,5,6,7,8,9]
    symbols = ['!', '@', '#', '$', '%', '&']
    
    password = ""
    while max> 0:
        random_letter = random.randint(0, 25)
        password += char_list[random_letter]
        random_upper_letter = random.randint(0, 25)
        password += upper_char[random_upper_letter]
        password += str(random.randint(0,9))
        random_symbol = random.randint(0,5)
        password += symbols[random_symbol]
        max = max - 4
    return password

def store_password(name, password):
    f = open("password.txt", "a")
    f.write(name + ", " + password + "\n")
    f.close()
    

def open_passwords():
    f = open("password.txt", "r")
    passwords = {}
    for line in f: 
        hi = line.split(", ")
        passwords[hi[0]] = hi[1]
    return passwords
    

def main():
    max= int(input("How many character would you like your password? "))
    new_password = generate_password(max)
    print(new_password)
    name = input("What was this password for? (Give exact name) ")
    store_password(name, new_password)

    list_passwords = open_passwords()
    find_password = input("What password would you like to look for? " )
    print(list_passwords[find_password])


main()