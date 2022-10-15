
#
try:
    start = int(input("Enter the start of the multiplication range: "))
    end = int(input("Enter the end of the multiplication range: "))
    print("========================================Multiplication table=========================================")


    for i in range(start,end+1):
        for j in range(10+1):

            if i >0 and j>0 :
                print(f"{i}*{j}={int(i * j)}  ", end="")
            else:
                print(" ", end=" ")


        print()

    print("====================================================================================================")


except Exception as ex:
    print(ex)