
# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# PawanLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input


class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print('Lender-Book database has been updated. You can take the book now.')
        else:
            print(f'Book is already being used by {self.lendDict[book]}')

    def addBook(self, book):
        self.bookList.append(book)
        print('Book has been added to the book list')

    def returnBook(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    pawan = Library(['python', 'rich daddy poor daddy',
                    'data structure', 'algorithms'], 'vikram vedha')

    while(True):
        print(
            f'Welcome to the {pawan.name} library. Enter your choice to continue')
        print('1.Display Books')
        print('2 lend a Books')
        print('3 add a Books')
        print('4 return a Books')
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print('Please enter a valid option')
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            pawan.displayBooks()

        elif user_choice == 2:
            book = input('enter the name of the book you want to lend:')
            user = input('enter your name')
            pawan.lendBook(user, book)

        elif user_choice == 3:
            book = input('enter the name of the book you want to add')
            pawan.addBook(book)

        elif user_choice == 4:
            book = input('enter the name of the book you want to return')
            pawan.returnBook(book)

        else:
            print('Not a valid option')

        print('Press q to quit and c to continue')
        user_choice2 = ""
        while(user_choice2 != 'c' and user_choice2 != 'q'):
            user_choice2 = input()
            if user_choice2 == 'q':
                exit()

            elif user_choice2 == 'c':
                continue
