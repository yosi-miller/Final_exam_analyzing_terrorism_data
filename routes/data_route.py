from flask import Blueprint
from repository.csv_repository import init_crash_information_from_csv
from services.logger_server import log_info, log_error

data_bp = Blueprint('data_bp', __name__)

@data_bp.route('/init_main_data', methods=['GET'])
def insert_information_from_main_csv():
    result = init_crash_information_from_csv()
    if result[0]:
        response = {"status": "success", "message": result[1]}
        log_info(response)

        return response, 200
    else:
        response = {"status": "error", "message": result[1]}
        log_error(response)

        return response, 400