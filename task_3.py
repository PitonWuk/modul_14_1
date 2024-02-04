"""
Завдання 3
Користувач вводить з клавіатури шлях до існуючої та
до нової директорії. Після чого запускається потік, який має
скопіювати вміст директорії у нове місце. Збережіть структуру
директорії. Виведіть статистику виконаних операцій на екран.
"""
import threading
import shutil
import os

class DirectoryCopyThread(threading.Thread):
    def __init__(self, source_dir, dest_dir):
        super().__init__()
        self.source_dir = source_dir
        self.dest_dir = dest_dir

    def run(self):
        try:
            shutil.copytree(self.source_dir, self.dest_dir)
            print("Directory copied successfully from", self.source_dir, "to", self.dest_dir)
        except OSError as e:
            print(f"Error: {self.source_dir} -> {self.dest_dir} ({e})")

def main():
    source_dir = input("Enter the path to the source directory: ")
    dest_dir = input("Enter the path to the destination directory: ")

    copy_thread = DirectoryCopyThread(source_dir, dest_dir)
    copy_thread.start()
    copy_thread.join()

    print("Operation completed.")

main()
