from flask import Flask, render_template
import logging

from repository.csv_repository import init_information_from_main_csv
from routes.data_route import data_bp


# הגדרת פורמט הלוג כך שיכלול את הזמן, שם הקובץ ומספר השורה
logging.basicConfig(
    filename='project_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d'
)

app = Flask(__name__)

app.register_blueprint(data_bp)

@app.route('/home')
def home():
    # return render_template(
    #     'index.html')
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)

# TODO: run on docker
# TODO: add readme