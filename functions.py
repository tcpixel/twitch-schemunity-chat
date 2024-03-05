import tkinter as tk
import pyperclip

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

