"""
Завдання 4
Користувач вводить з клавіатури шлях до існуючої директорії та слово для пошуку. Після чого запускаються два
потоки. Перший потік має знайти файли з потрібним словом
і злити їх вміст в один файл. Другий потік очікує на завершення роботи першого потоку і проводить виключення усіх
заборонених слів (список цих слів потрібно зчитати з файлу
із забороненими словами) з отриманого файлу. Виведіть статистику виконаних операцій на екран.

"""
import threading
import os

class SearchThread(threading.Thread):
    def __init__(self, directory, keyword, output_file):
        super().__init__()
        self.directory = directory
        self.keyword = keyword
        self.output_file = output_file

    def run(self):
        found_files = []
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.endswith(".txt"):  # Пошук лише в текстових файлах
                    filepath = os.path.join(root, file)
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                        if self.keyword in content:
                            found_files.append(filepath)

        with open(self.output_file, "w", encoding="utf-8") as out_file:
            for file in found_files:
                with open(file, "r", encoding="utf-8") as in_file:
                    out_file.write(in_file.read())

        print(f"Found files with keyword '{self.keyword}': {found_files}")
        print(f"Merged content saved to {self.output_file}")

class CensorThread(threading.Thread):
    def __init__(self, input_file, banned_words_file):
        super().__init__()
        self.input_file = input_file
        self.banned_words_file = banned_words_file

    def run(self):
        banned_words = set()
        with open(self.banned_words_file, "r", encoding="utf-8") as f:
            for line in f:
                banned_words.add(line.strip())

        with open(self.input_file, "r+", encoding="utf-8") as f:
            content = f.read()
            for word in banned_words:
                content = content.replace(word, "***")
            f.seek(0)
            f.write(content)
            f.truncate()

        print(f"Censored file saved to {self.input_file}")

def main():
    directory = input("Enter the path to the directory: ")
    keyword = input("Enter the keyword to search: ")
    output_file = "merged_content.txt"
    banned_words_file = "banned_words.txt"

    search_thread = SearchThread(directory, keyword, output_file)
    censor_thread = CensorThread(output_file, banned_words_file)

    search_thread.start()
    search_thread.join()

    censor_thread.start()
    censor_thread.join()

    print("Operations completed.")

main()
