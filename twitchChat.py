import tkinter as tk
from tkinter import ttk, StringVar
import sv_ttk
# import functions

from functions import *

def on_button_click():
    print(checkbox1_var.get())

chacoEmotes = True

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

button3 = ttk.Button(right_frame_2, text="Copy to Clipboard", command=copy_to_clipboard(textbox2.get('1.0', tk.END).strip()))
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
# if __name__=="__main__":
root.mainloop()
