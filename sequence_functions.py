def fibonnacci(num):
    arr=[]
    if num==1:
        arr.append(1)
        return arr
    if num==2:
        arr.append(1)
        arr.append(1)
        return arr
    arr.append(1)
    arr.append(1)
    fib_num1=1
    fib_num2=1
    fib_num=0
    for i in range(2,num):
        fib_num = fib_num1 + fib_num2
        fib_num1 = fib_num2
        fib_num2 = fib_num
        arr.append(fib_num)
    return arr    


   


    

print(fibonnacci(1))