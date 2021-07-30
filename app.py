# import app_qr_csv_gen
from flask import Flask, render_template, request
import pandas as pd
# import pandas as pd
import csv
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/submit', methods=['GET','POST'])
def submit():
    userdata = dict(request.form)
    Name = userdata["Name"][0]
    # Last_Name = userdata["Name"][0]
    Email = userdata["Email"][0]
    Contact = userdata["Contact"][0]
    Contact = userdata["Location"][0]
    # if len("FName") < 2 and len("LName") < 3 and len("Email") < 10 and len("Contact")<10 :
    #   return "Please submit valid data."

    # with open('data_places.csv', mode='a') as csv_file:
    #   data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #   data.writerow([First_Name,Last_Name,Email,Contact])

    df = pd.DataFrame(userdata, columns= [ 'Name','Email','Contact','Location'])
    df.to_csv('Data.csv')
    from app_qr_gen  import function2
    function2()
    return "Thank you! you will get your ticket on your email"

app.run(host='0.0.0.0', port=4000, debug=True)
