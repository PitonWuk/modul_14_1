"""
Завдання 1
При старті додатку запускаються три потоки. Перший
потік заповнює список випадковими числами. Два інші потоки
очікують на заповнення. Коли перелік заповнений, обидва
потоки запускаються. Перший потік знаходить суму елементів
списку, другий потік знаходить середнє арифметичне значення
у списку. Отриманий список, сума та середнє арифметичне
виводяться на екран.
"""
import threading
import random
import time

class DataFillerThread(threading.Thread):
    def __init__(self, data, size):
        super().__init__()
        self.data = data
        self.size = size

    def run(self):
        for _ in range(self.size):
            self.data.append(random.randint(1, 100))
        print("Data filled:", self.data)

class SumThread(threading.Thread):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def run(self):
        total_sum = sum(self.data)
        print("Sum of elements:", total_sum)

class AverageThread(threading.Thread):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def run(self):
        average = sum(self.data) / len(self.data)
        print("Average of elements:", average)


def main():
    data = []
    size = 10

    filler_thread = DataFillerThread(data, size)
    sum_thread = SumThread(data)
    avg_thread = AverageThread(data)

    filler_thread.start()

    filler_thread.join()

    sum_thread.start()
    avg_thread.start()

    sum_thread.join()
    avg_thread.join()


main()
