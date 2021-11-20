import os
import textwrap

import zyga


def print_player_inventory(player_inventory):
    terminal_size = os.get_terminal_size()
    width = terminal_size.columns
    print(width, end='\n\n')

    player = zyga.active_entities['player']
    done_items = []
    for item in player.get_inventory():
        if item not in done_items:
            print(f'[{player.get_amount_of_item(item)}x] {item.name}')
            dedented_description = textwrap.dedent(item.description).strip()
            print(textwrap.fill(dedented_description, width=width, initial_indent='  ', subsequent_indent='    '))
            done_items.append(item)
            print()
    print()

    return