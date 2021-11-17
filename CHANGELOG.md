# Build b18112021-01

## **Build Highlights**

Very basic improvements. Fixed the `on_consume` in `item.consume()`. You thought that was all? No, sir! We have a plethora of improvements! A large chunk of agenda for the next update was completed! Just need to do minor, QOL improvements and making a player save file, then all is done.

## **Build Notes**

From now on, I will not work on any complex features, and just aim at cleaning up and optimising the code.

## **New Features/Additons**

- Made the `##` headings bold in `CHANGELOG.md`
- Added methods in `Player` class
  - Added `modify_defense` function

## **Changes/Bug Fixes**

- Modified the `Player` class
  - Removed commented, unused `modify_attributes` function
  - Removed commented, unused `get_health` function
  - Removed commented, unused `lose_hunger` function
  - Removed commented, unused `gain_hunger` function
  - Removed commented, unused `lose_stamina` function
  - Removed commented, unused `gain_stamina` function
  - Removed commented, unused `lose_thirst` function
  - Removed commented, unused `gain_thirst` function
  - Removed redundant `get_defense` function. Instead, use `entity.defense`.
- Removed commented, unused `Item` subclasses for favour for a universal `Item` class
  - Removed `Poison` class
  - Removed `BadItem` class
- Changed `destroy_object` to `kill_self` in `Enemy` class
- Changed error message if selected item is not found in valid_items list in `parse_actions.py`
- Removed `print()` after `result()` in `main.py` in preference to putting a `\n` after every error message or console out.
- Moved `default_actions.json`, `default_actions.py`, and `parse_actions.py` to `cli` sub-module.
- Removed `from . import parse_actions` from `world` sub-module's `__init__.py`, transferring it to `cli` submodule's `__init__.py`
  - Added `cli` sub-module in `zyga.__init__.py`

## **Agenda for next update**

- Making a player save file
- [-] Deal with new line above command input on clearing screen
- [-] Add feedback to the player that player does not have item in their inventory
- Add item description
- Optimise/clean code (comes at the end, or at least, in later stages)
- [-] Fix issue with `modify_health` draining too much health
- [-] Add modifiers for consume item max_ stats

- Adding worldgen/world interaction
