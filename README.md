# Project 4 - Beginner's Website Devlopment 

### Credits : [Mitch](https://github.com/mitchtabian)
## [Resource](https://www.youtube.com/watch?v=i6cwBiz7BuQ&list=PLgCYzUzKIBE_dil025VAJnDjNZHHHR9mW)

- This project is mainly about creating a simple website for my College's Wellness Program (UWP).The project is mainly done using **[Django(Python)](https://www.djangoproject.com/) and HTML**
- I followed coding with mitch's tutorial to create this website and used [**Bootstrap** ](https://getbootstrap.com/) for CSS.
- I had zero knowledge in HTML and Django before starting this project .

## What have I learnt ?
- [working in Python virtual Environment](https://www.youtube.com/watch?v=O9jEVOtpu5M&list=PLgCYzUzKIBE_dil025VAJnDjNZHHHR9mW&index=2)
- [Creating Django Basic Model with Admin access , Login , Registration and Accounts Screens ( A Basic Website )](https://www.youtube.com/watch?v=0hIMiq0YZSc&list=PLgCYzUzKIBE_dil025VAJnDjNZHHHR9mW&index=7) 
- [Using and Experimenting with different Bootstrap (v4.5) to add CSS framework to the website.](https://www.youtube.com/watch?v=PKOdeXy9-6M&list=PLgCYzUzKIBE_dil025VAJnDjNZHHHR9mW&index=18)

## Pre-Requisites
- Install [python3](https://www.python.org/downloads/)
- Install Django
```
...\> py -m pip install Django
```
- Install Virtualenv 
```	
...\> pip install virtualenv
```
## How to Create Python Virtual Environment ?
- Open command prompt at the place you want to create the virtual Environment
			
	<kbd>Shift</kbd> + <kbd>Right-click</kbd> and click on 'open command window here' 

- Create virtual environment 
```
virtualenv <your environment name > 
# Eg: virtualenv Dravidsenvironment'
```
- Activate virtual environment 
	- Swtich to the directory 
	```
	cd <name of the environement created> 
	# Eg: cd Dravidsenvironment
	```
	- Activate the environment
	```
	Scripts\activate
	```
	
- Now you can create files and install dependencies that will be used only withing the environment created.

## How to Open the website that I created ?

- Download files and check whether all pre-requisites are installed 
- with Command prompt pointing in the src folder type,
```
...\> python manage.py runserver
```
- An ip-address that goes <kbd>http://127.0.0.1:8000/</kbd> will be returned 
- Paste in your browser url and press enter to open the website.

### Note:
This is a project that I took up voluntarily to learn a thing or two about creating a website .
