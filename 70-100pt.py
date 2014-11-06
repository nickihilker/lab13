#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")
#these are the enemies
enemy1 = drawpad.create_rectangle(290,180,330,200, fill= 'blue')
enemy2 = drawpad.create_rectangle(490,280,530,300, fill= 'blue')
enemy3 = drawpad.create_rectangle(190,380,230,400, fill= 'blue')
direction = 1

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    self.up.bind("<Button-1>", self.upClicked)
       	    drawpad.pack(side=RIGHT)
       	    self.animate()
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "yellow")
       	    self.right.grid(row=1,column=1)
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    drawpad.pack(side=RIGHT)
       	    self.animate()
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "pink")
       	    self.down.grid(row=0,column=1)
       	    self.down.bind("<Button-1>", self.downClicked)
       	    drawpad.pack(side=RIGHT)
       	    self.animate()
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "black")
       	    self.left.grid(row=1,column=0)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
            global enemy1

	    global enemy2
	    
	    global enemy3
	    global direction
	    x1, y1, x2, y2 = drawpad.coords(enemy1)
	    if x2 > drawpad.winfo_width(): 
                direction = - 5
            elif x1 < 0:
                direction = 5
	    # Uncomment this when you're ready to test out your animation!
	    drawpad.move(enemy1,direction*.5,0)
	    drawpad.move(enemy2,direction*-2,0)
	    drawpad.move(enemy3,direction,0)
	    drawpad.after(10,self.animate)
        def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)

app = MyApp(root)
root.mainloop()