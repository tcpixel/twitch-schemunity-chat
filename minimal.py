import tkinter as tk
from tkinter import ttk, StringVar
import sv_ttk
from functions import *

root = tk.Tk()
root.title("Schemunity Twitch Chat")

# Erstellen eines Tab-Widgets
tab_control = ttk.Notebook(root)

#####
# Tab 1 - Standards
#####
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Standards')
tab_control.pack(expand=1, fill="both")

chacoEmotes = tk.BooleanVar(value=True)
checkbox1 = ttk.Checkbutton(tab1, text='Chaco Emotes', variable=chacoEmotes, onvalue=True, offvalue=False)
# checkbox1.pack(pady=15, anchor=tk.W)
checkbox1.grid(row=0,column=0,columnspan=2, sticky='W', padx=5, pady=5)

button1 = ttk.Button(tab1, text="Überflausch", command=lambda: copy_to_clipboard(ueberflausch(chacoEmotes)))
button1.grid(row=1,column=0, sticky='W', padx=5, pady=5)
button1 = ttk.Button(tab1, text="Schemfuel", command=lambda: copy_to_clipboard(schemfuel()))
button1.grid(row=1,column=1, sticky='W', padx=5, pady=5)
button1 = ttk.Button(tab1, text="Party", command=lambda: copy_to_clipboard(party_st()))
button1.grid(row=1,column=2, sticky='W', padx=5, pady=5)


#####
# Tab 2 - Party
#####
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Party')
tab_control.pack(expand=1, fill="both")

amount = tk.IntVar(value=2)
spinbox1 = ttk.Spinbox(tab2, from_=1, to=6, textvariable=amount)
spinbox1.grid(row=0,column=0,columnspan=3, sticky='W', padx=5, pady=15)
randomize = tk.BooleanVar(value=False)
checkboxR = ttk.Checkbutton(tab2, text="Randomize", variable=randomize, onvalue=True, offvalue=False)
checkboxR.grid(row=0,column=3, sticky='W', padx=5, pady=15)

partyEmoteValues = {}
for emote in partyEmotes:
    partyEmoteValues[emote] = tk.BooleanVar(value=True)
partyEmoteValues["Custom"] = tk.BooleanVar(value=False)

col=0
for emote in partyEmotes:
    checkbox = ttk.Checkbutton(tab2, text=emote, variable=partyEmoteValues[emote], onvalue=True, offvalue=False)
    checkbox.grid(row=(col//4+1),column=(col%4), sticky='W', padx=5, pady=0)
    col+=1
checkbox = ttk.Checkbutton(tab2, text="Custom", variable=partyEmoteValues["Custom"], onvalue=True, offvalue=False)
checkbox.grid(row=(col//4+2),column=0, sticky='W', padx=5, pady=10)

customEmote = StringVar()
customEmote.trace("w", lambda name, index, mode, sv=customEmote: customEmoteEingabe(sv))
entry1 = ttk.Entry(tab2, textvariable=customEmote)
entry1.grid(row=(col//4+2),column=1, columnspan=2, sticky='W', padx=0, pady=10)

button2 = ttk.Button(tab2, text="Copy to Clipboard", command=lambda: copy_to_clipboard(generate_party(amount.get(), randomize.get(), partyEmoteValues)))
button2.grid(row=(col//4+2),column=3, sticky='E', padx=5, pady=10)


#####
# Tab 3 - Emoji Text
#####
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Emoji Text')
tab_control.pack(expand=1, fill="both")

emojiText = StringVar()
entry3 = ttk.Entry(tab3, textvariable=emojiText)
entry3.grid(row=0,column=0,columnspan=3, sticky='W', padx=5, pady=15)

textEmoji = StringVar(value='schemfParty')
schemfParty = ttk.Radiobutton(tab3, text='schemfParty', variable=textEmoji, value='schemfParty')
schemfParty.grid(row=1,column=0, sticky='W', padx=5, pady=5)
schemfUel = ttk.Radiobutton(tab3, text='schemfUel', variable=textEmoji, value='schemfUel')
schemfUel.grid(row=1,column=1, sticky='W', padx=5, pady=5)
schemfLove = ttk.Radiobutton(tab3, text='schemfLove', variable=textEmoji, value='schemfLove')
schemfLove.grid(row=1,column=2, sticky='W', padx=5, pady=5)
schemfPikdwiffel = ttk.Radiobutton(tab3, text='schemfPikdwiffel', variable=textEmoji, value='schemfPikdwiffel')
schemfPikdwiffel.grid(row=1,column=3, sticky='W', padx=5, pady=5)
schemfCustom = ttk.Radiobutton(tab3, text='Custom', variable=textEmoji, value='schemfCustom')
schemfCustom.grid(row=2,column=0, sticky='W', padx=5, pady=0)

customTextEmote = StringVar()
customTextEmote.trace("w", lambda name, index, mode, sv=customTextEmote: customEmoteTextEingabe(sv))
entry2 = ttk.Entry(tab3, textvariable=customTextEmote)
entry2.grid(row=2,column=1, columnspan=2, sticky='W', padx=5, pady=0)

button4 = ttk.Button(tab3, text="Copy to Clipboard", command=lambda: copy_to_clipboard(generate_emoji_text(emojiText.get(), textEmoji.get())))
button4.grid(row=2,column=3, sticky='E', padx=5, pady=0)

sv_ttk.set_theme("dark")
# if __name__=="__main__":
root.mainloop()
