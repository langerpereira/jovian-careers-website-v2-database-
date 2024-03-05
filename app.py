from flask import Flask, render_template, jsonify
from database import load_jobs_fromdb

app = Flask(__name__)

@app.route("/")
def hello_jovian():
  result_dicts= load_jobs_fromdb()
  return render_template('home.html', 
                          jobs = result_dicts,
                          company_name ='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

