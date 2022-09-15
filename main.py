# Ella Thomas
# 5/09/2022
# Book store project 

books = []

def add_book():
  new_book = input("What is the name of the book?")
  author = input("Who is the author of the book?")
  pages = input("How many pages does the book have?")
  books.append(new_book)
  books.append(author)
  books.append(pages)


def main():
  quit = True
  while quit == True:
    menu = input("Press A to add a book:\n Press M to modify the number of pages of a book: \n Press L to print the number of pages of a book: \n Press P to Print out all books’ titles with their authors and the number of pages: \n Press Q to quit:\n")
    if menu == "A":
      add_book()
      
    elif menu == "M":
      books[2] = input("What is the new number of pages?")
      print(books)
    elif menu == "L":
      print("Kia ora")
    elif menu == "P":
      print(books)
    elif menu == "Q":
      quit = False

main()

