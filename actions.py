import zyga

def display_inventory():
    player = zyga.active_entities['player']

    done_items = []

    for item in player.get_inventory():
        if not item in done_items:
            print(f'[{player.get_amount_of_item(item)}x] {item.name}')
            done_items.append(item)
    return

# Return all actions as dictionary object
def return_actions():
    return {
        'inventory': display_inventory
    }
