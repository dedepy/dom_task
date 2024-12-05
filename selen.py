import time

from imports import *
load_dotenv()

#Получение почты и пароля из окружения
mail = os.getenv('mail')
password = os.getenv('password')
#Таймер для поиска элементов
AUTH_TIMEOUT = 120
def login():
    driver = webdriver.Chrome()
    driver.get('https://px6.me/')
    wait = WebDriverWait(driver, AUTH_TIMEOUT)
    enter = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME,'icon-login')))
    enter.click()
    enter_mail = wait.until(
        EC.presence_of_element_located((By.NAME,'email')))
    enter_mail.send_keys(mail)
    enter_password = wait.until(
        EC.presence_of_element_located((By.NAME, 'password')))
    enter_password.send_keys(password)
    time.sleep(30)
    enter_button = wait.until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="form-login"]/div[7]/button')))
    enter_button.click()
    #1 метод
    # prox1 = wait.until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="el-30643198"]/td[3]/ul/li[1]/div[2]')))
    # prox2 = wait.until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="el-30643190"]/td[3]/ul/li[1]/div[2]')))
    # date1 = wait.until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="el-30643198"]/td[4]/ul/li[1]/div[2]')))
    # date2 = wait.until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="el-30643190"]/td[4]/ul/li[1]/div[2]')))
    # print(prox1.text, ' - ', date1.text)
    # print(prox2.text, ' - ', date2.text)
    #2 метод
    prox = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'right.clickselect ')))
    date = wait.until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'right.color-success')))

    pattern = re.compile(r"^\d{1,3}(\.\d{1,3}){3}:\d+$")
    arr = []
    for i in prox:
        arr.append(i.text)
    result = [item for item in arr if pattern.match(item)]
    for i in range (len(result)):
        print(result[i], ' - ', date[i].text)



login()