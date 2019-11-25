
# How to run 

## Install 
        
	$ git clone https://github.com/LouisCaixuran/gomoku.git
	$ cd gomoku
	$ sudo pip3 install -r requirements.txt
	$ sudo python3 setup.py install

## Use
	$ play-go -h
	usage: play-go [-h] {1,2,3,4} {1,2,3,4}

	gomoku program

	positional arguments:
	{1,2,3,4}   1.Human; 2.MCTS; 3.Random; 4.Expert
	{1,2,3,4}   1.Human; 2.MCTS; 3.Random; 4.Expert

	optional arguments:
	 -h, --help  show this help message and exit


If you want to play with Expert player,you can run:
	
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



# Support four players:

* 1.Human player
* 2.MCTS player
* 3.Random player
* 4.Expert player
	
