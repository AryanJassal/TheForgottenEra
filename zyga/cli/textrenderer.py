import os
import textwrap
# from ..main import *


def print_player_inventory(player_inventory):
    terminal_size = os.get_terminal_size()
    width = terminal_size.columns

    # player = active_entities['player']
    for item_id, data in player_inventory:
        # print(f'[{player.get_amount_of_item(item)}x] {item.name}')
        print(f'[{data.get("amount", 0)}x] {data["item"].name}')
        dedented_description = textwrap.dedent(data['item'].description).strip()
        print(textwrap.fill(dedented_description, width=width, initial_indent='  ', subsequent_indent='    '), end='')
        print()
    # for item, data in player_inventory:
    #     print(f'[{data.get("amount", "")}x] {data.get("name", "")}')
    # print()

    return
