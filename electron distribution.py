from mendeleev import *

user_input = element(input("enter element name/symbol: "))
atomic_no_of_input = user_input.atomic_number

while True:
    if atomic_no_of_input <=2:
        print("1s^" + str(atomic_no_of_input))
        break

    if atomic_no_of_input >=3 and atomic_no_of_input <= 38:
        if atomic_no_of_input <=4:
            print("1s^2 2s^" + str(atomic_no_of_input-2))
            break
        elif atomic_no_of_input >4 and atomic_no_of_input <11:
            print("1s^2 2s^2 2p^" + str(atomic_no_of_input-4))
            break
        elif atomic_no_of_input > 10 and atomic_no_of_input < 13:
            print("1s^2 2s^2 2p^6 3s^" + str(atomic_no_of_input-10))
            break
        elif atomic_no_of_input > 12 and atomic_no_of_input <= 18:
            print("1s^2 2s^2 2p^6 3s^2 3p^" + str(atomic_no_of_input-12))
            break
        elif atomic_no_of_input >18 and atomic_no_of_input <=20:
            print("1s^2 2s^2 2p^6 3s^2 3p^6 4s^" + str(atomic_no_of_input - 18))
            break
        elif atomic_no_of_input > 20 and atomic_no_of_input <= 30:
            print("1s^2 2s^2 2p^6 3s^2 3p^6 4s^2 3d^" + str(atomic_no_of_input - 20))
            break
        elif atomic_no_of_input > 30 and atomic_no_of_input <= 36:
            print("1s^2 2s^2 2p^6 3s^2 3p^6 4s^2 3d^10 4p^" + str(atomic_no_of_input - 30))
            break
        elif atomic_no_of_input > 36 and atomic_no_of_input <= 38:
            print("1s^2 2s^2 2p^6 3s^2 3p^6 4s^2 3d^10 4p^6 5s^" + str(atomic_no_of_input - 36))
            break
    else:
        print(f"Sorry, I currently only wrote the code for elements upto atomic number 38, that is strontium. Your current element " + str(user_input) + " is unsupported")
    break