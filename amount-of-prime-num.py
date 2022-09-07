# Number of prime numbers
num = int(input("Input number of prime numbers: "))
lst_of_primes = []
prime = True
y = 0
x = 2
while y < num:
    for i in range(2, x):
        if (x % i) == 0:
            prime = False
            break
    if prime:
        y += 1
        lst_of_primes.append(x)
    prime = True
    x += 1
print(lst_of_primes)
