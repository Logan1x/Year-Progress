## Finding day of year
from datetime import datetime, date
from flask import Flask, render_template
import calendar
import os

app = Flask(__name__)


# Current date
doy = datetime.now().timetuple().tm_yday
 
# Current year

tday = date.today()
leap = calendar.isleap(tday.year)

#Calculating Year progress
if leap == True:
    item = (doy/366)*100
    item = int(item)
    yleap = 366
else:
    item = (doy/365)*100
    item = int(item)
    yleap = 365


@app.route("/")
def index():
    return render_template("index.html", item= item, doy = doy, yleap = yleap)

@app.route("/abc")
def abc():
    return render_template("abc.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)