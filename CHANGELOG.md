# Build b20112021

## **Build Highlights**

TODO

## **Build Notes**

From now on, I will not work on any complex features, and just aim at cleaning up and optimising the code.

This is just for me and my future reference: I tried to pass `**kwargs` to initialise item classes, and it was more trouble and user-unfriendliness than the current pass dictionary to class and `__init__` function will do its job method.

## **New Features/Additons**

- Added `print_player_inventory` function in `textrenderer.py` in the `cli` module.

## **Changes/Bug Fixes**

- Changed main working branch from `master` to a different `development` branch.
  - Build version will reflect the day of merging `development` into `master`.
- Removed redundant `attack_enemy` method from `Entity` class
- Changed `os.system('cls clear')` to `import subprocess; subprocess.call('cls clear', shell=False)`
- Changed `if '%' in prompt; elif command[1] == prompt` to two separate `if` statements
- Added a default `None` value for `get_default_actions` in `parse_actions.py`
- Added `except AttributeError` for method calling commands in `parse_actions.py`
- Fixed indentation error in `consume` function of `Item` class in `item_classes.py`.
- Renamed `render.py` to `textrenderer.py` in `cli` module.
- Changed values of `__init__.py` in the `cli` module and the `zyga` package

## **Agenda for next update**

- [x] Add modifiers for consume item max_ stats
- [x] Fix issue with `modify_health` draining too much health
- [x] Deal with new line above command input on clearing screen
- [x] Add feedback to the player that player does not have item in their inventory
- [x] Add item description
- [ ] Making a player save file
- [ ] Optimise/clean code (comes at the end, or at least, in later stages)

- [ ] Adding worldgen/world interaction
