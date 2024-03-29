import tkinter as tk
import pyperclip
import random
import pyautogui
import time
import win32gui
from multiprocessing import Process
from config import *

def insert_text(text, textbox):
    textbox.delete('1.0', tk.END)
    textbox.insert(tk.END, text)

def copy_to_clipboard(text_to_copy):
    pyperclip.copy(text_to_copy)

def ueberflausch(chacoEmotes):
    text = ""
    for element in "ÜBERFLAUSCH":
        text += "schemfChaco " if chacoEmotes.get() else "schemfUel "
        text += (element+" ")
    text += "schemfChaco" if chacoEmotes.get() else "schemfUel"
    return text

def schemfuel():
    text = ""
    for element in "SCHEMFUEL":
        text += "schemfUel "
        text += (element+" ")
    text += "schemfUel"
    return text

def party_st():
    text = ""
    for element in "PARTY":
        text += "schemfParty "
        text += (element+" ")
    text += "schemfParty"
    return text

# Party Emotes
customEmotes = []
def customEmoteEingabe(sv):
    eingabe = sv.get()
    global customEmotes
    customEmotes = eingabe.split(" ")

def generate_party(amount, randomize, partyEmoteValues):
    text = ""
    more = True
    while more:
        if randomize:
            textToAdd = ""
            number = random.randint(0, len(partyEmotes)+len(customEmotes)-1)
            emote = partyEmotes[number] if number < len(partyEmotes) else customEmotes[number-len(partyEmotes)]
            if number < len(partyEmotes):
                textToAdd = ""
                if partyEmoteValues[emote].get():
                    for x in range(amount):
                        textToAdd += (emote + " ")
                if (len(textToAdd)+len(text)) <= twitchMax:
                    text += textToAdd
                else:
                    more = False
                    break
            else:
                textToAdd = ""
                if partyEmoteValues["Custom"].get():
                    for x in range(amount):
                        textToAdd += (emote + " ")
                if (len(textToAdd)+len(text)) <= twitchMax:
                    text += textToAdd
                else:
                    more = False
                    break
        else:
            for emote in partyEmotes:
                textToAdd = ""
                if partyEmoteValues[emote].get():
                    for x in range(amount):
                        textToAdd += (emote + " ")
                if (len(textToAdd)+len(text)) <= twitchMax:
                    text += textToAdd
                else:
                    more = False
                    break
            for emote in customEmotes:
                textToAdd = ""
                if partyEmoteValues["Custom"].get():
                    for x in range(amount):
                        textToAdd += (emote + " ")
                if (len(textToAdd)+len(text)) <= twitchMax:
                    text += textToAdd
                else:
                    more = False
                    break

    return text

# Emoji Text
def customEmoteTextEingabe(sv):
    global customEmoteText
    customEmoteText = sv.get()

def generate_emoji_text(emText, emoji):
    if emoji == "schemfCustom":
        emoji = customEmoteText
    text = ""
    for element in emText:
        text += (emoji+" ")
        text += (element+" ")
    text += emoji
    return text

# Auto Party
autoTypeState = "Stopped"
def auto_party(button, textbox, window, partySettings):
    global autoTypeState
    if autoTypeState == "Stopped":
        button.config(state="disabled")
        textbox.delete('1.0', tk.END)
        textbox.insert(tk.END, "Starting Auto-Type.\n")
        textbox.insert(tk.END, "Waiting for Twitch Active Window...\n")
        autoTypeState = "Waiting"
    
    if autoTypeState == "Waiting":
        active_window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if twitchWindowTitle in active_window_title:
            textbox.insert(tk.END, "Twitch detected. Starting Auto-Type.\n")
            autoTypeState = "Running"
    if autoTypeState == "Running":
        active_window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if twitchWindowTitle in active_window_title:
            copy_to_clipboard(generate_party(partySettings[0], partySettings[1], partySettings[2]))
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.1)
            pyautogui.press('enter')
        else:
            autoTypeState = "Stopped"
            textbox.insert(tk.END, "Autp-Type stopped.\n")
            button.config(state="enabled")

    if autoTypeState == "Waiting" or autoTypeState == "Running":
        window.after(autoTypeSleep, lambda: auto_party(button, textbox, window, partySettings)) 