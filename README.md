
# How to run 

## Install 
```        
	$ git clone https://github.com/LouisCaixuran/gomoku.git
	$ cd gomoku
```

### If use CLI:
```
	$ sudo pip3 install -r requirements.txt
	$ sudo python3 setup.py install
```

### If use CLI and web:

```
	$ sudo pip3 install -r web-requirements.txt
	$ sudo python3 setup.py install
```
## Use CLI:
```	
	$ play-go -h
	usage: play-go [-h] {1,2,3,4} {1,2,3,4}

	gomoku program

	positional arguments:
	{1,2,3,4}   1.Human; 2.MCTS; 3.Random; 4.Expert
	{1,2,3,4}   1.Human; 2.MCTS; 3.Random; 4.Expert

	optional arguments:
	 -h, --help  show this help message and exit
```

* If you want to play with Expert player,you can run:
```	
	$ play-go  1 4

             0   1   2   3   4   5   6   7   8   9   10  11  12  13  14

         0   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

         1   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

         2   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

         3   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

         4   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

         5   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

         6   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

         7   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

         8   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

         9   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

         10  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

         11  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

         12  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

         13  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

         14  -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
         please enter action:
```

## Use Web UI:

### Play in local server

```
	$ play-go-web  runserver 

```
Open http://127.0.0.1:8000/main/ in browser


### Play in '192.168.1.10:8000' server

Update the setting.py file : ALLOWED_HOSTS=['192.168.1.10'];

```
	 $ play-go-web  runserver 192.168.1.10:8000
```

Open http://192.168.1.10:8000/main/ in browser

	
