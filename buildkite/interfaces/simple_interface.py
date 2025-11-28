import pyautogui

def simple_choices(text_content:str,choices_buttons:list):
    #TODO:add a comment about this function after 
    return pyautogui.confirm(text=text_content, buttons=choices_buttons)
