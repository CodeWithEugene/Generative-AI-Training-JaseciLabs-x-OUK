from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/hello')
def get_hello():
    result = subprocess.run(
        ['/home/eugenius/Documents/Eugenius/Projects/Generative-AI-Training-JaseciLabs-x-OUK/assignment_1/jac-env/bin/jac', 'run', '/home/eugenius/Documents/Eugenius/Projects/Generative-AI-Training-JaseciLabs-x-OUK/assignment_1/cloud_service.jac'],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        return jsonify({"message": result.stdout.strip()})
    else:
        return jsonify({"error": result.stderr.strip()}), 500

if __name__ == '__main__':
    app.run(debug=True)
