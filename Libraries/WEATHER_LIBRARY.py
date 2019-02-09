import requests,json


def RequestData(APIKEY,endpoint):
	BaseURL = "http://api.openweathermap.org/data/2.5/"
	print"Sending request: " + BaseURL + endpoint + "&APPID=" + APIKEY
	response = requests.get(BaseURL + endpoint + "&APPID=" + APIKEY)
	if response.status_code == 200:
		data = json.loads(response.content.decode("utf-8"))
		return data
	else:
		if response.status_code == 401:
			print"Error 401: Not Authenticated."
		if response.status_code == 400:
			print"Error 400: Bad Request."
		if response.status_code == 403:
			print"Error 403: Access Denied."
		if response.status_code == 404:
			print"Error 404: Not Found"

def GetWeather(APIKEY,CityID):
	endpoint = "weather?id=%s"%(CityID)
	data = RequestData(APIKEY,endpoint)
	return data

APIKEY = raw_input("Enter API Key: ")
