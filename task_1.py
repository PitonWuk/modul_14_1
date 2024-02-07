"""
1. Напишіть програму, яка приймає два цілих числа від
користувача і виводить суму діапазону чисел між ними.
"""

start = int(input("Enter first number: "))
end = int(input("Enter second number: "))
sum = 0

for num in range(start + 1, end):
    sum += num

print("Sum is", start, "and", end, "=", sum)

"""
2. Напишіть програму, для знаходження суми всіх парних
чисел від 1 до 100.
"""

sum = 0
for num in range(2, 101, 2):
    sum += num

print("Sum =", sum)

"""
3. Напишіть програму, яка приймає рядок від користувача і
виводить кожну літеру рядка на окремому рядку.
"""
str = input("Enter the string: ")
for i in str:
    print(i)

"""
4. Напишіть програму, яка створює список цілих чисел та
виводить новий список, який містить лише парні числа з
вихідного списку.
"""
def numbers(list):
    even_numbers = [num for num in list if num % 2 == 0]
    return even_numbers

def main():
    list = [5, 2, 23, 4, 56, 6, 27, 8, 14, 114]
    print("List:", list)

    even_numbers = numbers(list)

    print("Even numbers:", even_numbers)

main()

"""
5. Напишіть функцію, яка приймає список рядків від
користувача і повертає новий список, що містить лише
рядки, що починаються з великої літери.
"""
def filter_capitalized_strings(string_list):
    capitalized_strings = [string for string in string_list if string[0].isupper()]
    return capitalized_strings

def main():
    input_strings = []
    while True:
        string = input("Enter the string or press Enter to continue: ")
        if string == "":
            break
        input_strings.append(string)

    filtered_strings = filter_capitalized_strings(input_strings)

    print("List of Capitalized strings:", filtered_strings)

main()

"""
6. Напишіть функцію, яка приймає список рядків від
користувача і повертає новий список, що містить лише
рядки, які містять слово "Python".
"""

def filter_python_strings(string_list):
    python_strings = [string for string in string_list if "Python" in string]
    return python_strings


def main():
    input_strings = []
    while True:
        string = input("Enter the string or press Enter to continue: ")
        if string == "":
            break
        input_strings.append(string)

    python_strings = filter_python_strings(input_strings)

    if python_strings:
        print("List with 'Python':", python_strings)
    else:
        print("Nothing....")

main()

"""
7. (додаткове на кристалики)Напишіть програму, яка
створює словник, де ключами є слова, а значеннями - їхні
визначення. Дозвольте користувачу додавати, видаляти
та шукати слова у цьому словнику.
"""
def add_word(dictionary):
    word = input("Enter the word: ")
    definition = input("Enter the definition: ")
    dictionary[word] = definition
    print("Added to dictionary.")

def delete_word(dictionary):
    word = input("Enter the word for delete: ")
    if word in dictionary:
        del dictionary[word]
        print("Deleted.")
    else:
        print("Word did not find.")

def search_word(dictionary):
    word = input("Enter the word you want to search for: ")
    if word in dictionary:
        print("Definition of the word '{}': {}".format(word, dictionary[word]))
    else:
        print("Word not found in the dictionary.")

def main():
    dictionary = {}

    while True:
        print("\nSelect an action:")
        print("1. Add a word and its definition")
        print("2. Delete a word")
        print("3. Find a word")
        print("4. Show the entire dictionary")
        print("5. Exit the program")

        choice = input("Enter the number: ")

        if choice == "1":
            add_word(dictionary)
        elif choice == "2":
            delete_word(dictionary)
        elif choice == "3":
            search_word(dictionary)
        elif choice == "4":
            print("Dictionary:", dictionary)
        elif choice == "5":
            print("The end.")
            break
        else:
            print("Try again.")

main()




"""
Частина 2: Об'єктно-орієнтоване програмування (ООП)

Симулятор роботи сайту

WebSite: Основний клас, який представляє вебсайт.
Атрибути: назва сайту, URL, список сторінок.
Методи: додавання/видалення сторінок, відображення
інформації про сайт.
WebPage: Клас, який представляє окрему сторінку на сайті.
Атрибути: заголовок сторінки, вміст, дата публікації.
Методи: відображення деталей сторінки.
Реалізація функціональності:
Дозвольте користувачеві створювати новий сайт з
певною назвою та URL. Додайте можливість створювати нові
сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
функцію для видалення сторінок з сайту. Включіть функцію
для відображення всієї інформації про сайт, включаючи
список усіх сторінок.
Розробіть простий текстовий інтерфейс для взаємодії з
користувачем. Користувач повинен мати змогу вибирати дії,
такі як створення сайту, додавання/видалення сторінок,
перегляд інформації про сайт.
"""
class WebPage:
    def __init__(self, title, content, publication_date):
        self.title = title
        self.content = content
        self.publication_date = publication_date

    def display_details(self):
        print("Title:", self.title)
        print("Content:", self.content)
        print("Publication Date:", self.publication_date)
        print()

class WebSite:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)

    def remove_page(self, title):
        self.pages = [page for page in self.pages if page.title != title]

    def display_info(self):
        print("Website Name:", self.name)
        print("URL:", self.url)
        print("Pages:")
        for page in self.pages:
            page.display_details()

def create_website():
    name = input("Enter website name: ")
    url = input("Enter website URL: ")
    return WebSite(name, url)

def create_page():
    title = input("Enter page title: ")
    content = input("Enter page content: ")
    publication_date = input("Enter publication date: ")
    return WebPage(title, content, publication_date)

def main():
    website = None
    while True:
        print("\nChoose an action:")
        print("1. Create website")
        print("2. Add page")
        print("3. Remove page")
        print("4. Display website info")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            website = create_website()
        elif choice == "2":
            if website:
                page = create_page()
                website.add_page(page)
                print("Page added successfully.")
            else:
                print("Create a website first.")
        elif choice == "3":
            if website:
                title = input("Enter page title to remove: ")
                website.remove_page(title)
                print("Page removed successfully.")
            else:
                print("Create a website first.")
        elif choice == "4":
            if website:
                website.display_info()
            else:
                print("Create a website first.")
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()


