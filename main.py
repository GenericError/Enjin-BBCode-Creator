""" A BBcode creator for Enjin, entirely written in Python """

import easygui
import pyperclip

colour_dictionary = {
    "1": "#FF0000",
    "2": "#FF3A00",
    "3": "#FF5800",
    "4": "#FF9300",
    "5": "#FFB000",
    "6": "#FFCD00",
    "7": "#FFEB00",
    "8": "#F5FF00",
    "9": "#D7FF00",
    "10": "#BAFF00",
    "11": "#9CFF00",
    "12": "#62FF00",
    "13": "#44FF00",
    "14": "#27FF00",
    "15": "#00FF13",
    "16": "#00FF31",
    "17": "#00FF4E",
    "18": "#00FF6B",
    "19": "#00FF89",
    "20": "#00FFA6",
    "21": "#00FFE1",
    "22": "#00FEFF",
    "23": "#00C4FF",
    "24": "#00A6FF",
    "25": "#006BFF",
    "26": "#004EFF",
    "27": "#0031FF",
    "28": "#0013FF",
    "29": "#0900FF",
    "30": "#2700FF",
    "31": "#4400FF",
    "32": "#7F00FF",
    "33": "#9C00FF",
    "34": "#D700FF",
    "35": "#F500FF",
    "36": "#FF00EB",
    "37": "#FF00CD",
    "38": "#FF00B0",
    "39": "#FF0075",
    "40": "#FF0058",
    "41": "#FF003A",
    "42": "#FF001D",
}

bold_tags = ['[b]', '[/b]']
italic_tags = ['[i]', '[/i]']
underline_tags = ['[u]', '[/u]']
strikethrough_tags = ['[s]', '[/s]']
colour_tags = ["[color=HEXA_CODE]", "[/color]"]

version = "0.0.2"

program_title = "Enjin-BBCode-Creator version " + version

text_to_use = easygui.enterbox(msg="Enter the text:", title=program_title,
                               strip=True)
bold_text = easygui.ynbox(msg="Do you want bold text?", title=program_title)
italic_text = easygui.ynbox(msg="Do you want italic text?", title=program_title)
underlined_text = easygui.ynbox(msg="Do you want underlined text?", title=program_title)
strikethrough_text = easygui.ynbox(msg="Do you want text with a strikethrough?", title=program_title)
while 1:
    size = easygui.integerbox(msg = "What size of text? Enter a number between 1 and 7, or 0 for the default size", title = program_title, upperbound = 7, lowerbound = 0)
    if size < 8 and size >= 0:
        break
    else:
        easygui.msgbox(msg="Woah, that wasn't a valid number! Try again!", title = program_title)

colour_incrementer = 0
colourized_string = ""
for letter in text_to_use:
    colour_incrementer += 1
    string_this_loop = ""
    string_this_loop += str(colour_tags[0]).replace("HEXA_CODE", colour_dictionary[str(colour_incrementer)])
    if underlined_text:
        string_this_loop += underline_tags[0]
    if strikethrough_text:
        string_this_loop += strikethrough_tags[0]
    string_this_loop += letter
    if underlined_text:
        string_this_loop += underline_tags[1]
    if strikethrough_text:
        string_this_loop += strikethrough_tags[1]
    string_this_loop += colour_tags[1]
    colourized_string += string_this_loop
    if colour_incrementer == 42:
        colour_incrementer = 0

start_tags = ""
end_tags = ""

if bold_text:
    start_tags += bold_tags[0]
    end_tags += bold_tags[1]
if italic_text:
    start_tags += italic_tags[0]
    end_tags += italic_tags[1]
if size != 0:
    start_tags += "[size=" + str(size) + "]"
    end_tags += "[/size]"

final_string = start_tags + colourized_string + end_tags

easygui.codebox(msg="Here is your text! Press OK to copy it to the clipboard", title = program_title, text = final_string)
pyperclip.copy(final_string)
easygui.msgbox(msg = "Thanks for using the program! The text is now on your clipboard. Bye bye!", title = program_title)
