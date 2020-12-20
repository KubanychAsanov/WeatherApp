from tkinter import *
import requests
from PIL import ImageTk, Image
from func import format_response

root = Tk()
class Weather:
	def __init__(self,k):
		self.HEIGHT = 600
		self.WIDTH = 800
		self.file = open('History.txt', 'a')

		self.canvas = Canvas(root, height=self.HEIGHT, width=self.WIDTH)
		self.canvas.pack()

		self.background_image = ImageTk.PhotoImage(Image.open('rain.jpg'))
		self.background_label = Label(root, image=self.background_image)
		self.background_label.place(relwidth=1, relheight=1)
			
		self.frame = Frame(root, bg="gray", bd=5)
		self.frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

		self.entry = Entry(self.frame,font=("Courier", 18))
		self.entry.place(relwidth=0.65, relheight=1)

		self.lower_frame = Frame(root, bg="gray", bd=10)
		self.lower_frame.place(relx=0.5, rely=0.25, relheight=0.6, relwidth=0.75, anchor="n")

		self.label = Label(self.lower_frame, font=('Courier', 18),anchor="nw", justify="left", bd=4)
		self.label.place(relwidth=1, relheight=1)

		self.label_1 = Label(root, text="Write the city.", font=("Courier",17))
		self.label_1.place(relx=0.13, rely=0.045)

		self.button = Button(self.frame, text="Get Weather", font=("Courier",17), command=lambda: self.get_weather(self.entry.get()))
		self.button.place(relx=0.7, relheight=1, relwidth=0.3)
		root.bind("<Return>",func=lambda event : self.get_weather(self.entry.get()))
			
	def get_weather(self, city):
		self.weather_key = "b447c1a7213b24edcff904cb1a82a55f"
		self.url = "https://api.openweathermap.org/data/2.5/weather"
		self.params = {'APPID': self.weather_key, 'q': city, 'units': 'metric'}
		self.response = requests.get(self.url, params=self.params)
		self.answer = self.response.json()
		self.file.write(format_response(self.answer))
		self.label['text'] = format_response(self.answer)
			
f = Weather(root)		
root.title("Weather")
root.mainloop()