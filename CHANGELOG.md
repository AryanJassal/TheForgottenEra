# Release 0.00.120-beta

## Build Highlights

GIANT UPDATE!!! Added a lot of features. You know what? I'm naming this build a beta release.

## Build Notes

`use` action not working yet. Oh, yeah. I added actions.

## New Features/Additons

- Modified project structure (see *Changes/Bug Fixes*)
- Added `__init__.py` to each module and sub-module
- Added actions
- Added action parsing
- Added player and enemy classes
- Adding item classes
- Working on `use` command

## Changes/Bug Fixes

- Changes to project structure

  - Removed `entities` and `items` folder from `game_objects` subfolder.
    - Added `utils.py` file to this sub-module
    - Added `default_enemy_config.json` for testing enemies. This feature may end up in the final product.
    - Added `base_enemies.py` which instantiates these default enemies.
  - `utils` folder has been removed in favour of `utils.py` file
  - `worldgen` has been renamed to `world`
    - Added `default_actions.json` and `default_actions.py` file to this sub-module. They deal with action commands such as `move left`.
    - Added `parse_actions` file. This is a simple yet complex parser which parses json command structure into actual commands and rules.

## **Agenda for next update**

- Fixing `use` command
- Adding more commands
- Adding more items
- Making the player inventory function
- Making a player save file
- Adding worldgen
- Cleaning up UI
- Making a proper loop using the `main.py` file in project root
