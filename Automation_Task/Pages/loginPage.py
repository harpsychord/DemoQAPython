import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, selenium):
        self.selenium = selenium

    # Page objects
    def loginUserField(self):
        return self.selenium.find_element(By.ID, "userName")
    
    def loginPassField(self):
        return self.selenium.find_element(By.ID, "password")
    
    def loginButton(self):
        return self.selenium.find_element(By.ID, "login")
    
    def logoutButton(self):
        return self.selenium.find_element(By.XPATH, "//button[contains(text(),'Log out')]")

    # Page functions
    def navigate(self):
        self.selenium.get('https://demoqa.com/login')

    def login(self, username, password):
        self.loginUserField().send_keys(username)
        self.loginPassField().send_keys(password)
        self.loginButton().click()

        # Ensure we have logged in by waiting for a particular element.
        element = WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.ID, "userName-value"))
        )
    
    def logout(self):
        self.logoutButton().click()