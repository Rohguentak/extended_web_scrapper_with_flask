from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from save_as_csv import save_to_file



app = Flask("extendedScrapper")

db = {}

@app.route("/")
def home():
  return render_template("test.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    existingjobs = db.get(word)
    if existingjobs:
      job_result = existingjobs
    else:
      job_result = get_jobs(word)
      db[word] = job_result
  else:
    return redirect("/")
  
  return render_template("report.html",searchby=word,jobnum=len(job_result), jobs=job_result)

@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs)
    return send_file("job_info.csv")
  except:
    return redirect("/")

#@app.route("/<username>")
#def contact(username):
#  return f"here is contact {username}"
app.run(host="0.0.0.0")
