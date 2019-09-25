


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from tkinter import messagebox


class ImageGenerator(object):
	"""docstring for ImageGenerator"""

	def frame_dim(self,h,w):
		self.h = h
		self.w= w
		print(self.h)
		print(self.w)
		return True
		

	def generate(self,file,path,h,w):

		print(file)
		print(path)

		try :
			with open(file,'r+') as f:  
				data = f.read()
				print(data)

		except:
			messagebox.showerror("Error Msg", "File Not Found!")
			return False


			

		stopwords = set(STOPWORDS)

		wordcloud = WordCloud(
        # font_path='assets\\abc.otf',
        background_color='black',
        stopwords=stopwords,
        max_words=200,
        max_font_size=5, 
        scale=5,
        height= h,
        width= w,
        repeat=True,
        random_state=1 # chosen at random by flipping a coin; it was heads
    	).generate(str(data))
		
		try:
			plt.imsave(path,wordcloud)
			return True
		except Exception as e:
			return str(e)



		
