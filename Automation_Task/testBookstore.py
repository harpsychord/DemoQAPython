# To run this, use the command:
# pytest -v --driver Firefox testBookstore.py

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.profilePage import ProfilePage
from Pages.loginPage import LoginPage
from Pages.bookstorePage import BookstorePage
from Pages.bookDetailsPage import BookDetailsPage

# Unified login function to reduce code.
def login(selenium):
    username = "quality"
    password = "Password#123"

    loginPage = LoginPage(selenium)
    loginPage.navigate()
    loginPage.login(username, password)

@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(5)
    selenium.maximize_window()
    selenium.get('https://demoqa.com/')
    return selenium

# Test 1 - Login
# While not logged in.
def testLoginNotice(selenium):

    # If I access the profile page while not logged in.
    profilePage = ProfilePage(selenium)
    profilePage.navigate()

    # I should get text telling me to login or register.
    notLogged = profilePage.notLoggedInText()
    pytest.assume(notLogged.text == "Currently you are not logged into the Book Store application, please visit the login page to enter or register page to register yourself.")

# Test 2 - Bookstore List
def testBookstoreList(selenium):
    # Given that we login.
    login(selenium)

    # We see a header with our username.
    profilePage = ProfilePage(selenium)
    pytest.assume(profilePage.loggedUserHeader() == "quality")

    # And a list of books, along with our first book.
    pytest.assume(profilePage.getBookTitle(1) == "Git Pocket Guide")

# Test 3 - Bookstore add to collection
def testAddBook(selenium):

    bookToAdd = "Learning JavaScript Design Patterns"

    # Given that we login.
    login(selenium)

    # Check profile page for our book.
    profilePage = ProfilePage(selenium)
    if profilePage.getBookTitle(2) == bookToAdd:
        # We need to delete this book if it already exists in order to continue testing.
        profilePage.deleteBook(2)

    # Given the user is presented with a list of books
    bookstorePage = BookstorePage(selenium)
    bookstorePage.navigate()

    # When the user drills into a book from the list and clicks Add To Your Collection
    # Then the user receives an alert validating the action has been taken
    bookstorePage.navigateToBook(bookToAdd)

    bookDetailsPage = BookDetailsPage(selenium)
    pytest.assume(bookDetailsPage.getTitle() == bookToAdd)
    pytest.assume(bookDetailsPage.addBook() == "Book added to your collection.")

# Test 4 - Profile
def testVerifyProfile(selenium):

    # Given the user is logged in
    login(selenium)

    # When the user navigates to https://demoqa.com/profile
    profilePage = ProfilePage(selenium)
    profilePage.navigate()

    # Then the user should see the seeded book (Git) and the recently added book(s)
    pytest.assume(profilePage.getBookTitle(1) == "Git Pocket Guide")
    pytest.assume(profilePage.getBookTitle(2) == "Learning JavaScript Design Patterns")

# Test 5 - Logout
def testLogout(selenium):

    loginPage = LoginPage(selenium)
    
    # Given the user is logged in
    login(selenium)

    # When the user clicks Log out
    loginPage.logout()

    # Then the user should be redirected to https://demoqa.com/login
    pytest.assume(selenium.current_url == "https://demoqa.com/login")
