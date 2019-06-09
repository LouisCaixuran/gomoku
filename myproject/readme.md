readme.md

This is a gomoku web game based on django framework.

## How to build the environmet

	$pip3 install django
	$pip3 install numpy
	$pip3 install channels

## How to run the program

### Play in local server
	
	$python3 manage.py runserver

Open http://127.0.0.1:8000/main/ in browser

### Play in another server
If the server IP is 192.168.1.10 
update the setting.py file : ALLOWED_HOSTS=[192.168.1.10]
	
	$python3 manage.py runserver 192.168.1.10:8000

Open http://192.168.1.10:8000/main/ in browser


## Notice

only support python3

