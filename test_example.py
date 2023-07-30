# test_example.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture
def driver(request):
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--version')
    platform = request.config.getoption('--platform')
    
    capabilities = {
        "browserName": browser,
        "version": version,
        "platform": platform,
        "selenium:options": {
            "debugConnectToRunningApp": True,
            "browserName": browser,
        }
    }
    
    driver = webdriver.Remote(
        command_executor='http://a9a62f8fea028418b89cc1c7fae3c67f-808020604.us-east-1.elb.amazonaws.com:4444/wd/hub',
        desired_capabilities=capabilities
    )
    
    yield driver
    driver.quit()

def test_example(driver):
    driver.get("https://example.com")
    assert driver.title == "Example Domain"

    # Interaction with web elements
    search_input = driver.find_element_by_name("q")
    search_input.send_keys("GitHub Actions")
    search_input.submit()

    # Verify search results
    search_results = driver.find_elements_by_css_selector("h3")
    assert len(search_results) > 0

    # Print search results titles
    for result in search_results:
        print(result.text)

