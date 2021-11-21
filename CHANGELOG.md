# Build b20112021

## **Build Highlights**

TODO

## **Build Notes**

From now on, I will not work on any complex features, and just aim at cleaning up and optimising the code.

This is just for me and my future reference: I tried to pass `**kwargs` to initialise item classes, and it was more trouble and user-unfriendliness than the current pass dictionary to class and `__init__` function will do its job method.

Note: Player cannot save because items in player inventory are references to classes. Need to change that to some other method of storing an inventory.

## **New Features/Additons**

- Added `print_player_inventory` function in `textrenderer.py` in the `cli` module.
- Added `save_player` in `default_actions.py` in `cli` module.
- Added `modify_attributes` function in the `Player` class.
- Added `development` variable in `zyga/main.py`, which is separate from `global_vars`

## **Changes/Bug Fixes**

- Changed main working branch from `master` to a different `development` branch.
  - Build version will reflect the day of merging `development` into `master`.
- Removed redundant `attack_enemy` method from `Entity` class
- Changed `if '%' in prompt; elif command[1] == prompt` to two separate `if` statements
- Added a default `None` value for `get_default_actions` in `parse_actions.py`
- Added `except AttributeError` for method calling commands in `parse_actions.py`
- Fixed indentation error in `consume` function of `Item` class in `item_classes.py`.
- Renamed `render.py` to `textrenderer.py` in `cli` module.
- Changed values of `__init__.py` in the `cli` module and the `zyga` package
- Added error checking to loading files
  - Added error checking before loading an empty `playerconfig.json` file.
- Removed duplicated code in `modify_x` function, replaced with a call to the `modify_attributes` function
- Migrated `Agenda for Next Update` to GitHub Projects
