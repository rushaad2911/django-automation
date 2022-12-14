
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #F12
import os 

def login(input_repo_name):
        
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path="D:\seleniumdrivers\chromedriver.exe", options=chr_options)


    driver.get('https://github.com/new')
    driver.implicitly_wait(5)

    username_button = driver.find_element(By.ID,'login_field')
    password_button = driver.find_element(By.ID,'password')
    login_button = driver.find_element(By.NAME,'commit')


    username_button.send_keys('m.rushaadq@gmail.com')
    password_button.send_keys('rushaadq2911')
    # password_button.send_keys(keys.   'OPTIONS'  )

    #future

    # def clk(x):
    #     x.click()
    # clk(login_button)

    login_button.click()


    repo_name = driver.find_element(By.ID,'repository_name')
    repo_name.click()
    repo_name.send_keys(f'{input_repo_name}')


    repo_private_butt = driver.find_element(By.CLASS_NAME,'js-privacy-toggle-label-private')

    repo_private_butt.click()


    create_repo_button = driver.find_element(By.CLASS_NAME,'btn-primary.btn')
    create_repo_button.submit()

    repo_setup_info = driver.find_element(By.ID,'empty-setup-new-repo-echo')

    

    print("done creating repo")
