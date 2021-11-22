import zyga


def display_inventory():
    player = zyga.active_entities['player']
    zyga.cli.print_player_inventory(player.get_inventory().items())
    return


# Return all actions as dictionary object
def return_actions():
    return {
        'inventory': display_inventory
    }
