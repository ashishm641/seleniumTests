import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestSeleniumGrid(unittest.TestCase):

    def setUp(self):
        # Define the desired capabilities for Chrome
        options = webdriver.ChromeOptions()
        options.browser_name = "chrome"
        options.version = "latest"
        options.platform = "macOS 11.0"
        base_url = "http://a9a62f8fea028418b89cc1c7fae3c67f-808020604.us-east-1.elb.amazonaws.com:4444/ui#/sessions"

        # Create the Remote WebDriver with the specified capabilities
        self.driver = webdriver.Remote(command_executor=base_url, options=options)

    def test_example(self):
        # Your test code goes here
        self.driver.get("http://a9a62f8fea028418b89cc1c7fae3c67f-808020604.us-east-1.elb.amazonaws.com:4444/ui#/sessions")
        assert "Selenium Grid" in self.driver.title
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("admin")
        self.driver.find_element_by_id("submit").click()
        assert "Dashboard" in self.driver.title

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
