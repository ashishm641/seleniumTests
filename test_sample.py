import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver(request):
    # Define the desired capabilities for Selenium Grid
    options = Options()
    options.browser_name = "chrome"
    options.browser_version = "latest"
    options.platform_name = "macOS 11.0"
    base_url = "https://a9a62f8fea028418b89cc1c7fae3c67f-808020604.us-east-1.elb.amazonaws.com:4444/wd/hub"

    # Create the Remote WebDriver with the specified capabilities
    driver = webdriver.Remote(command_executor=base_url, options=options)
    
    def fin():
        driver.quit()
    
    request.addfinalizer(fin)
    return driver

def test_example(driver):
    # Your test code goes here
    driver.get("https://www.example.com")
    assert "Example Domain" in driver.title
