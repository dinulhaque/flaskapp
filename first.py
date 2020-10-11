from flask import  Flask, render_template
import requests
import json
import pandas
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    


    base_url = "https://gorest.co.in/public-api/products/"

    # Send get http request and using the json function to parse data
    page = requests.get(base_url).json()


    # New Dictionary to store the data
    Data = {

        'Id': [],
        'Name': [],
        'Price': [],
    }


    #For loop to store the data in the above dictionary
    for i in (page['data']):

        x = i['id']
        y = i['name']
        z = i['price']

        if x:
            Data['Id'].append(x)  # adding Id data to the dictionary
        else:
            Data['Id'].append('none')

        if y:
            # adding Name value to the dictionary declared above
            Data['Name'].append(y)
        else:
            Data['Name'].append('none')


        # same again but this time its for     value 'Price'
        if z:
            Data['Price'].append(z)
        else:
            Data['Price'].append('none')


    table = pd.DataFrame(Data, columns=['Name', 'Price'])
    table.index = table.index + 1



    table['Price'] = pd.to_numeric(table['Price'])

    #I am now sorting the price value to the highest first using the .sort_values function
    highprice = table.sort_values(by=['Price'], ascending=False)


    final = highprice[:5]

    """print(final)"""




    return render_template("index.html", tables = [final.to_html(classes='data')], titles = final.columns.values)



