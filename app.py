from flask import Flask, render_template
import logging
from routes.data_route import data_bp
from dotenv import load_dotenv
from routes.info_attack_route import terrorise_attack_info_bp
load_dotenv()

logging.basicConfig(
    filename='project_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s - %(filename)s:%(lineno)d'
)

app = Flask(__name__)

app.register_blueprint(data_bp)

app.register_blueprint(terrorise_attack_info_bp, url_prefix='/terroristic_attack_info')
@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

# TODO: run on docker