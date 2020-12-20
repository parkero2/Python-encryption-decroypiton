def decrypt():
    alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " ", ".", ",", "!"]
    input_message = input("Enter a message to be encrypted. ")
    input_message_array = []
    output_message_array = []

    for i in range(len(input_message)):
        input_message_array.append(input_message[i].lower())
    print(input_message_array)

    # Check all the letters in the message are valid and accepted
    for y in range(len(input_message_array)):
        if input_message_array[y] not in alph:
            print("Character {} is not in my alphabet!".format(input_message_array[y]))

    try:
        encrypt_by = int(input("How many letters to decrypt by?")) * -1
    except ValueError:
        print("Invalid number!")
        encrypt()

    for enc in range(len(input_message_array)):
        letter_location = alph.index(input_message_array[enc])
        if letter_location + encrypt_by < len(alph):
            output_message_array.append(alph[letter_location + encrypt_by])
        else:
            output_message_array.append(alph[letter_location + encrypt_by - len(alph)])
    output_message = ''.join(output_message_array)
    print("Final message: {}".format(output_message))