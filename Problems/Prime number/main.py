num = int(input())
if num <= 1:
    print('This number is not prime')
else:
    i = num - 1
    message = 'This number is prime'
    while i > 1:
        if num % i == 0:
            message = 'This number is not prime'
            break
        else:
            i -= 1
    print(message)
