# print("Press A to add a book:")
# print("Press M to modify the number of pages of a book:")
# print("Press L to print the number of pages of a book:")
# print("Press P to Print out all books’ titles with their authors and the number of pages:")
# print("Press Q to quit:")

# books = {
#   "book1": {"author": "Ella",
#             "pages": "200"},
#     "book2": {"author": "Lily",
#             "pages": "5"},
#     "book3": {"author": "Dayna",
#             "pages": "420"},
#     "book4": {"author": "Kistina",
#             "pages": "69"},
# }
# print(books)

books = []

quit = True

while quit == True:
  menu = input("Press A to add a book:\n Press M to modify the number of pages of a book: \n Press L to print the number of pages of a book: \n Press P to Print out all books’ titles with their authors and the number of pages: \n Press Q to quit:\n")
  if menu == "A":
    new_book = input("What is the name of the book?")
    author = input("Who is the author of the book?")
    pages = input("How many pages does the book have?")
    books.append(new_book)
    books.append(author)
    books.append(pages)
    
  elif menu == "M":
    print("yo")
  elif menu == "L":
    print("Kia ora")
  elif menu == "P":
    print(books)
  elif menu == "Q":
    quit = False

