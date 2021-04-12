import calendar
from datetime import datetime
import json
from flask import Flask, render_template
from flask_script import Manager, Command
from flask_weasyprint import HTML, CSS, render_pdf

app = Flask(__name__)
# configure your app

manager = Manager(app)

@manager.command
def create_quittance(date, date_paiement):
    "create pdf quittance"
    with open('data.json', 'r') as f:
        json_dict = json.load(f)
    splitdate = date.split('/')
    month_range=calendar.monthrange(int(splitdate[1]),int(splitdate[0]))
    firstday, lastday = month_range
    formatted_firstday = "01/" + date
    formatted_lastday = str(lastday) + "/" + date
    format = "%d/%m/%Y"
    today=datetime.now()
    today_str = today.strftime(format)
    for data in json_dict:
        html = render_template('quittance.html', data=data, firstday=formatted_firstday, lastday=formatted_lastday, today=today_str, paymentdate=date_paiement)
        pdf = render_pdf(HTML(string=html))
        HTML(string=html, base_url='.').write_pdf('quittance.pdf',  stylesheets=[CSS(filename='static/style.css')])


if __name__ == "__main__":
    manager.run()