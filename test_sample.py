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
    # Create the Remote WebDriver with the specified capabilities
    driver = webdriver.Remote(command_executor=base_url, capabilities=capabilities)
    

    # Add teardown code to close the browser after the test is done
    def fin():
        driver.quit()
    request.addfinalizer(fin)

    return driver

# Your test function using the driver fixture
def test_example(driver):
    # Your test code using the driver fixture
    driver.get('https://example.com')
    assert "Example Domain" in driver.title
