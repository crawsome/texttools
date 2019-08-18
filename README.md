# texttools

## Purpose
Originally made for github.com/crawsome/pyrpg_mini, I ended up using a couple of these tools for my other projects that used console output. 

## Requirements 
* textwrap
* difflib

## marqueeprint(text)
Prints a centered

## leftprint
Left-justify print


## rightprint(text)
right-justify print


## centerprint(text)
centered print


### lr_justify(left, right, width)
From https://stackoverflow.com/questions/9660109/allign-left-and-right-in-python


### fiverowprintoptions(dataheader, table_data, title)
Prints 5 rows of something with numeric options on left

### gridoutput(table_data)
dynamic sized row-at-a-time output. Will appropriately size the margins of any dict passed to it and tries to print it out all pretty-like.

### similarstring(a, b)
if string is at least 80% similar, will return true
