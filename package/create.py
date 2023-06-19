import os 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

folder_path = 'D:/vs code/project/'

virtualenv_file = '/mnt/d/vs?code/project/django-automation/virtual.sh'

folder_name = str(input('Enter Folder name: '))

project_name = str(input('Enter project name: '))

git_repo_name = str(input('Enter git repo name: '))

project_file = os.getcwd()

os.chdir(folder_path)



def create_folder(): 
    
    os.mkdir(folder_name)
    os.chdir(folder_name)
    print(f"{folder_name} created ")
    print(f"\n Current working directory is {os.getcwd()} \n") 
    
    
    env_setup()


def env_setup():
    
    os.system(f'bash {virtualenv_file}')
    print('vir activated')
   
    
    
    print('\n virtualenv activated')
    
    os.system('git init')
   
    
    project_setup()
    
    
def project_setup():
    
    print('\ncreating project')
    
    os.system(f'django-admin startproject {project_name} .')

    
    print('creating github repo')
    
    if git_repo_name != "":
        
        login(git_repo_name)
        
    
    
    
    
    print("process done")
    
    
    

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
   

    login_button.click()


    repo_name = driver.find_element(By.ID,'repository_name')
    repo_name.click()
    repo_name.send_keys(f'{input_repo_name}')


    repo_private_butt = driver.find_element(By.CLASS_NAME,'js-privacy-toggle-label-private')

    repo_private_butt.click()


    create_repo_button = driver.find_element(By.CLASS_NAME,'btn-primary.btn')
    create_repo_button.submit()

    # repo_setup_info = driver.find_element(By.ID,'empty-setup-new-repo-echo')
    # repo_setup_info = repo_setup_info.text
    
    # os.system(repo_setup_info)

    print("done creating repo")


create_folder()