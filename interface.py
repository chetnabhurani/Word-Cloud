from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from cloud import ImageGenerator as ig
import re

class user_interface(Frame):

	def __init__(self,root):
		super().__init__(root)
		self.root = root

		super().__init__(root)
		self.root = root


		self.heading = Label(self.root, text="WordCloud Image Generator Tool", bg="#25CCF7", fg="black",font=("Courier 20 bold"))
		self.heading.place(x=0,y=0,width=500,height=44)

		self.height_l = Label(self.root, text="Enter Height : ", fg="black",font=("Times 14 bold"))
		self.height_l.place(x=10,y=90)

		self.h_entry = Entry(self.root)
		self.h_entry.place(x=151,y=86, height=30,width=124)


		self.width_l = Label(self.root, text="Enter Width : ", fg="black",font=("Times 14 bold"))
		self.width_l.place(x=10,y=140)


		self.w_entry = Entry(self.root)
		self.w_entry.place(x=151,y=138, height=30,width=124)


		self.fgen_btn=Button(self.root, text="Create Frame!",bg="#758AA2", fg="black", command= lambda: self.gen_frame())
		self.fgen_btn.place(x=325,y=110, width=135, height=30)

		self.path_l = Label(self.root, text="Enter Img Path : ", fg="black",font=("Times 14 bold"))
		self.path_l.place(x=10,y=210)

		self.p_entry = Entry(self.root)
		self.p_entry.place(x=151,y=212, height=30,width=124)

		self.file_l = Label(self.root, text="Enter Text File \nPath : ", fg="black",font=("Times 14 bold"))
		self.file_l.place(x=10,y=258)

		self.f_entry = Entry(self.root)
		self.f_entry.place(x=151,y=264, height=30,width=124)

		self.igen_btn=Button(self.root, text="Generate Image!",bg="#758AA2", fg="black", command= lambda: self.gen_img())
		self.igen_btn.place(x=325,y=240, width=135, height=30)

		self.author=Label(root,text="Designed & Developed by - Chetna",font=("Times 10"))
		self.author.place(x=300,y=580)



	def gen_frame(self):
		self.h = int(self.h_entry.get())
		self.w = int(self.w_entry.get())
		
		if ig().frame_dim(self.h,self.w):
			messagebox.showinfo("Success", "Frame Created Successfully!")

		else:
			
			messagebox.showerror("Error Msg", "Error in generating image! \n Height should be less than 50 \n Width should be less than 90")


	def gen_img(self):
		p = self.p_entry.get()
		f = self.f_entry.get()
		
		if ig().generate(f,p,self.h,self.w):
			messagebox.showinfo("Success", "Image Generated Successfully!")
			self.img = ImageTk.PhotoImage(Image.open(p))
			self.panel = Label(self.root, image = self.img)
			self.panel.place(x=15,y=320)
		else:
			self.clear_words()
			messagebox.showerror("Error Msg", "Error in generating image!")

	def clear_words(self):

		self.h_entry.delete(0, 'end')
		self.p_entry.delete(0, 'end')
		self.w_entry.delete(0, 'end')
		self.f_entry.delete(0, 'end')



		

