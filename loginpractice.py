import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin(unittest.TestCase): #Test Scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self): #Test Case 1
        driver = self.browser
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.CSS_SELECTOR,"button#submit.btn").click()

        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,"h1.post-title").text
        response_data2 = driver.find_element(By.CSS_SELECTOR,"p.has-text-align-center").text

        self.assertIn('Logged In Successfully', response_data)
        self.assertIn('Congratulations student. You successfully logged in!', response_data2)

    def test_failed_login_wrong_password(self): #Test Case 2
        driver = self.browser
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("passwordsalah")
        driver.find_element(By.CSS_SELECTOR,"button#submit.btn").click()

        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,"div#error.show").text

        self.assertIn('Your password is invalid!', response_data)
    
    def test_failed_login_wrong_username(self): #Test Case 3
        driver = self.browser
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.find_element(By.ID, "username").send_keys("Muhammad Nur Huda")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.CSS_SELECTOR,"button#submit.btn").click()

        # validasi
        response_data = driver.find_element(By.CSS_SELECTOR,"div#error.show").text

        self.assertIn('Your username is invalid!', response_data)

    
if __name__ == '__main__':
    unittest.main()