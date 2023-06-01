import time
import random

def miller_rabin_test(n, k):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def miller_rabin(n, iterations=10):

    if miller_rabin_test(n, iterations):
        print(n,"є простим числом")
        return True
        
    else:
        print(n,"не є простим числом")
        return False
        

    

def brute_method(base, target, modulus):
    start_time = time.time()
    time_limit = 300
    exponent = 0
    result = 0

    while result != target:
        result = (base ** exponent) % modulus
        exponent += 1

        if time.time() - start_time > time_limit:
            raise TimeoutError("Рекомедований час виконання (5 хв) - перевищено")
        
        #print(result)

        
    end_time = time.time()
    execution_time = end_time - start_time
    print("Час виконання: ", execution_time, "сек")
    return exponent 

import time

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

def modular_inverse(a, modulus):
    gcd, x, _ = extended_gcd(a, modulus)
    if gcd == 1:
        return x % modulus
    else:
        raise ValueError("Обернене число не існує")

def silver_polak_hellman(base, target, modulus):
    start_time = time.time()
    time_limit = 300

    x = 1
    exponent = 0
    while x != target:
        x = (x * base) % modulus
        exponent += 1

        if time.time() - start_time > time_limit:
            raise TimeoutError("Рекомендований час виконання (5 хв) - перевищено")

    end_time = time.time()
    execution_time = end_time - start_time
    print("Час виконання: ", execution_time, "сек")
    return exponent


# Введення значень
while True:
    print("Menu:\n\n1. Метод перебору.\n2. Метод СПГ. \n3. Вихід.\n")
    var = int(input("Оберіть метод: "))
    base = int(input("Введіть основу (base): "))
    target = int(input("Введіть ціль (target): "))
    modulus = int(input("Введіть модуль (modulus): "))
    if miller_rabin(modulus):
        if var == 1:
            try:
                exponent = brute_method(base, target, modulus)
                print("Потрібний степінь: ", exponent - 1)
            except TimeoutError:
                print("Час виконання перевищено")
        if var == 2:
            try:
                exponent = silver_polak_hellman(base, target, modulus)
                print("Потрібний степінь: ", exponent)
            except TimeoutError:
                print("Час виконання перевищено")
        if var == 3:
            break
exit()
