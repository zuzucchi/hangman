def hangman(word):
    wrong_guess = 0
    stages = ["0",                          # stagesリストのlenは7、インデックスは0～6
             "1__________   ",
             "2|         |  ",
             "3|         0  ",
             "4|        /|- ",
             "5|        / - ",
             "6|            ",
             ]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong_guess < len(stages) - 1:    # len(stages)=7です。len()関数はインデックス（1個目が0）ではなく個数（1個目が1）を数える。
        print("\n")
        guess = input("Guess a letter")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = "$"
        else:
            wrong_guess += 1
        print((" ".join(letter_board)))
        print("\n".join(stages[0:wrong_guess + 1])) # 間違いが0（wrong_guess=0）の場合でも、スライス指定部で+1される→stages[0:1]となり1行目は絶対printされる
        if "__" not in letter_board:                # (承前) 6回間違うとstages[0:7]となり6行目までprintされ、while文の判定式が
            print("You win! The word was:")         # (承前) wrong_guess : 6 < len(stages)-1 : 6 →False判定 →ループを抜けて、if not win文で負け判定される
            print(" ".join(letter_board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong_guess + 1]))
        print("You lose! It was {}".format(word))