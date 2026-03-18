
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(original_text,shift_amount, user_direction):
    if user_direction == 'encode':
            new=""
            for i in original_text:
                if i.isalpha():
                    ind = alphabet.index(i)
                    ind_n = (ind + shift_amount) % 26
                    new += alphabet[ind_n]
                else:
                    new+=i
            print(new)

    elif user_direction == 'decode':
            new=""
            for i in original_text:
                if i.isalpha():
                    ind = alphabet.index(i)
                    ind_n = (ind - shift_amount) % 26
                    new += alphabet[ind_n]
                else:
                    new+=i
            print(new)
    else:
        print("Invalid choice thank you")
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    choice=input("Do you want to continue? Yes or No: ").lower()
    if choice=='no':
        print("Thank You for using the Caesar Cypher, Goodbye!!")
        break



