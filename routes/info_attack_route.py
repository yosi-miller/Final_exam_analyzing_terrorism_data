from flask import Blueprint, jsonify, request
from services.logger_server import log_error, log_info
from services.info_attack_server import calculate_top_attacks

terrorise_attack_info_bp = Blueprint('terroristic_attack_info_bp', __name__)

@terrorise_attack_info_bp.route('/top-attacks', methods=['GET'])
def get_top_attacks():
    try:
        top_n = request.args.get('top_n', default=None, type=int)
        result = calculate_top_attacks(top_n)
        log_info(f"Top attacks fetched successfully")
        return jsonify(result), 200

    except Exception as e:
        log_error(f"Error fetching top attacks: {str(e)}")
        return jsonify({"error": "An error occurred"}), 500
