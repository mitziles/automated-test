from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def get_driver(context):
    return context.driver

def check_error(driver):
    try:
        password_error = driver.find_element(By.XPATH, "//div[@class='Ly8vae uSvLId']")
        if password_error.is_displayed():
            return True
    except NoSuchElementException:
        pass

    try:
        login_error = driver.find_element(By.XPATH, "//div[@class='Ekjuhf Jj6Lae']")
        if login_error.is_displayed():
            return True
    except NoSuchElementException:
        pass

    return False 

@given('User opens login page')
def step_given_login(context):
    options = Options()
    options.headless = False 

    service = Service("geckodriver.exe")
    context.driver = webdriver.Firefox(service=service, options=options)

    url = "https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=1&emr=1&flowEntry=ServiceLogin&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=AXH0vVuZTiMRH5RaP01-HLdooKff46UU1GnmGsMt9oEabAtJwb7Z50_Lut-VpH6xAZYWWMcBTPQLYQ&osid=1&passive=1209600&service=mail"
    context.driver.get(url)

@when('Introduce credentials with username "{email}" and password "{password}"')
def step_credentials(context, email, password):
    driver = get_driver(context)
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='email']")))
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email)
    driver.find_element(By.XPATH, "//button[span[text()='Next']]").click()

    if check_error(driver):
        driver.quit()
        return

    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='password']")))
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[span[text()='Next']]").click()

    if check_error(driver):
        driver.quit()
        return

@then('Login successful')
def step_successful(context):
    driver = get_driver(context)
    wait = WebDriverWait(driver, 10)

    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Compose']")))
        button = driver.find_element(By.XPATH, "//div[text()='Compose']")
        assert button.is_displayed()
        print("Login reușit!")
    except Exception as e:
        print(f"Eroare la login: {e}")
    
    driver.quit()
