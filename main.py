
#
try:
    start=int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range:"))
    counter = 0
    even=[]
    odd=[]


    for i in range(start,end+1):
        counter = 0
        if i == 1:

            continue
        for j in range(1,i+1):
            if i % j ==0:
                counter+=1
        if counter !=2:
            odd.append(i)
        if counter ==2:
            even.append(i)
    print(f"Composite numbers: {even}")
    print(f"Simple numbers: {odd}")



except Exception as ex:
    print(ex)