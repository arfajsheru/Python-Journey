# nouber of occrences 


def number_of_occ():
    try:
        list_size = int(input("Enter the length of your number list: "))
        if list_size <= 0:
            print("Please enter a positive number for list length.")
            return
    except ValueError:
        print("Please enter a valid integer for list length.")
        return
    mylist = []
    for i in range(1, list_size + 1):
        num = int(input(f"Enter your number {i}: "))
        mylist.append(num)
    
    num = int(input("Enter your find number in list: "))
    occ = 0
    for i in mylist:
        if i == num:
            occ +=1
    
    print(f"The number {num} appears {occ} time(s) in the list.")

number_of_occ()