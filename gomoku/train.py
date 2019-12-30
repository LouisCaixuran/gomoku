# -*- coding: utf-8 -*-

from __future__ import print_function
import random
import numpy as np
from collections import defaultdict, deque
from board import Gomoku
from self_play import collect_selfplay_data
from player import MCTSPlayer as MCTS_Pure
from alphazero import AlphaZeroPlayer
#from policy_value_net_numpy import PolicyValueNet 
from policy_value_net_pytorch import PolicyValueNet 

class Train():
    def __init__(self, init_model=None):
        # params of the board and the game
        self.board_size = 8
        self.board = Gomoku(board_size=self.board_size)
        # training params
        self.n_playout = 400  # num of simulations for each move
        self.c_puct = 5
        self.buffer_size = 1024
        self.batch_size = 512  # mini-batch size for training
        self.data_buffer = deque(maxlen=self.buffer_size)
        self.epochs = 10  # num of train_steps for each update
        self.check_freq = 10
        self.game_batch_num = 500  
        
        self.best_win_ratio = 0.0
        self.lr_multiplier = 1
        self.learn_rate = 2e-3
        self.kl_targ = 0.02

        # num of simulations used for the pure mcts, which is used as
        # the opponent to evaluate the trained policy
        self.mcts_simulate_time = 5
        if init_model:
            # start training from an initial policy-value net
            self.policy_value_net = PolicyValueNet(self.board.width,
                                                   self.board.height,
                                                   model_file=init_model)
        else:
            # start training from a new policy-value net
            self.policy_value_net = PolicyValueNet(self.board.width,
                                                   self.board.height)
            self.mcts_player = AlphaZeroPlayer(self.board,self.policy_value_net.policy_value_fn,
                                      c_puct=self.c_puct,
                                      n_playout=self.n_playout,
                                      is_selfplay=1)
    
    
    #进行训练
    def policy_update(self):
        """update the policy-value net"""
        mini_batch = random.sample(self.data_buffer, self.batch_size)
        state_batch = [data[0] for data in mini_batch]
        mcts_probs_batch = [data[1] for data in mini_batch]
        winner_batch = [data[2] for data in mini_batch]
        old_probs, old_v = self.policy_value_net.policy_value(state_batch)
        
        for i in range(self.epochs):
            loss, entropy = self.policy_value_net.train_step(
                    state_batch,
                    mcts_probs_batch,
                    winner_batch,
                    self.learn_rate*self.lr_multiplier)
            new_probs, new_v = self.policy_value_net.policy_value(state_batch)
            kl = np.mean(np.sum(old_probs * (
                    np.log(old_probs + 1e-10) - np.log(new_probs + 1e-10)),
                    axis=1)
            )
            if kl > self.kl_targ * 4:  # early stopping if D_KL diverges badly
                break
        # adaptively adjust the learning rate
        if kl > self.kl_targ * 2 and self.lr_multiplier > 0.1:
            self.lr_multiplier /= 1.5
        elif kl < self.kl_targ / 2 and self.lr_multiplier < 10:
            self.lr_multiplier *= 1.5

        print(("kl:{:.5f},lr_multiplier:{:.3f},loss:{},entropy:{}"
               ).format(kl,self.lr_multiplier,loss,entropy))
        return loss, entropy
  
    #进行评估
    def policy_evaluate(self, n_games=10):
        """
        Evaluate the trained policy by playing against the pure MCTS player
        Note: this is only for monitoring the progress of training
        """
        win_cnt = defaultdict(int)
        for i in range(n_games):
            board = Gomoku(board_size=self.board_size)
            alphazero_player = AlphaZeroPlayer(board,self.policy_value_net.policy_value_fn,
                                               c_puct=self.c_puct,
                                               n_playout=self.n_playout)
            pure_mcts_player = MCTS_Pure(board, c_puct=self.c_puct,
                                         simulate_time = self.mcts_simulate_time)
            
            winner = board.play(alphazero_player,
                                pure_mcts_player,isShow=False)
            win_cnt[winner] += 1
        win_ratio = 1.0*(win_cnt[1] + 0.5*win_cnt[-1]) / n_games
        print("simulate_time:{}, win: {}, lose: {}, tie:{}".format(
             self.mcts_simulate_time,
                win_cnt[1], win_cnt[2], win_cnt[-1]))
        return win_ratio

   #保存模型数据
    def save_model(self,win_ratio):
        self.policy_value_net.save_model('./current_policy.model')
        if win_ratio > self.best_win_ratio:
            print("New best policy!!!!!!!!")
            self.best_win_ratio = win_ratio
            # update the best_policy
            self.policy_value_net.save_model('./best_policy.model')
            if (self.best_win_ratio == 1.0 and
                self.mcts_simulate_time  <= 5):
                self.mcts_simulate_time  += 5
                self.best_win_ratio = 0.0

    # 整个训练流水线
    def run(self):
        """run the training pipeline"""
        try:
            for i in range(self.game_batch_num):
                #收集数据
                play_data,episode_len = collect_selfplay_data(self.board, self.mcts_player)
                self.data_buffer.extend(play_data)
                print("batch i:{}, episode_len:{}".format(i+1, episode_len))
                  
                #训练模型
                if len(self.data_buffer) > self.batch_size:
                    loss,entropy = self.policy_update()
                
                # 每50次对模型进行一次评估
                if (i+1) % self.check_freq == 0:
                    print("current self-play batch: {}".format(i+1))
                    win_ratio = self.policy_evaluate()
                    self.save_model(win_ratio)
        except KeyboardInterrupt:
            print('\n\rquit')


if __name__ == '__main__':
    training_pipeline = Train()
    training_pipeline.run()
