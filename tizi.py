import requests, json, random, re, time,selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
chrome_opt = Options()  # 创建参数设置对象.
chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument('--headless')  # 无界面化.
chrome_opt.add_argument('--disable-gpu')  # 配合上面的无界面化.
chrome_opt.add_argument('--window-size=1366,768')  # 设置窗口大小, 窗口大小会有影响.
chrome_opt.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=chrome_opt)
def get_email():
    a = random.randint(11, 99)
    b = random.randint(0, 20)
    email = 'varytmp+{}uu{}d@gmail.com'.format(a, b)
    return email
def send(email):
    data = {
        'email': email
    }
    s = requests.post(url='https://cv2.cheap/auth/send', data=data).text
    #print(s)
def get_num(email):
    #print(email)
    head = {
        'Cookie': 'csrf_gmailnator_cookie=9283eccf4672e233327c1d07cbde2fbe; __gads=ID=808c92a03a3667c7-2268f1463cc6007d:T=1614844196:RT=1614845007:S=ALNI_MaEB-hZfUPTo6kHkEmOBLzPe4nqTQ; cto_bundle=AGHOXV9XSVpTNzY3TlRHbldjMDY5RFhQTlU4Y2J1cUpIWGNLVU0xa3ZiWGRKV1duNHo5cXpJYSUyQm5mZ0ROVDJBRFlIa211cG85JTJCOElMV0ZGQUIzVCUyRjg4NTdQZmZSSW9xMzZmMVY5dXdXeDViUUFYeG51SWNibEhqZGxqWGU5NjBQZHpxMg; _ga=GA1.2.1618068840.1614844229; _gid=GA1.2.103981802.1614844229; ci_session=15d382f04f7b998cecd0f9158bfe3db2c8f32629; __cfduid=d1f9a21dd34e5060cfd24ea55f37149961614844181'}
    data = {'csrf_gmailnator_token': '9283eccf4672e233327c1d07cbde2fbe', 'action': 'LoadMailList',
            'Email_address': email}
    s = requests.post(url='https://www.gmailnator.com/mailbox/mailboxquery', data=data, headers=head).text
    id = re.findall(r'(?<=messageid\\/#).+(?=\\">\\n\\t\\t\\t\\t\\t<table class=\\"message_container)', s)[0]
    #print(id)
    data1 = {'csrf_gmailnator_token': '9283eccf4672e233327c1d07cbde2fbe', 'action': 'get_message', 'message_id': id,'email': 'varytmp'}
    mess = requests.post(url='https://www.gmailnator.com/mailbox/get_single_message/', headers=head, data=data1).text
    #print(mess)
    s_url = re.findall(r'(?<=\\uff1a\\r\\n\\r\\n).+(?=\\r\\n \\r\\n\\u795d\\u987a\\)', mess)[0].replace('\\','')

    #print(s_url)
    driver.get(s_url)
    time.sleep(5)
    driver.quit()


def register(email):

    driver.get('https://www.zionladdero.com/register')
    #driver.switch_to.frame('//*[@id="register"]/div/div')
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'register')))
    driver.find_element_by_xpath('//*[@id="id_username"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="id_password1"]').send_keys('refddr265rt!')
    driver.find_element_by_xpath('//*[@id="id_password2"]').send_keys('refddr265rt!')
    driver.find_element_by_xpath('//*[@id="register"]/div/div/div[2]/form/div[5]/button').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[11]/div/div[4]/div/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="send-confirm-email"]').click()
    ssr=driver.find_element_by_xpath('/ html / body / div[1] / div / div / div[4] / div / div / p / strong[1]').text
    print(ssr)
    time.sleep(5)
    return ssr
def register2(email,invite):

    driver.get(invite)
    #driver.switch_to.frame('//*[@id="register"]/div/div')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[1]/div/div[2]/a').click()

    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'register')))
    driver.find_element_by_xpath('//*[@id="id_username"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="id_password1"]').send_keys('refddr265rt!')
    driver.find_element_by_xpath('//*[@id="id_password2"]').send_keys('refddr265rt!')
    driver.find_element_by_xpath('//*[@id="register"]/div/div/div/div[2]/form/div[5]/button').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[11]/div/div[4]/div/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="send-confirm-email"]').click()
    ssr=driver.find_element_by_xpath('/ html / body / div[1] / div / div / div[4] / div / div / p / strong[1]').text
    time.sleep(5)
def main():
    email=get_email()
    ssr=register(email)
    time.sleep(5)
    get_num(email)
    return ssr
def main2(invite):
    email = get_email()

    register2(email,invite)
    time.sleep(5)
    get_num(email)

if __name__ == "__main__":
    sele=input('请选择：1.新账号，2.邀请：\n')
    if int(sele)==2:

        invite=input('输入链接:')
        main2(invite)
    elif int(sele)==1:
        main()
    else:
        print('输入错误！')
