from channels.generic.websocket import WebsocketConsumer
import json
from queue import Queue
from .board import Gomoku
from .player import ExpertPlayer,RandomPlayer,MCTSPlayer
import threading
import logging

class ChessConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.queue = Queue(maxsize=1)  #定义一个queue，作为两个线程的交互数据
        

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['msgtype'] == 'chess' :
            self.queue.put(text_data_json)

        if text_data_json['msgtype'] =='playinfo':
            self.isfirst=text_data_json['whoisfirst']
            self.player=text_data_json['player']
            start_game_thread = threading.Thread(target=start_game,args=(self,))
            start_game_thread.start()

class Webplayer(object):
    def __init__(self,consumer,chess):
        self.consumer=consumer
        self.chess=chess


    def get_action(self):
        chess_data=self.consumer.queue.get()
        acion=chess_data['Px']*15+chess_data['Py']
        #logging.info("chess_data:{}".format(chess_data))

        return acion

    def reply(self,x,y):
        reply_data={}
        reply_data['msgtype'] = 'chess'
        reply_data['Color'] = self.chess.status[self.chess.last_action]
        reply_data['Px'] = x
        reply_data['Py'] = y
        reply_data['end'] = self.chess.end
        reply_data['winner'] = self.chess.winner
        self.consumer.send(json.dumps(reply_data))
        logging.info("reply_data:{}".format(reply_data))
        #logging.info("chess_lastaction:{}".format(self.chess.last_action))
        #logging.info("chess_status:{}".format(self.chess.status))

def log_config():
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    logging.basicConfig(filename = 'gomoku.log', 
                        level=logging.DEBUG,
                        format=LOG_FORMAT,
                        datefmt=DATE_FORMAT)


def start_game(consumer):
    log_config()
    chess =Gomoku()
    player1=Webplayer(consumer,chess)
    
    if consumer.player=="expert":
        player2=ExpertPlayer(chess)
    elif consumer.player=="senior":
        player2=MCTSPlayer(chess)
    else:
        player2=RandomPlayer(chess)

    logging.info("consumer_player:{}".format(consumer.player))
    logging.info("player2Board:{}".format(player2.board))
    
    if consumer.isfirst=='Me':
        chess.play(player1,player2)
    else:
        chess.play(player2,player1)


