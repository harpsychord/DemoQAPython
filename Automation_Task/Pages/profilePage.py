import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:
    def __init__(self, selenium):
        self.selenium = selenium

    # Page objects
    def notLoggedInText(self):
        return self.selenium.find_element(By.ID, "notLoggin-label")

    def loggedUserHeader(self):
        return self.selenium.find_element(By.ID, "userName-value").text
    
    def bookList(self):
        return self.selenium.find_elements(By.CLASS_NAME, "rt-tr-group")

    def getBookTitle(self, bookNumber):
        return self.bookList()[bookNumber-1].find_elements(By.CLASS_NAME, "rt-td")[1].text
    
    def getBookDeleteButton(self, bookNumber):
        return self.bookList()[bookNumber-1].find_elements(By.CLASS_NAME, "rt-td")[4].find_element(By.ID, "delete-record-undefined")

    # Page functions
    def navigate(self):
        self.selenium.get('https://demoqa.com/profile')

    def deleteBook(self, bookNumber):
        self.getBookDeleteButton(bookNumber).click()
        
        # Wait for verification modal to appear.
        element = WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.ID, "closeSmallModal-ok"))
        )

        # Click the OK button.
        self.selenium.find_element(By.ID, "closeSmallModal-ok").click()

        # Wait for the alert.
        time.sleep(2)
        alert = self.selenium.switch_to.alert
        alertText = alert.text

        # Click alert.
        alert.accept()
        return alertText