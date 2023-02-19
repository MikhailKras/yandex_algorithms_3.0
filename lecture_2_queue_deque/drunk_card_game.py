from __future__ import annotations


class Card:
    def __init__(self, card_value: int):
        self.card_value = card_value

    def __gt__(self, other: Card) -> bool:
        if self.card_value == 0 and other.card_value == 9:
            return True
        elif self.card_value == 9 and other.card_value == 0:
            return False
        else:
            return self.card_value > other.card_value


def get_winner(list_first_player: list, list_second_player: list):
    i = 0
    while list_first_player and list_second_player:
        if i > 10 ** 6:
            return 'botva'
        i += 1
        top_card_first_player = Card(list_first_player.pop(0))
        top_card_second_player = Card(list_second_player.pop(0))
        if top_card_first_player > top_card_second_player:
            list_first_player.append(top_card_first_player.card_value)
            list_first_player.append(top_card_second_player.card_value)
        else:
            list_second_player.append(top_card_first_player.card_value)
            list_second_player.append(top_card_second_player.card_value)
    else:
        if list_first_player:
            return f'first {i}'
        else:
            return f'second {i}'


if __name__ == '__main__':
    input_list_first_player = list(map(int, input().split()))
    input_list_second_player = list(map(int, input().split()))
    print(get_winner(input_list_first_player, input_list_second_player))
