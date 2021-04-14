
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
               
               languages += obj.get("name")
               languages += "," 

           currencies = ""
           for obj in json_parser["currencies"]:
               currencies += ","
               currencies += obj.get("name")

           rates = []
           for currency in json_parser["currencies"]:
               symbol = currency["code"]
               url2 = ("http://data.fixer.io/api/latest?access_key=0f74f9e3e64cb0c2ce6ec5230dc7592d&format=1&symbol=%s"%symbol)
               r2 = requests.get(url2)
               text2 = r2.text
               json_parser2 = json.loads(text2)
               rates.append(str(json_parser2["rates"][symbol]))

           return 'Country Data :\nCountry’s Full Name:'+json_parser["name"] +'\nCountry’s Capital:'+ json_parser["capital"]+'\nCountry’s Common Language:'+languages+ \
                  '\nCountry’s Currency Name:'+ currencies +'\nCountry’s Currency rate:'+','.join(map(str,rates))+"\n"


app.run(host='0.0.0.0')
































