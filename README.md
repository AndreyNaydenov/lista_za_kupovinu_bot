# Project Description: Shopping List Telegram Bot

## Overview
The idea behind this Telegram bot is to manage a dynamic shopping list. Users can add items to the list when they need them and remove items once they’ve been purchased. Additionally, the bot will include features like automatic item addition, store location suggestions, and a product library with essential information about each item.

## Key Features

1. **Dynamic Shopping List:**
   - Users can manually add items to the shopping list when needed.
   - Items can be removed from the list once purchased.

2. **Automatic Item Addition:** (TODO in future)
   - The bot can automatically add items to the list based on predefined criteria (e.g., frequent purchases, seasonal needs).

3. **Store Location Integration:** (TODO in future)
   - Users can indicate which store carries specific items.
   - The bot can suggest stores where listed items can be found, based on user preferences or previous shopping history.

4. **Product Library:** (TODO in future)
   - The bot will feature a comprehensive product library containing basic information about various items.
   - Users can browse or search the library to find detailed information on products before adding them to the list.

5. **Buying history:** (TODO in future)
   - Gather and show statistics like frequency of shopping products.

## Objective
To simplify the shopping process by providing a well-organized, easily manageable shopping list, enhanced with automation and detailed product information. This bot aims to save users time and effort in planning and executing their shopping tasks.

## Basic realisation
User starts the bot and can make a new list or attach to an existing one (by using list ID, like in ntfy.sh). After that he can issue commands "/add <product name and other info>" "/remove <product num or short name>" "/got <same as /remove>" "/list" 

## TODO
- Make /add function
- Make /flush function to remove all elements from the list
- Make /got function to mark item as bought
- Make /remove function to just remove item without marking as bought
- Make function that shows recommended items to add (depending in history)
- Buttons to not write commands manually
