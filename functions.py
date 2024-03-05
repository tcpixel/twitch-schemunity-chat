import tkinter as tk
import pyperclip
import random
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
# partyEmotes.append("Custom")

customEmotes = []
def customEmoteEingabe(sv):
    eingabe = sv.get()
    global customEmotes
    customEmotes = eingabe.split(" ")
    # print(customEmotes)

    # partyEmotes[len(partyEmotes)-1]

def generate_party(amount, randomize, partyEmoteValues):
    text = ""
    more = True
    allEmotes = partyEmoteValues
    for emote in customEmotes:
        allEmotes[emote] = partyEmoteValues["Custom"].get()
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