import encrypt, decrpyt


def menu():
    enc_or_dec = input("Press E for encryption, or D for decryption. ")
    if enc_or_dec.upper() == "E":
        encrypt.encrypt()
    elif enc_or_dec.upper() == "D":
        decrpyt.decrypt()
    else:
        print("Not a valid choice.")
    menu()


menu()

