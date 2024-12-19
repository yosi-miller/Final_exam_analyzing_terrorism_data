from flask import Flask
import logging
from routes.data_route import data_bp
from dotenv import load_dotenv

load_dotenv()

# Setting the log format to include the time, file name and line number
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