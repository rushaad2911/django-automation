#! /bin/bash


virtualenv vir
echo "virtualenv vir created"
source vir/bin/activate
echo "virtualenv activated"
pip install django
echo "done installing django"
django-admin startproject config .
echo "done creating project-----------"