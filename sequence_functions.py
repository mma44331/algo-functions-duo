def fibonnacci(num):
    if num < 1:
        print('erreur is not a valid number')
        return
    if num == 1:
        return [1]
    if num == 2:
        return [1,1]
    fib=[1,1]
    for i in range(2,num):
        fib.append(fib[-2]+fib[-1])
    return fib

        


   


    

print(fibonnacci(7))