from sklearn.naive_bayes import MultinomialNB
import time
import random
from hashlib import *

# 定义决策表示
ROCK = 0
PAPER = 1
SCISSORS = 2

X_train = [[]]
y_train = []

model = None
total_rounds = 100
player_score = 0
sequence = []

# 定义决策名称
CHOICES = {
    ROCK: "石头",
    PAPER: "剪刀",
    SCISSORS: "布"
}


def train_model(X_train, y_train):
    model = MultinomialNB()
    model.fit(X_train, y_train)
    return model


def predict_opponent_choice(model, X_pred):
    return model.predict(X_pred)


def predict(i,my_choice):

    
    global  sequence
    model = None
    if i < 5:
        opponent_choice = [random.randint(0, 2)]
    else:
        model = train_model(X_train, y_train)
        opponent_choice = predict_opponent_choice(model, [sequence])

# ...Constructing a training set...#

    return opponent_choice

def play_game(flag):
    global player_score
    for i in range(total_rounds):

        start_time = time.time()
        my_choice = None
        opponent_choice = [random.randint(0, 2)]

        my_choice = int(input("请出拳（0 - 石头，1 - 剪刀，2 - 布）："))

        end_time = time.time()
        if end_time - start_time > 5:
            print("超时！！！")
            break
        if my_choice not in {0, 1, 2}:
            print("错误的输入")
            break

        opponent_choice = predict(i,my_choice)

        landa = (opponent_choice[0] - 1) % 3
        print("你的出拳：", CHOICES[my_choice])
        print(f"Me10n出拳：{CHOICES[landa]}")

        if (my_choice + 1) % 3 == landa:
            print("你赢了！")

            player_score += 3
        elif (landa + 1) % 3 == my_choice:
            print("Me10n赢了！")
            player_score += 0
        else:
            print("平局！")

            player_score += 1
        print("你的分数：", player_score)
        print("-----------------------------------")

        if player_score >= 260:
            print("你获得了flag:"+flag+"")
            break

    print("游戏结束")
    print("你的分数：", player_score)


print("++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Landa和他的好兄弟Me10n很喜欢玩石头剪刀布，但是他老是输给Me10n。于是他写了个程序来帮他出拳，你来挑战一下吧！")
print("平局得1分，赢得3分，输得0分。100局中如果你能得到260分就送你一个flag作为奖励吧！注意出拳要快！")
print("++++++++++++++++++++++++++++++++++++++++++++++++++")

with open('flag' , 'r' ) as f:
    flag = f.read()

play_game(flag)
