# Write a function book_info that requires title and author as keyword arguments but also
# accepts optional keyword arguments like year and genre. The function should print the book
# information, including the title, author, and any provided optional details.

def book_info(**kwargs):
    print("book information")
    for key,value in kwargs.items():
        print(key,":",value)


book_info(title="A Time to Kill",author="Adil sial",year=2015,genre="Historical")