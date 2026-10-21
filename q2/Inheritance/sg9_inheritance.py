class Publication: # initializing publication class w/ title and author
    def __init__(self, title: str, author: str): 
        self.title = title
        self.author = author

    def get_title(self): # returns the title of publication
        return self.title

    def get_author(self): # returns the author of publication
        return self.author

    def set_title(self, title: str): # sets title of publication
        self.title = title

    def set_author(self, author: str): # sets author of publication
        self.author = author

    def display_info(self): # displays title and author by printing
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

class Book: # initializing book class w/ past attributes + number of pages
    def __init__(self, title: str, author: str, number_of_pages: int):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages

    def get_number_of_pages(self): # returns number of pages in book
        return self.number_of_pages

    def set_number_of_pages(self, number_of_pages: int): # sets number of pages in book, with checking if value is positive
        if number_of_pages > 0:
            self.number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive")

    def display_info(self): # prints title, author, and number of pages
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Number of Pages: {self.number_of_pages}")

class Magazine: # initializing magazine class w/ past attributes + issue number
    def __init__(self, title: str, author: str, issue_number: int):
        self.title = title
        self.author = author
        self.issue_number = issue_number

    def get_issue_number(self): # returns issue number of magazine
        return self.issue_number

    def set_issue_number(self, issue_number: int): # sets issue number of magazine, checking if value is positive
        if issue_number > 0:
            self.issue_number = issue_number
        else:
            print("The issue number must be positive")

    def display_info(self): # prints title, author, and issue number
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Issue Number: {self.issue_number}")

if __name__ == "__main__": # main execution

    # instances of Publication, Book, and Magazine
    pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
    mag1 = Magazine("National Geographic", "Various Authors", 202)

    # display information for each instance

    print("Publication Information:")
    pub1.display_info()

    print("\nBook Information:")
    book1.set_number_of_pages(-310)
    book1.display_info()

    print("\nMagazine Information:")
    mag1.display_info()