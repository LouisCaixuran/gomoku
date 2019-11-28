
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

 usage: play-go [-h] [--size SIZE] [--simulate_time SIMULATE_TIME]
                {1,2,3,4} {1,2,3,4}

 gomoku program

 positional arguments:
   {1,2,3,4}             1.Human; 2.MCTS; 3.Random; 4.Expert
   {1,2,3,4}             1.Human; 2.MCTS; 3.Random; 4.Expert

 optional arguments:
   -h, --help            show this help message and exit
   --size SIZE           The Board size,default is 8*8
   --simulate-time SIMULATE-TIME
                         The MCTS playout simulation time,default is 2s
```

### Choose a player to play

If you want to play with Expert, you can run:

``` 
 $ play-go 1 4
     
     0   1   2   3   4   5   6   7

 0   -   -   -   -   -   -   -   -

 1   -   -   -   -   -   -   -   -

 2   -   -   -   -   -   -   -   -
 
 3   -   -   -   -   -   -   -   -

 4   -   -   -   -   -   -   -   -

 5   -   -   -   -   -   -   -   -

 6   -   -   -   -   -   -   -   -

 7   -   -   -   -   -   -   -   -
 The Current player: 1
 please enter action:

```

### Auto test diffent players ability

If you want to test MCTS vs Expert , you can run:

```	
$ play-go  2 4

     0   1   2   3   4   5   6   7

 0   -   -   -   -   O   O   -   -

 1   -   -   -   O   -   -   O   X

 2   -   -   -   -   X   -   O   -

 3   -   -   -   X   X   O   -   -

 4   -   -   X   X   X   X   X   -

 5   -   O   -   -   O   -   -   -

 6   -   -   O   -   -   -   -   -

 7   -   -   -   -   -   -   -   -
 The Current player: 2
 player1: O, last action: 0 4
 player2: X, last action: 4 6
 2  wins

```

### Change the chess board size 

If you want to change the chess board size from '8*8'  to '15*15',
you can run :

```

$ play-go 1 4  --size 15

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
The Current player: 1
please enter action:

```

### Change MCTS playout simuelation time
  
The ability of MCTS player can improve when the simulation time is increased.

If you want to change simuelation time to 10s(default 2s), you can run:

```
$ play-go 2 4 -- simulate_time 10

    0   1   2   3   4   5   6   7

 0   -   -   -   -   -   -   -   -

 1   -   -   -   -   -   -   -   -

 2   -   -   -   -   -   O   -   -

 3   -   -   -   -   X   -   -   -

 4   -   -   -   -   -   -   -   -

 5   -   -   -   -   -   -   -   -

 6   -   -   -   -   -   -   -   -

 7   -   -   -   -   -   -   -   -
The Current player: 2
player1: O, last action: 2 5
player2: X, last action: 3 4

```

## Use Web UI:

### Play in local server

```
 $ play-go-web  runserver 

```
Open http://127.0.0.1/main/ in browser


### Play in '192.168.1.10:8000' server

Update the setting.py file : ALLOWED_HOSTS=['192.168.1.10'];

```
 $ play-go-web  runserver 192.168.1.10:8000
```

Open http://192.168.1.10:8000/main/ in browser


# For developers

Any new code to committed should pass the unit tests.


## Run the code for develop:

``` 
 $ sudo python3 setup.py develop

 $ sudo pyhthon3 run.py -h 
```

## Run the unit test:

```
 $ sudo pytest 
```	


