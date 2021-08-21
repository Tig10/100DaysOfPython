# Write your code below this line 👇

def prime_checker(number):
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime:
        print(f'It\'s a prime number.')
    else:
        print(f'It\'s not a prime number.')


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
