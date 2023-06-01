from application import app
from application.services.Hydrawise import Hydrawise
from flask import request

hydrawise = Hydrawise()


@app.route('/controllers/schedules', methods=['GET'])
def get_controllers_schedules() -> dict:
    return hydrawise.get_schedules()


@app.route('/customers/details', methods=['GET'])
def get_customer_details() -> dict:
    return hydrawise.get_customer_details()


@app.route('/zones/<zone_id>/run', methods=['POST'])
def run_zone(zone_id: str) -> dict:
    run_time = request.args.get('run_time', 0)
    return hydrawise.run_zone(zone_id, run_time)
