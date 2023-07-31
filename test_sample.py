import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver(request):
    # Define the desired capabilities for Chrome
    options = webdriver.ChromeOptions()
    options.browser_name = "chrome"
    options.version = "latest"
    options.platform = "macOS 11.0"
    # The following line will tell Selenium to accept connections to servers that are using self-signed certificates or outdated versions of SSL.
    options.ssl_version = "AUTO"
    base_url = "http://a9a62f8fea028418b89cc1c7fae3c67f-808020604.us-east-1.elb.amazonaws.com:4444/wd/hub"

    # Create the Remote WebDriver with the specified capabilities
    driver = webdriver.Remote(command_executor=base_url, options=options)

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver

def test_example(driver):
    # Your test code goes here
    driver.get("http://a9a62f8fea028418b89cc1c7fae3c67f-808020604.us-east-1.elb.amazonaws.com:4444/ui#/sessions")
    assert "Selenium Grid" in driver.title
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_id("password").send_keys("admin")
    driver.find_element_by_id("submit").click()
    assert "Dashboard" in driver.title

if __name__ == "__main__":
    pytest.main()
