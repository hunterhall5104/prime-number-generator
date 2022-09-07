#Prime numbers up to x
num = int(input("Input max number: "))
lst_of_primes = [1, ]
prime = True
for x in range(2, num):
    for i in range(2, x):
        if (x % i) == 0:
            prime = False
            break
    if prime:
        lst_of_primes.append(x)
    prime = True
print(lst_of_primes)
