import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookstorePage:
    def __init__(self, selenium):
        self.selenium = selenium

    def getTitleLink(self, bookName): 
        return self.selenium.find_element(By.ID, "see-book-"+bookName)

    def navigate(self):
        self.selenium.get('https://demoqa.com/books')

    def navigateToBook(self, bookName):
        bookLink = self.getTitleLink(bookName)
        # Scroll the screen to fully view the element we need to click on to avoid ad overlays.
        self.selenium.execute_script("arguments[0].scrollIntoView();", bookLink)
        bookLink.click()
        element = WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.ID, "title-wrapper"))
        )