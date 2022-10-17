import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookDetailsPage:
    def __init__(self, selenium):
        self.selenium = selenium

    # Page objects

    def getTitle(self):
        return self.selenium.find_element(By.ID, "title-wrapper").find_element(By.ID, "userName-value").text
    
    def addBookButton(self):
        # Turns out both buttons (Go Back and Add) have this same ID.
        return self.selenium.find_element(By.XPATH, "//button[contains(text(), 'Add To Your Collection')]")

    # Page functions

    def addBook(self):
        self.selenium.execute_script("arguments[0].scrollIntoView();", self.addBookButton())
        self.addBookButton().click()
        
        # Wait for the alert.
        time.sleep(2)
        alert = self.selenium.switch_to.alert
        alertText = alert.text

        # Click alert.
        alert.accept()
        return alertText