import random
def hangman(word):
    wrong = 0
    stages = [
        "",
        "________       ",
        "|              ",
        "|        |     ",
        "|        0     ",
        "|       /|\    ",
        "|       /\     ",
        "|              ",
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね。"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)# 入力さえた文字charが何番目にあるかを探す
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1

        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you are Winner!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("you loser! The answer is {}".format(word))

word_list = ["python", "genetics", "science", "battle", "soccer",]
i = random.randint(0, len(word_list)-1)
hangman(word_list[i])
