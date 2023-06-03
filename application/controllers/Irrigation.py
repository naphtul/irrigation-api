from application import app
from application.services.Hydrawise import Hydrawise
from flask import request, send_from_directory

hydrawise = Hydrawise()


@app.route("/ui", defaults={'path': ''})
def ui(path):
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/controllers/schedules', methods=['GET'])
def get_controllers_schedules() -> dict:
    return hydrawise.get_schedules()


@app.route('/customers/details', methods=['GET'])
def get_customer_details() -> dict:
    return hydrawise.get_customer_details()


@app.route('/zones/<zone_id>', methods=['POST'])
def run_zone(zone_id: str) -> dict:
    run_time = request.args.get('run_time', 0)
    return hydrawise.run_zone(zone_id, run_time)

@app.route('/zones/<zone_id>', methods=['DELETE'])
def stop_zone(zone_id: str) -> dict:
    return hydrawise.stop_zone(zone_id)
