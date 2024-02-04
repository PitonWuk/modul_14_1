"""
Завдання 2
Користувач вводить з клавіатури шлях до файлу. Після
чого запускаються три потоки. Перший потік заповнює файл
випадковими числами. Два інші потоки очікують на заповнення. Коли файл заповнений, обидва потоки стартують.
Перший потік знаходить усі прості числа, другий потік знаходить факторіал кожного числа у файлі. Результати пошуку
кожен потік має записати у новий файл. Виведіть на екран
статистику виконаних операцій.

"""

import threading
import random
import math


class FileFillerThread(threading.Thread):
    def __init__(self, filename, size):
        super().__init__()
        self.filename = filename
        self.size = size

    def run(self):
        with open(self.filename, 'w') as file:
            for _ in range(self.size):
                file.write(str(random.randint(1, 100)) + '\n')
        print("File filled:", self.filename)


class PrimeNumbersThread(threading.Thread):
    def __init__(self, input_filename, output_filename):
        super().__init__()
        self.input_filename = input_filename
        self.output_filename = output_filename

    def is_prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def run(self):
        primes = []
        with open(self.input_filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                if self.is_prime(number):
                    primes.append(number)
        with open(self.output_filename, 'w') as file:
            for prime in primes:
                file.write(str(prime) + '\n')
        print("Prime numbers written to:", self.output_filename)


class FactorialThread(threading.Thread):
    def __init__(self, input_filename, output_filename):
        super().__init__()
        self.input_filename = input_filename
        self.output_filename = output_filename

    def run(self):
        with open(self.input_filename, 'r') as infile, open(self.output_filename, 'w') as outfile:
            for line in infile:
                number = int(line.strip())
                factorial = math.factorial(number)
                outfile.write(str(factorial) + '\n')
        print("Factorials written to:", self.output_filename)


def main():
    input_filename = input("Enter the path to the input file: ")
    output_prime_filename = "prime_numbers.txt"
    output_factorial_filename = "factorials.txt"
    size = 10

    filler_thread = FileFillerThread(input_filename, size)
    prime_thread = PrimeNumbersThread(input_filename, output_prime_filename)
    factorial_thread = FactorialThread(input_filename, output_factorial_filename)

    filler_thread.start()

    # Wait for file to be filled
    filler_thread.join()

    # Start prime and factorial threads
    prime_thread.start()
    factorial_thread.start()

    # Wait for prime and factorial threads to finish
    prime_thread.join()
    factorial_thread.join()

    print("Operations completed.")


main()
