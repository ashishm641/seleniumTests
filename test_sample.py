import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture
def driver(request):
    # Define the desired capabilities for Selenium Grid
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['browserName'] = 'chrome'
    capabilities['version'] = 'latest'
    capabilities['platform'] = 'macOS 11.0'
    base_url = "https://a9a62f8fea028418b89cc1c7fae3c67f-808020604.us-east-1.elb.amazonaws.com:4444/wd/hub"

    # Create the Remote WebDriver with the specified capabilities
    driver = webdriver.Remote(command_executor=base_url, desired_capabilities=capabilities)
    
    def fin():
        driver.quit()
    
    request.addfinalizer(fin)
    return driver

def test_example(driver):
    # Your test code goes here
    driver.get("https://www.example.com")
    assert "Example Domain" in driver.title
