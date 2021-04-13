import flask
import requests
import json


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/Users/"rema egbaria"/Desktop/<string:country_name>',methods=['GET'])
def country(country_name):
           url = ("https://restcountries.eu/rest/v2/name/%s?fullText=true" % country_name)
           r = requests.get(url)
           text = r.text[1:(len(r.text) - 1)]
           json_parser = json.loads(text)


           languages = ""
           for obj in json_parser["languages"]:
               languages += ","
               languages += obj.get("name")

           currencies = ""
           for obj in json_parser["currencies"]:
               currencies += ","
               currencies += obj.get("name")

           url2 = ("http://data.fixer.io/api/latest?access_key=0f74f9e3e64cb0c2ce6ec5230dc7592d&format=1&symbols=ils")
           r2 = requests.get(url2)
           text2 = r2.text
           json_parser2 = json.loads(text2)


           return 'Country Data :\nCountry’s Full Name:'+json_parser["name"] +'\nCountry’s Capital:'+ json_parser["capital"]+'\nCountry’s Common Language:'+languages+ \
                  '\nCountry’s Currency Name:'+ currencies +'\nCountry’s Currency rate:'+str(json_parser2["rates"].get("ILS"))


app.run()
