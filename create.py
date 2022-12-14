import os 
import shutil
import subprocess
import github_login

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
    
    # github_login.login(git_repo_name)
    
    print("process done")
    
    
    
create_folder()