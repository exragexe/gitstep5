
#
try:
    dovzh = int(input("Enter the number of lines in length: "))
    shir = int(input("Enter the number of rows in width: "))
    print("========================================Multiplication table=========================================")


    for i in range(dovzh+1):
        for j in range(shir+1):

            if i > 0 and j > 0:
                print(f"{i}*{j}={int(i * j)}  ", end="")
            else:
                print(" ", end=" ")


        print()

    print("====================================================================================================")


except Exception as ex:
    print(ex)