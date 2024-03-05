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
left_frame_1 = ttk.Frame(tab1, borderwidth=10)
left_frame_1.pack(side=tk.LEFT, padx=10)
right_frame_1 = ttk.Frame(tab1, borderwidth=10)
right_frame_1.pack(side=tk.LEFT, padx=10)

# Rechte Seite
textbox1 = tk.Text(right_frame_1, height=30, width=40)
textbox1.pack(pady=10)

button1 = ttk.Button(right_frame_1, text="Copy to Clipboard", command=lambda: copy_to_clipboard(textbox1.get('1.0', tk.END).strip()))
button1.pack(pady=3)

# Linke Seite
chacoEmotes = tk.BooleanVar(value=True)
checkbox1 = ttk.Checkbutton(left_frame_1, text='Chaco Emotes', variable=chacoEmotes, onvalue=True, offvalue=False)
checkbox1.pack(pady=15, anchor=tk.W)

button1 = ttk.Button(left_frame_1, text="Überflausch", command=lambda: insert_text(ueberflausch(chacoEmotes), textbox1))
button1.pack(pady=3, anchor=tk.W)

button1 = ttk.Button(left_frame_1, text="Schemfuel", command=lambda: insert_text(schemfuel(), textbox1))
button1.pack(pady=3, anchor=tk.W)

button1 = ttk.Button(left_frame_1, text="Party", command=lambda: insert_text(party_st(), textbox1))
button1.pack(pady=3, anchor=tk.W)



#####
# Tab 2 - Party
#####
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Party')
tab_control.pack(expand=1, fill="both")
left_frame_2 = ttk.Frame(tab2, borderwidth=10)
left_frame_2.pack(side=tk.LEFT, padx=10)
right_frame_2 = ttk.Frame(tab2, borderwidth=10)
right_frame_2.pack(side=tk.LEFT, padx=10)

# Rechte Seite
textbox2 = tk.Text(right_frame_2, height=30, width=40)
textbox2.pack(pady=10)

button3 = ttk.Button(right_frame_2, text="Copy to Clipboard", command=lambda: copy_to_clipboard(textbox2.get('1.0', tk.END).strip()))
button3.pack(pady=3)

# Linke Seite
amount = tk.IntVar(value=2)
spinbox1 = ttk.Spinbox(left_frame_2, from_=1, to=6, textvariable=amount)
spinbox1.pack(pady=3, anchor=tk.W)
randomize = tk.BooleanVar(value=False)
checkboxR = ttk.Checkbutton(left_frame_2, text="Randomize", variable=randomize, onvalue=True, offvalue=False)
checkboxR.pack(pady=15, anchor=tk.W)

partyEmoteValues = {}
for emote in partyEmotes:
    partyEmoteValues[emote] = tk.BooleanVar(value=True)
partyEmoteValues["Custom"] = tk.BooleanVar(value=False)

for emote in partyEmotes:
    checkbox = ttk.Checkbutton(left_frame_2, text=emote, variable=partyEmoteValues[emote], onvalue=True, offvalue=False)
    checkbox.pack(pady=3, anchor=tk.W)
checkbox = ttk.Checkbutton(left_frame_2, text="Custom", variable=partyEmoteValues["Custom"], onvalue=True, offvalue=False)
checkbox.pack(pady=3, anchor=tk.W)

# Custom Textfeld
customEmote = StringVar()
customEmote.trace("w", lambda name, index, mode, sv=customEmote: customEmoteEingabe(sv))
entry1 = ttk.Entry(left_frame_2, textvariable=customEmote)
entry1.pack(pady=3)

# Generate
button2 = ttk.Button(left_frame_2, text="Generate", command=lambda: insert_text(generate_party(amount.get(), randomize.get(), partyEmoteValues), textbox2))
button2.pack(pady=5)


#####
# Tab 3 - Emoji Text
#####
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Emoji Text')
tab_control.pack(expand=1, fill="both")
left_frame_3 = ttk.Frame(tab3, borderwidth=10)
left_frame_3.pack(side=tk.LEFT, padx=10)
right_frame_3 = ttk.Frame(tab3, borderwidth=10)
right_frame_3.pack(side=tk.LEFT, padx=10)

# Rechte Seite
textbox3 = tk.Text(right_frame_3, height=30, width=40)
textbox3.pack(pady=10)

button4 = ttk.Button(right_frame_3, text="Copy to Clipboard", command=lambda: copy_to_clipboard(textbox3.get('1.0', tk.END).strip()))
button4.pack(pady=3)

# Linke Seite
emojiText = StringVar()
entry3 = ttk.Entry(left_frame_3, textvariable=emojiText)
entry3.pack(pady=10)

textEmoji = StringVar(value='schemfParty')
schemfParty = ttk.Radiobutton(left_frame_3, text='schemfParty', variable=textEmoji, value='schemfParty')
schemfParty.pack(pady=3, anchor=tk.W)
schemfUel = ttk.Radiobutton(left_frame_3, text='schemfUel', variable=textEmoji, value='schemfUel')
schemfUel.pack(pady=3, anchor=tk.W)
schemfLove = ttk.Radiobutton(left_frame_3, text='schemfLove', variable=textEmoji, value='schemfLove')
schemfLove.pack(pady=3, anchor=tk.W)
schemfPikdwiffel = ttk.Radiobutton(left_frame_3, text='schemfPikdwiffel', variable=textEmoji, value='schemfPikdwiffel')
schemfPikdwiffel.pack(pady=3, anchor=tk.W)
schemfCustom = ttk.Radiobutton(left_frame_3, text='Custom', variable=textEmoji, value='schemfCustom')
schemfCustom.pack(pady=3, anchor=tk.W)

customTextEmote = StringVar()
customTextEmote.trace("w", lambda name, index, mode, sv=customTextEmote: customEmoteTextEingabe(sv))
entry2 = ttk.Entry(left_frame_3, textvariable=customTextEmote)
entry2.pack(pady=3)

button5 = ttk.Button(left_frame_3, text="Generate", command=lambda: insert_text(generate_emoji_text(emojiText.get(), textEmoji.get()), textbox3))
button5.pack(pady=5)

sv_ttk.set_theme("dark")
# if __name__=="__main__":
root.mainloop()
