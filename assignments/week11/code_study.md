### Template for Code Reading Exercise

1. Where did you find the code and why did you choose it? (Provide the link)

https://github.com/acm-0/AdventureGame/tree/main/TkinterVersion 
---

1. What does the program do? What's the general structure of the program?

   (TkinterVersion/adventure.py)
- Main Game file
  -
- handling the GUI for a text based adventure game using Tkinter and initialising the game
- 1. importing libraries
- 2. importing files handling actions and sound (game engine) 
- 3. initialising the UI window from Tkinter
- 4. UI help button
- 5. Handling of possible events in interface (e. g. button pressed, item selected)
- 6. Updating GUI locations
- 7. Functions concerning commands
- 8. Setting up the GUI with text and button locations, images, texts, etc.
- 9. Running the functions in a clean manner to execute the game
---

1. Function analysis: pick one function and analyze it in detail:

ShowHelp(): 
- What does this function do?

It opens a window called "adventure help" where help information on the GUI is given. 
In said window, there is a graphic explaining the GUI interface with a legend (explanation) attached to it.
There also is a third little segment where the games main idea and the commands are explained.

- What are the inputs and outputs?

inputs: Tkinter library commands, image "HelpImage.png", 2 textbox-sets

output: a separate window displaying all of the above
- How does it work (step by step)?

first, a  tk window separate to the first one is created. A title is given ("Adventure Help"). Then, its size and background colour are defined.
Next, the image is opened and saved. The first textbox is created and 
the set containing its content is defined. Its size and place are set. Afterwards, the same is done 
with the second textbox, with the difference that an ok button is defined and assigned to the tk action of destroying the window named "top"

---

1. Takeaways: are there anything you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)

Code is structured in a nice, clear way. Lots of information is outsourced into other files and
notes used creatively to separate different parts. Code is taking text based adventure game to the next level
by adding a graphical interface with buttons and images. A bit slow and easily breakble though. Crashed once after a command.
Im considering using Tkinter the same way as I thought about improving my text based adventure game about a students life
with a graphical interface. 


1. What parts of the code were confusing or difficult at the beginning to understand?

As it is heavily using Tkinter, I had to look up a ot of the libraries commands (ex. tk.Toplevel()) to know whats going on.
A lot of code is also outsourced, as previously mentioned, which complicates the code study as you also need to look into these files.

- Were you able to understand what it is doing after your own research?

I think i got a good idea of what it is doing after reading on Tkinter.

---

Extra notes