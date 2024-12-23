from flask import Blueprint, jsonify, request
from services.logger_server import log_error, log_info
from services.info_attack_server import calculate_top_attacks, calculate_average_casualties_by_area, \
    calculate_percentage_change_attacks_by_region, calculate_most_active_groups_by_region, \
    calculate_correlation_between_hitting_and_hits, calculate_groups_involved_in_same_attacks, \
    calculate_groups_most_involved_in_same_targets

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

@terrorise_attack_info_bp.route('/average_casualties_by_area', methods=['GET'])
def get_average_casualties_by_area():
    try:
        top_n = request.args.get('top_n', default=None, type=int)
        result = calculate_average_casualties_by_area(top_n)
        log_info(f"Average casualties by area fetched successfully")
        return jsonify(result), 200

    except Exception as e:
        log_error(f"Error fetching average casualties by area: {str(e)}")
        return jsonify({"error": "An error occurred"}), 500

@terrorise_attack_info_bp.route('/percentage_change_attacks_by_region', methods=['GET'])
def get_percentage_change_attacks_by_region():
    try:
        top_n = request.args.get('top_n', default=None, type=int)
        result = calculate_percentage_change_attacks_by_region(top_n)
        log_info(f"Percentage change in attacks by region fetched successfully")
        return jsonify(result), 200

    except Exception as e:
        log_error(f"Error fetching percentage change in attacks by region: {str(e)}")
        return jsonify({"error": "An error occurred"}), 500

@terrorise_attack_info_bp.route('/most_active_groups_by_region', methods=['GET'])
def get_most_active_groups_by_region():
    try:
        region = request.args.get('region', default=None, type=str)
        result = calculate_most_active_groups_by_region(region)
        log_info(f"Most active groups by region fetched successfully")
        return jsonify(result), 200

    except Exception as e:
        log_error(f"Error fetching most active groups by region: {str(e)}")
        return jsonify({"error": "An error occurred"}), 500

@terrorise_attack_info_bp.route('/correlation_between_hitting_and_hits', methods=['GET'])
def get_correlation_between_hitting_and_hits():
    try:
        result = calculate_correlation_between_hitting_and_hits()
        log_info(f"Correlation between hitting and hits calculated successfully")
        return jsonify({"correlation": result}), 200

    except Exception as e:
        log_error(f"Error calculating correlation between hitting and hits: {str(e)}")
        return jsonify({"error": "An error occurred"}), 500

@terrorise_attack_info_bp.route('/groups_involved_in_same_attacks', methods=['GET'])
def get_groups_involved_in_same_attacks():
    try:
        result = calculate_groups_involved_in_same_attacks()
        log_info(f"Groups involved in same attacks fetched successfully")
        return jsonify(result), 200

    except Exception as e:
        log_error(f"Error fetching groups involved in same attacks: {str(e)}")
        return jsonify({"error": "An error occurred"}), 500

@terrorise_attack_info_bp.route('/groups_most_involved_in_same_targets', methods=['GET'])
def get_groups_involved_in_same_targets():
    try:
        result = calculate_groups_most_involved_in_same_targets()
        log_info(f"Groups involved in same targets fetched successfully")
        return jsonify(result), 200

    except Exception as e:
        log_error(f"Error fetching groups involved in same targets: {str(e)}")
        return jsonify({"error": "An error occurred"}), 500