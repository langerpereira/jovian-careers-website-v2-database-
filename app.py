from flask import Flask, render_template, jsonify, request
from database import load_jobs_fromdb,load_job_fromdb

app = Flask(__name__)

@app.route("/")
def hello_jovian():
  result_dicts= load_jobs_fromdb()
  return render_template('home.html', 
                          jobs = result_dicts,
                          company_name ='Jovian')

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_fromdb()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_fromdb(id)
    if not job:
      return "Not Found", 404
    return render_template('jobpage.html',
                           job=job)

@app.route("/job/<id>/apply", methods=['POST'])
def apply_to_job(id):
  data = request.form
  return jsonify(data)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

 