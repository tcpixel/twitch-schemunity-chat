import tkinter as tk
from tkinter import ttk, StringVar
import pyperclip
import random
import sv_ttk

def on_button_click():
    print(checkbox1_var.get())

chacoEmotes = True

root = tk.Tk()
root.title("Schemunity Twitch Chat")
twitchMax = 500

# Erstellen eines Tab-Widgets
tab_control = ttk.Notebook(root)

#####
# Tab 1 - Standards
#####
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Standards')
tab_control.pack(expand=1, fill="both")
left_frame_1 = ttk.Frame(tab1)
left_frame_1.pack(side=tk.LEFT, padx=10)
right_frame_1 = ttk.Frame(tab1)
right_frame_1.pack(side=tk.LEFT, padx=10)

# Checkbox 
chacoEmotes = tk.BooleanVar(value=True)
checkbox1 = ttk.Checkbutton(left_frame_1, text='Chaco Emotes', variable=chacoEmotes, onvalue=True, offvalue=False)
checkbox1.pack(pady=15)

def ueberflausch():
    text = ""
    for element in "ÜBERFLAUSCH":
        text += "schemfChaco " if chacoEmotes.get() else "schemfUel "
        text += (element+" ")
    text += "schemfChaco" if chacoEmotes.get() else "schemfUel"
    textbox1.delete('1.0', tk.END)
    textbox1.insert(tk.END, text)
button1 = ttk.Button(left_frame_1, text="Überflausch", command=ueberflausch)
button1.pack(pady=3)

def schemfuel():
    text = ""
    for element in "SCHEMFUEL":
        text += "schemfUel "
        text += (element+" ")
    text += "schemfUel"
    textbox1.delete('1.0', tk.END)
    textbox1.insert(tk.END, text)
button1 = ttk.Button(left_frame_1, text="Schemfuel", command=schemfuel)
button1.pack(pady=3)

def party_st():
    text = ""
    for element in "PARTY":
        text += "schemfParty "
        text += (element+" ")
    text += "schemfParty"
    textbox1.delete('1.0', tk.END)
    textbox1.insert(tk.END, text)
button1 = ttk.Button(left_frame_1, text="Party", command=party_st)
button1.pack(pady=3)

# Rechte Seite
textbox1 = tk.Text(right_frame_1, height=30, width=40)
textbox1.pack(pady=10)

def copy_to_clipboard1():
    text_to_copy = textbox1.get('1.0', tk.END).strip()
    pyperclip.copy(text_to_copy)
    print("Text copied to clipboard:", text_to_copy)
button1 = ttk.Button(right_frame_1, text="Copy to Clipboard", command=copy_to_clipboard1)
button1.pack(pady=3)


#####
# Tab 2 - Party
#####
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Party')
tab_control.pack(expand=1, fill="both")
left_frame_2 = ttk.Frame(tab2)
left_frame_2.pack(side=tk.LEFT, padx=10)
right_frame_2 = ttk.Frame(tab2)
right_frame_2.pack(side=tk.LEFT, padx=10)

# Emotes
partyEmotes = ["schemfParty", "schemfUel", "silver1032Dance", "PartyParrot", "xar2EDM", "BirbRave", "DinoDance", "GoatEmotey", "catJAM", "Gandalf", "schemfPikdwiffel"]
partyEmotes.append("Custom")
partyEmoteValues = {}
for emote in partyEmotes:
    partyEmoteValues[emote] = tk.BooleanVar(value=True) if emote != "Custom" else tk.BooleanVar(value=False)

dropdown2 = ttk.Combobox(left_frame_2, values=["1", "2", "4", "Random"])
dropdown2.current(0)
dropdown2.pack(pady=5)

for emote in partyEmotes:
    checkbox = ttk.Checkbutton(left_frame_2, text=emote, variable=partyEmoteValues[emote], onvalue=True, offvalue=False)
    checkbox.pack(pady=3, anchor=tk.W)

# Custom Textfeld
def callback(sv):
    partyEmotes[len(partyEmotes)-1] = str(sv.get())
    # print(sv.get())
customEmote = StringVar()
customEmote.trace("w", lambda name, index, mode, sv=customEmote: callback(sv))
entry1 = ttk.Entry(left_frame_2, textvariable=customEmote)
entry1.pack(pady=3)

# Generate
def generate_party():
    text = ""
    more = True
    while more:
        if dropdown2.get() == "Random":
            textToAdd = ""
            emote = partyEmotes[random.randint(0, len(partyEmotes)-1)]
            if emote not in partyEmoteValues:
                if partyEmoteValues["Custom"].get():
                    textToAdd += (emote + " ")
            else:
                if partyEmoteValues[emote].get():
                    textToAdd += (emote + " ")
            if (len(textToAdd)+len(text)) <= twitchMax:
                text += textToAdd
            else:
                more = False
        else:
            for emote in partyEmotes:
                textToAdd = ""
                if emote not in partyEmoteValues:
                    if partyEmoteValues["Custom"].get():
                        for x in range(int(dropdown2.get())):
                            textToAdd += (emote + " ")
                else:
                    if partyEmoteValues[emote].get():
                        for x in range(int(dropdown2.get())):
                            textToAdd += (emote + " ")
                if (len(textToAdd)+len(text)) <= twitchMax:
                    text += textToAdd
                else:
                    more = False
                    break

    textbox2.delete('1.0', tk.END)
    textbox2.insert(tk.END, text)
button2 = ttk.Button(left_frame_2, text="Generate", command=generate_party)
button2.pack(pady=5)



textbox2 = tk.Text(right_frame_2, height=30, width=40)
textbox2.pack(pady=10)

def copy_to_clipboard2():
    text_to_copy = textbox2.get('1.0', tk.END).strip()
    pyperclip.copy(text_to_copy)
    print("Text copied to clipboard:", text_to_copy)
button2 = ttk.Button(right_frame_2, text="Copy to Clipboard", command=copy_to_clipboard2)
button2.pack(pady=3)

# Tab 3
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Emoji Text')
tab_control.pack(expand=1, fill="both")

# Button, Dropdown-Menü und Texteingabefeld für Tab 3
button3 = ttk.Button(tab3, text="Button", command=on_button_click)
button3.pack(pady=10)

options3 = ['Option X', 'Option Y', 'Option Z']
dropdown3 = ttk.Combobox(tab3, values=options3)
dropdown3.current(0)
dropdown3.pack(pady=10)

entry3 = ttk.Entry(tab3)
entry3.pack(pady=10)

sv_ttk.set_theme("dark")
root.mainloop()
