from flask import Flask, render_template, jsonify
import json
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scenario/<scenario>/<path:scenario_path>')
def get_scenario(scenario, scenario_path):
    file_path = os.path.join('scenarios', scenario, f'{scenario_path}.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            scenario_data = json.load(f)
        return jsonify(scenario_data)
    else:
        return jsonify({'error': 'Scenario not found'}), 404

@app.route('/scenario/random/initial')
def get_random_scenario():
    scenarios = ['american_revolution', 'covid_lockdown', 'world_war_2', 'space_exploration']
    random_scenario = random.choice(scenarios)
    return get_scenario(random_scenario, 'initial')

if __name__ == '__main__':
    app.run(debug=True, port=12001)
