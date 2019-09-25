
from tkinter import *
from interfacee import user_interface as UI


def app():
	
	root = Tk()
	root.geometry("500x600+300+50")
	root.resizable(False,False)
	root.title("WordCloud Image Generator")

	frame = UI(root)
	frame.place()

	root.mainloop()

if __name__ == '__main__':
	app()
