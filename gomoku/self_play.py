

def initial_board(gomoku):
    gomoku.status=[0 for i in range(gomoku.height*gomoku.width)]
    gomoku.available=[i for i in range(gomoku.height*gomoku.width)]
    gomoku.last_action=-1
    gomoku.end=False
    gomoku.winner=-1
    gomoku.current_player=1
    gomoku.moved_player=0 


def start_self_play(gomoku,player):
    s=[]
    p=[]
    initial_board(gomoku)
    while True:
        move,probs=player.get_action(return_prob=1)
        s.append(gomoku.current_state())
        p.append(probs)
        gomoku.set_action(move)
        gomoku.next_states()
        end,winner=gomoku.game_end()
        if end:
            if winner==1:
                v=[(-1)**i for i in range(len(s)) ]
            elif winner==2:
                v=[ (-1)**(i+1) for i in range(len(s)) ]
            else:
                v=[0 for i in range(len(s)) ]
            return zip(s,p,v)
    

def collect_selfplay_data(gomoku,player,game_num=10):
    data=[]
    for i in range(game_num):
        data.append(list(start_self_play(gomoku,player)))

    return data,len(data)


