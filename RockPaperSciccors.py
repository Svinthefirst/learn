import random

choices = ["камень", "ножницы", "бумага"]
win_combinations = [("камень", "ножницы"), ("ножницы", "бумага"), ("бумага", "камень")]

def get_winner(player, computer):
    if player == computer:
        return "ничья"
    if (player, computer) in win_combinations:
        return "игрок"
    else:
        return "компьютер"

def main():
    score_player = 0
    score_computer = 0
    while True:
        print("\nВаш выбор: камень, ножницы или бумага?")
        player_choice = input().strip().lower()
        if player_choice not in choices:
            print("Неверный ввод, попробуйте снова.")
            continue
        computer_choice = random.choice(choices)
        print(f"Компьютер выбрал: {computer_choice}")
        
        winner = get_winner(player_choice, computer_choice)
        if winner == "игрок":
            print("Вы победили!")
            score_player += 1
        elif winner == "компьютер":
            print("Компьютер победил!")
            score_computer += 1
        else:
            print("Ничья!")
        
        print(f"Счёт: Игрок {score_player} : {score_computer} Компьютер")
        
        print('Наберите "выход" чтобы закончить или любой другой текст чтобы продолжить')
        again = input().strip().lower()
        if again == "выход":
            print("Спасибо за игру!")
            break

main()
