

path = r"C:\Users\Arfaj sheru\OneDrive\Desktop\Python-journey\Lecture 07 File Input-Output in python\PractiseSet\practice.txt"
# f = open(path, "a")
# f.write("Hii everyone\nwe are learning File I/O\nusing java\nI like Programming java\n\n\n")
# f.close
# with open(path,"r")as f:
#     # f.write("Hii everyone\nwe are learning File I/O\nusing java\nI like Programming java\n\n\n")
#     data = f.read()
#     new_data = data.replace("java","python")
#     print(new_data)

# with open(path,"w")as f:
#     f.write(new_data)

def check_for_word():
    word = "python"
    with open(path, "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print(f"{word} is found in data")
        else: 
            print(f"{word} is not found in data")

# check_for_word()


def check_for_line():
    word = "Hiiiiiiii"
    data = True
    line_no = 1
    with open(path,"r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

# check_for_line()


def find_even_number():
    with open(path,"r") as f:
        data = f.read()
        print(data)
        num = ""
        my_list = []
        # get number
        for i in range(len(data)):
            if(data[i] == ","):
                print(int(num))
                my_list.append(int(num))
                num = ""
            else:
                num += data[i]
        even = 0
        odd = 0
        #Check number is even or odd 
        for i in my_list:
            if(i % 2 == 0):
                print(f"{i}ᴱ", end=" ")
                even += 1   
            else:
                print(f"{i}ᴼ" ,end=" ")
                odd += 1


        print(f"\nEven number {even} times in list")
        print(f"Odd number {odd} times in list")
find_even_number()

            
    


