import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin(unittest.TestCase): #Test Scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_contact(self): #Test Case 1
        driver = self.browser
        driver.get("https://practicetestautomation.com/contact/")
        driver.find_element(By.ID, "wpforms-161-field_0").send_keys("Keripik") #nama awal
        driver.find_element(By.ID, "wpforms-161-field_0-last").send_keys("Cabe") #nama akhir
        driver.find_element(By.ID, "wpforms-161-field_1").send_keys("keripikcabe@cabe.com") #email
        driver.find_element(By.ID, "wpforms-161-field_2").send_keys("Keripik cabe adalah makanan yang nikmat") #komen atau pesan
        driver.find_element(By.ID,"wpforms-submit-161").click()

        # validasi
        response_data = driver.find_element(By.ID,"wpforms-confirmation-161").text
        self.assertIn('Thanks for contacting us! We will be in touch with you shortly.', response_data)
            #koding sudah dicek berhasil hanya kalo ada captcha bukan robot dari google hasilnya jadi gagal.

#    def test_failed_contact_empty_email_empty_comment(self): #Test Case 2
#       driver = self.browser
#       driver.get("https://practicetestautomation.com/contact/")
#        driver.find_element(By.ID, "wpforms-161-field_0").send_keys("Harry") #nama awal
#        driver.find_element(By.ID, "wpforms-161-field_0-last").send_keys("Potter") #nama akhir
#        driver.find_element(By.ID, "wpforms-161-field_1").send_keys("") #email
#        driver.find_element(By.ID, "wpforms-161-field_2").send_keys("") #komen atau pesan
#        driver.find_element(By.ID,"wpforms-submit-161").click()

        # validasi
#        response_data = driver.find_element(By.ID,"wpforms-161-field_1-error").getAttribute("This field is required.");
#        self.assertIn('This field is required.', response_data)

if __name__ == '__main__':
    unittest.main()