import numpy as np


def initial_board(gomoku):
    gomoku.status = [0 for i in range(gomoku.height * gomoku.width)]
    gomoku.available = [i for i in range(gomoku.height * gomoku.width)]
    gomoku.last_action = -1
    gomoku.end = False
    gomoku.winner = -1
    gomoku.current_player = 1
    gomoku.moved_player = 0


def start_self_play(gomoku, player):
    s = []
    p = []
    initial_board(gomoku)
    while True:
        move, probs = player.get_action(return_prob=1)
        s.append(gomoku.current_state())
        p.append(probs)
        gomoku.set_action(move)
        gomoku.next_states()
        end, winner = gomoku.game_end()
        print(probs)
        if end:
            if winner == 1:
                v = [(-1)**i for i in range(len(s))]
            elif winner == 2:
                v = [(-1)**(i + 1) for i in range(len(s))]
            else:
                v = [0 for i in range(len(s))]
            return zip(s, p, v)


def rotate1(gomoku, one_game_data):
    ext_data = []
    s1 = []
    p1 = []
    count = 1
    for s, p, v in one_game_data:
        s1.append(s)
        p1.append(p)
        for i in range(4):
            s1.append(4 * np.zeros((4, gomoku.width, gomoku.height)))
            p1.append(np.zeros((gomoku.height * gomoku.width)))
            for j in range(4):
                s1[count][j] = np.rot90(s1[count - 1][j])
            p1[count] = np.rot90(
                p1[count - 1].reshape(gomoku.width, gomoku.height)).flatten()
            ext_data.append((s1[count], p1[count], v))
            count = count + 1
        print(ext_data[2][0][0])
    return ext_data


def rotate(gomoku, one_game_data):
    extend_data = []
    for state, probs, value in one_game_data:
        for i in [1, 2, 3, 4]:
            # rotate counterclockwise
            equi_state = np.array([np.rot90(s, i) for s in state])
            equi_prob = np.rot90(probs.reshape(gomoku.height,
                                               gomoku.width), i)
            extend_data.append((equi_state, equi_prob.flatten(), value))
    return extend_data


def collect_selfplay_data(gomoku, player, game_num=10):
    play_data = []
    for i in range(game_num):
        play_data.extend(rotate(gomoku, start_self_play(gomoku, player)))

    return play_data, len(play_data)
