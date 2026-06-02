import random
import time

def create_deck():
    values = ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']
    suits = ['♥', '♦', '♣', '♠']
    deck = [(v, s) for v in values for s in suits]
    random.shuffle(deck)
    return deck

def card_str(card):
    return f"{card[0]}{card[1]}"

def get_rank(card, trump_suit):
    values = ['6', '7', '8', '9', '10', 'В', 'Д', 'К', 'Т']
    rank = values.index(card[0])
    if card[1] == trump_suit:
        rank += 100
    return rank

def can_beat(attack, defend, trump_suit):
    if defend[1] == attack[1]:
        return get_rank(defend, trump_suit) > get_rank(attack, trump_suit)
    elif defend[1] == trump_suit and attack[1] != trump_suit:
        return True
    return False

def draw_cards(deck, n):
    cards = []
    for _ in range(min(n, len(deck))):
        cards.append(deck.pop())
    return cards

def show_hand(hand):
    for i, card in enumerate(hand):
        print(f"{i+1}. {card_str(card)}", end="  ")
    print()

def main():
    print("=== Игра 'Дурак'ы ===")
    print("Правила: вы и компьютер ходите по одной карте.")
    print("Если вы не можете побить карту соперника - вы её забираете.")
    print("Козырь бьёт любую некозырную карту.\n")

    deck = create_deck()
    trump_suit = deck[0][1]
    deck.pop(0)
    print(f"Козырь: {trump_suit}\n")

    player_hand = draw_cards(deck, 6)
    computer_hand = draw_cards(deck, 6)

    turn = 'player'

    while True:
        print(f"\n--- Ваша рука ({len(player_hand)} карт) ---")
        show_hand(player_hand)
        print(f"Карт у компьютера: {len(computer_hand)}")
        print(f"Козырь: {trump_suit}")
        print(f"Ход: {'игрок' if turn == 'player' else 'компьютер'}")

        if turn == 'player':
            if not player_hand:
                print("У вас нет карт! Вы победили!")
                break

            print("Выберите карту для хода (номер):")
            try:
                idx = int(input()) - 1
                if idx < 0 or idx >= len(player_hand):
                    print("Неверный номер карты.")
                    continue
                attack_card = player_hand.pop(idx)
            except ValueError:
                print("Введите число.")
                continue

            print(f"Вы ходите: {card_str(attack_card)}")
            time.sleep(0.8)

            print("Компьютер думает...")
            time.sleep(0.5)
            beaten = False
            for i, defend_card in enumerate(computer_hand):
                if can_beat(attack_card, defend_card, trump_suit):
                    print(f"Компьютер бьёт: {card_str(defend_card)}")
                    computer_hand.pop(i)
                    beaten = True
                    break
            if not beaten:
                print("Компьютер не может побить и забирает карту.")
                computer_hand.append(attack_card)
            else:
                turn = 'computer'
            time.sleep(0.8)

        else:
            if not computer_hand:
                print("У компьютера нет карт! Вы проиграли!")
                break

            attack_card = computer_hand.pop(random.randint(0, len(computer_hand)-1))
            print(f"Компьютер ходит: {card_str(attack_card)}")
            time.sleep(0.8)

            print("\nВаши карты:")
            show_hand(player_hand)
            print("Выберите номер карты, которой хотите побить, или 0 чтобы забрать карту себе.")
            beaten = False
            while True:
                try:
                    choice = int(input("Ваш выбор: "))
                    if choice == 0:
                        print("Вы решили забрать карту себе.")
                        player_hand.append(attack_card)
                        break
                    elif 1 <= choice <= len(player_hand):
                        defend_card = player_hand[choice-1]
                        if can_beat(attack_card, defend_card, trump_suit):
                            print(f"Вы бьёте картой: {card_str(defend_card)}")
                            player_hand.pop(choice-1)
                            beaten = True
                            break
                        else:
                            print("Этой картой нельзя побить. Попробуйте другую или 0 чтобы забрать.")
                    else:
                        print(f"Введите число от 0 до {len(player_hand)}")
                except ValueError:
                    print("Введите число.")

            if beaten:
                turn = 'player'
            else:
                turn = 'computer'
            time.sleep(0.8)

        if len(player_hand) < 6 and deck:
            need = 6 - len(player_hand)
            player_hand.extend(draw_cards(deck, need))
        if len(computer_hand) < 6 and deck:
            need = 6 - len(computer_hand)
            computer_hand.extend(draw_cards(deck, need))

        if not deck:
            if len(player_hand) == 0:
                print("\nПоздравляем! Вы выиграли!")
                break
            elif len(computer_hand) == 0:
                print("\nВы проиграли! Компьютер остался без карт.")
                break
            elif len(player_hand) == 0 and len(computer_hand) == 0:
                print("\nНичья!")
                break

    print("Игра окончена. Спасибо за игру!")

if __name__ == "__main__":
    main()
