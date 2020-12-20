from datetime import *
today = datetime.today()
def format_response(answer):
	try:
		name =answer['name']
		desk = answer['weather'][0]['description']
		temp = answer['main']['temp']
		country = answer['sys']['country']

		final_str = "City: "+str(name)+"\nCountry: "+str(country)+"\nDescription: "+str(desk)+"\nTemperature: "+str(temp)+"\n                Time: "+str(today)+"\n\n"
	except:
		final_str = "There was a problem \nretrieving that information\n\n"

	return final_str
