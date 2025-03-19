from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver(context):
    return context.driver

@given('User opens login page')
def step_given_login(context):
    # Setezi opțiuni pentru Firefox
    options = Options()
    options.headless = False  # Setezi False pentru a dezactiva headless

    service = Service(GeckoDriverManager().install())
    context.driver = webdriver.Firefox(service=service, options=options)

    url = "https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=1&emr=1&flowEntry=ServiceLogin&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=AXH0vVuZTiMRH5RaP01-HLdooKff46UU1GnmGsMt9oEabAtJwb7Z50_Lut-VpH6xAZYWWMcBTPQLYQ&osid=1&passive=1209600&service=mail"
    context.driver.get(url)

@when('Introduce credentials')
def step_credentials(context):
    driver = get_driver(context)
    wait = WebDriverWait(driver, 10)
    # wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='AsY17b'][1]")))
    # driver.find_element(By.XPATH, "//div[@class='AsY17b'][1]").click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='email']")))
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys("alinpopescovici1234@gmail.com")
    driver.find_element(By.XPATH, "//button[span[text()='Next']]").click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("abcd1234.@")
    driver.find_element(By.XPATH, "//button[span[text()='Next']]").click()

@then('Login successful')
def step_successful(context):
    driver = get_driver(context)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Compose']")))
    button = driver.find_element(By.XPATH, "//div[text()='Compose']")
    assert button.is_displayed()

    driver.quit()
