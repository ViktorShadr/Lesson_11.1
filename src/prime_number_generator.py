def primes():
    """Генератор, который генерирует последовательность простых чисел."""
    n = 2
    prime_list = []
    while True:
        if all(n % prime != 0 for prime in prime_list):
            yield n
            prime_list.append(n)
        n += 1


p = primes()
for i in range(10):
    print(next(p))