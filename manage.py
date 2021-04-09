import json
from flask import Flask, render_template
from flask_script import Manager, Command
from flask_weasyprint import HTML, render_pdf
from weasyprint import HTML

app = Flask(__name__)
# configure your app

manager = Manager(app)

@manager.command
def create_quittance(date):
    "create pdf quittance"
    with open('data.json', 'r') as f:
        json_dict = json.load(f)
    html = render_template('quittance.html')
    pdf = render_pdf(HTML(string=html))
    HTML(string=html).write_pdf('quittance.pdf')


if __name__ == "__main__":
    manager.run()