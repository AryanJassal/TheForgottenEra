# Build alpha-22112021

## **Build Highlights**

Quite a bugfix-packed update, this one. This introduces ground-shattering changes into the build, such as migrating the Agenda to GitHub projects, making it easier to track all the issues and agenda from one place. This also marks a point for the (unexpectedly) most difficult part of the program: saving and loading player data. Need to add minor features before the major code overhaul.

## **Build Notes**

From now on, I will not work on any complex features, and just aim at cleaning up and optimising the code.

This is just for me and my future reference: I tried to pass `**kwargs` to initialise item classes, and it was more trouble and user-unfriendliness than the current pass dictionary to class and `__init__` function will do its job method.

## **New Features/Additons**

- Added `print_player_inventory` function in `textrenderer.py` in the `cli` module.
- Added `save_player` in `default_actions.py` in `cli` module.
  - Seperated saving the player stats and the player inventory into different steps and files
- Added `modify_attributes` function in the `Player` class.
- Added `development` variable in `zyga/main.py`, which is separate from `global_vars`

## **Changes/Bug Fixes**

- Changed main working branch from `master` to a different `development` branch.
  - ~~Build version will reflect the day of merging `development` into `master`.~~
  - Alpha, Beta, or Releases will be merged into master, not an experimental build.
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
- Removed redundant `if file:` in opening files to save data, as if the files don't exist, they will be created automatically
- Created `load_player` function to load the player including their inventory
- Created `load_file` function in `zyga.utils.py` to load a file *the proper way* everytime.
- Added newline after displaying inventory
- Changed command prompt from `|command-prompt>` to `|>`
- Changed item field names to play well with what gets sent out as a `dict` and what gets ultimately loaded back into the game
- Removed commented code from `display_inventory` function in `/actions.py`
- Changed empty `except:` to `except KeyError:` in `zyga.cli.parse_actions.py`
