# Build b16112021-01

## Build Highlights

Changed things here and there to better optimise the code. Fixed minor issues.

## New Features/Additons

- Added `actions.py`
  - Added `display_inventory`
- Added new methods to Player class
  - Added `modify_health`
  - Added `modify_max_health`
  - Added `modify_hunger`
  - Added `modify_max_hunger`
  - Added `modify_thirst`
  - Added `modify_max_thirst`
  - Added `modify_stamina`
  - Added `modify_max_stamina`

## Changes/Bug Fixes

- Removed item classes in favor of universal `Item` class
- Removed `get_health` and `remove_health` from Player
- Cleaned up actions code from `main.py` to `default_actions.py`
  - Moved methods from `main.py` to `actions.py` in project root
- Modified player inventory from `dict` to `list`

## **Agenda for next update**

- Adding more commands (working on it)
- Adding more items

- Making a player save file
- Adding worldgen
- Cleaning up UI
- Deal with new line above command input on clearing screen
- Add modifiers for consume item max_ stats
- Add feedback to the player that player does not have item in their inventory
- Optimise code (comes at the end, or at least, in later stages)
