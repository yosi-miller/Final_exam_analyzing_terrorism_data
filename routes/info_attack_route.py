from flask import Blueprint
from services.logger_server import log_info, log_error

terrorise_attack_info_bp = Blueprint('terroristic_attack_info_bp', __name__)