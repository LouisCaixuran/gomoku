readme.md

# How to run

	$ python run.py -h
	usage: run.py [-h] {1,2,3,4} {1,2,3,4}

	gomoku program

	positional arguments:
	{1,2,3,4}   1.HumanPlayer; 2.MCTSPlayer; 3.RandomPlayer; 4.ExpertPlayer
	{1,2,3,4}   1.HumanPlayer; 2.MCTSPlayer; 3.RandomPlayer; 4.ExpertPlayer

	optional arguments:
	-h, --help  show this help message and exit

If you want to play with ExpertPlayer,you can run
	
	$ python run.py 1 4


# Support four kinds of players:

* 1.Human player
* 2.MCTS player
* 3.Random player
* 4.Expert player
