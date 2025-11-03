class Book_Menu:

    def __init__(self, title,author, year, rating):
        self.title = title
        self.author = author 
        self.year = year 
        self.rating = rating 

    def menu_header():
        print(f'{"Title":<20}{"Author":<15}{"Year":^10}{"Rating":>10}')

    def content(book_list):
        for book in book_list:
            print(f"{book.title:<20}{book.author:<15}{book.year:^10}{book.rating:>10}")
        


title_info = ["Python Programming","Learning Python"]
author_info = ["Jack Doe","Jane Doe"]
year_info = [2018, 2019]
rating_info = [4.5, 4.7]

user_info = [Book_Menu(title_info[0],author_info[0],year_info[0],rating_info[0]),
             Book_Menu(title_info[1],author_info[1],year_info[1],rating_info[1])
             ]

Book_Menu.menu_header()
Book_Menu.content(user_info)

