from selenium import webdriver
from selenium.webdriver.common.by import By

def test_scores_service(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        score_element = driver.find_element(By.ID, "score")
        score = int(score_element.text)
        return 1 <= score <= 1000
    except Exception as e:
        print(f"Test failed: {e}")
        return False
    finally:
        driver.quit()

def main_function():
    url = "http://localhost:8777"
    test_result = test_scores_service(url)
    if test_result:
        print("Test passed!")
        exit(0)
    else:
        print("Test failed!")
        exit(-1)