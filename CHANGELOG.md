# Release 0.00.120-beta

## Build Highlights

Fixed issues in the `use` action, and added other actions. My command parser now basically ready for (almost) any commands.

## New Features/Additons

- Added new methods to Player class
  - Added `get_inventory`
  - Added `get_item_from_inventory`
  - Added `acquire_item`
  - Added `get_stats`
- Added new methods to Item class
  - Added `get_tags`

## Changes/Bug Fixes

- Cleaned up code in many places (removed commented, unused code)
- Updated `Poison.consume()` to support no arguments being passed
  - Added a temporary notifier that poison has been drunk
- Removed `temp_playerinv`

## **Agenda for next update**

- Adding more commands (working on it)
- Adding more items
- Making the player inventory function (working on it; need to display it)
- Making a player save file
- Adding worldgen
- Cleaning up UI
- Display all stats in `stats` command
- Add modifiers to poison which affect all stats
- Deal with command edge cases (error: index out of range on no input)
