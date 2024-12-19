from flask import Blueprint
from repository.csv_repository import init_crash_information_from_csv
from services.logger_server import log_info, log_error

data_bp = Blueprint('data_bp', __name__)

@data_bp.route('/init_main_data', methods=['GET'])
def insert_information_from_main_csv():
    try:
        init_crash_information_from_csv()
        response = {"status": "success", "message": "Initialization complete"}
        log_info(response)

        return response, 200
    except Exception as e:
        response = {"status": "error", "message": str(e)}
        log_error(response)

        return response, 400