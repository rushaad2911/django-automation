#! /bin/bash

requirements=/mnt/d/vs?code/project/django-automation/requirements.txt



echo "enter folder name"
read folder_name
sleep 0.5

echo "enter virtualenv name"
read virtualenv
sleep 0.5

echo "project name"
read project
sleep 0.5

echo "add git init"
read git
sleep 1s

function create_dir(){

    cd /mnt/d/vs?code/project

   
 
    $(mkdir $folder_name )
    echo "folder created" 
    cd $folder_name
    create_virtualenv
   
}

function create_virtualenv(){

    if [[ -z "$virtualenv" ]];then

        virtualenv vir
        echo "virtualenv vir created"
        source vir/bin/activate

    else

        echo $virtualenv
        echo "creating virtualenv $virtualenv"
        virtualenv $virtualenv
        echo "virtualenv $virtualenv created"
        source $virtualenv/bin/activate
    fi

    echo "virtualenv activated"


    create_project
    
}

function create_project(){

    echo "installing requirements"
    pip install -r $requirements
    echo "done installing django"
    pip freeze >> requirements.txt

    if [[ -z "$project" ]];then 

        django-admin startproject config .
    else
        django-admin startproject $project .
    fi


    sleep1 1
    echo "project created"
    $(touch .env)
    $(touch Dockerfile)
    echo ".env created"
    python manage.py runserver
    create_gitrepo

}

function create_gitrepo(){

    if [[ -z "$git" ]];then 
        $(git init)
        $(touch .gitignore)

    fi
    
}

create_dir