# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# DATA STRUCTURES AND ALGORITHMS
# ASSIGNMENT NO. 1
# PROGRAMMED BY: Nikka Pauline D. Generalao
# BSCOE 2-2

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

#array
my_arr = [8, 18, 3, 12, 86, 31, 20, 7, 29, 36]

#designs
bakod = ("-")

#start menu
def menu():
    print("\n************************* WELCOME TO ARRAYVERSE **************************\n")
    print(" "*8, bakod*56,
      "\n         Array of the day: ", my_arr, "\n",
      " "*7, bakod*56)
    print("\nNow, what would you like to do?\n\n"
        "(1) -> Add an element \n"
        "(2) -> Insert an element \n"
        "(3) -> Modify an element \n"
        "(4) -> Delete an element \n"
        "(5) -> Arrange in ascending order \n"
        "(6) -> Arrange in descending order \n"
        "(7) -> Exit \n")

#add
def add():

    print("\n****************************** Add An Item *******************************\n")
    my_arr.append(int(input("Enter the element you want to add: ")))

#insert
def insert():

    print("\n***************************** Insert An Item ******************************\n")

    ins_arr = int(input("Enter the index number of the element you want to insert: "))

    if ins_arr < len(my_arr) and ins_arr >= 0:
        if ins_arr == 0:
            element = int(input("Enter the element: "))
            my_arr.insert(ins_arr, element)
            print("\nThe element has been inserted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif ins_arr == 1:
            element = int(input("Enter the element: "))
            my_arr.insert(ins_arr, element)
            print("\nThe element has been inserted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif ins_arr == 2:
            element = int(input("Enter the element: "))
            my_arr.insert(ins_arr, element)
            print("\nThe element has been inserted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif ins_arr == 3:
            element = int(input("Enter the element: "))
            my_arr.insert(ins_arr, element)
            print("\nThe element has been inserted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif ins_arr == 4:
            element = int(input("Enter the element: "))
            my_arr.insert(ins_arr, element)
            print("\nThe element has been inserted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif ins_arr == 5:
            element = int(input("Enter the element: "))
            my_arr.insert(ins_arr, element)
            print("\nThe element has been inserted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif ins_arr == 6:
            element = int(input("Enter the element: "))
            my_arr.insert(ins_arr, element)
            print("\nThe element has been inserted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif ins_arr == 7:
            element = int(input("Enter the element: "))
            my_arr.insert(ins_arr, element)
            print("\nThe element has been inserted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif ins_arr == 8:
            element = int(input("Enter the element: "))
            my_arr.insert(ins_arr, element)
            print("\nThe element has been inserted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif ins_arr == 9:
            element = int(input("Enter the element: "))
            my_arr.insert(ins_arr, element)
            print("\nThe element has been inserted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

    else:
        print("\n", " " * 7, bakod * 56,
              "\n                     PLEASE ENTER A NUMBER FROM 0-9\n",
              " " * 7, bakod * 56)

#modify
def modify():

    print("\n***************************** Modify An Item ******************************\n")
    mod_arr = int(input("Enter the index number of the element you want to modify: "))

    if mod_arr < len(my_arr) and mod_arr >= 0:
        if mod_arr == 0:
            my_arr[0] = int(input("Enter the element: "))
            print("\nThe element has been modified!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif mod_arr == 1:
            my_arr[1] = int(input("Enter the element: "))
            print("\nThe element has been modified!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif mod_arr == 2:
            my_arr[2] = int(input("Enter the element: "))
            print("\nThe element has been modified!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif mod_arr == 3:
            my_arr[3] = int(input("Enter the element: "))
            print("\nThe element has been modified!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif mod_arr == 4:
            my_arr[4] = int(input("Enter the element: "))
            print("\nThe element has been modified!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif mod_arr == 5:
            my_arr[5] = int(input("Enter the element: "))
            print("\nThe element has been modified!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif mod_arr == 6:
            my_arr[6] = int(input("Enter the element: "))
            print("\nThe element has been modified!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif mod_arr == 7:
            my_arr[7] = int(input("Enter the element: "))
            print("\nThe element has been modified!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif mod_arr == 8:
            my_arr[8] = int(input("Enter the element: "))
            print("\nThe element has been modified!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif mod_arr == 9:
            my_arr[9] = int(input("Enter the element: "))
            print("\nThe element has been modified!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

    else:
        print("\n", " " * 7, bakod * 56,
              "\n                     PLEASE ENTER A NUMBER FROM 0-9\n",
              " " * 7, bakod * 56)

#delete
def delete():

    print("\n***************************** Delete An Item ***************************\n")
    del_arr = int(input("Enter the index number of the element you want to delete: "))

    if del_arr < len(my_arr) and del_arr >= 0:

        if del_arr == 0:
            my_arr.remove(8)
            print("\nThe element has been deleted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif del_arr == 1:
            my_arr.remove(18)
            print("\nThe element has been deleted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif del_arr == 2:
            my_arr.remove(3)
            print("\nThe element has been deleted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif del_arr == 3:
            my_arr.remove(12)
            print("\nThe element has been deleted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif del_arr == 4:
            my_arr.remove(86)
            print("\nThe element has been deleted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif del_arr == 5:
            my_arr.remove(31)
            print("\nThe element has been deleted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif del_arr == 6:
            my_arr.remove(20)
            print("\nThe element has been deleted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif del_arr == 7:
            my_arr.remove(7)
            print("\nThe element has been deleted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif del_arr == 8:
            my_arr.remove(29)
            print("\nThe element has been deleted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif del_arr == 9:
            my_arr.remove(36)
            print("\nThe element has been deleted!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

    else:
        print("\n", " " * 7, bakod * 56,
              "\n                     PLEASE ENTER A NUMBER FROM 0-9\n",
              " " * 7, bakod * 56)

#ascending
def ascend():

    print("\n********************** Arrange In Ascending Order **********************\n")

    my_arr.sort(reverse=False)

#descending
def descend():

    print("\n********************** Arrange In Descending Order *********************\n")

    my_arr.sort(reverse=True)

#program
while True:
    menu()

    opt = input("Choose an option: ")
    if opt in ("1", "2", "3", "4", "5", "6", "7"):

        if opt == "1":
            add()
            print("\nThe element has been added!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif opt == "2":
            insert()

        elif opt == "3":
            modify()

        elif opt == "4":
            delete()

        elif opt == "5":
            ascend()
            print("The element has been arranged!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif opt == "6":
            descend()
            print("The element has been arranged!\n",
                  bakod * 65, "\nNew array of the day: ", my_arr, "\n",
                  bakod * 65)

        elif opt == "7":
            print("\n"," " * 7, bakod * 56,
                  "\n                     THANKS FOR USING THIS PROGRAM!!! <3\n",
                  " " * 7, bakod * 56)
            exit()

    else:
        print("\n", " " * 7, bakod * 58,
              "\n         Invalid character! Enter a number from the selection (1-7)\n",
              " " * 7, bakod * 58)

    ans = input("\nDo you want to try again? (y/n): ")
    if ans == "y":
        menu()
    else:
        print("\n", " " * 7, bakod * 56,
              "\n                     THANKS FOR USING THIS PROGRAM!! <3\n",
              " " * 7, bakod * 56)
        break

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-