from flask import Flask, render_template, request, redirect
from scrapper import get_jobs
app = Flask("extendedScrapper")

@app.route("/")
def home():
  return render_template("test.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    job_result = get_jobs(word)
    print(job_result)
  else:
    return redirect("/")
  return render_template("report.html",searchby=word,jobresult=job_result)

#@app.route("/<username>")
#def contact(username):
#  return f"here is contact {username}"
app.run(host="0.0.0.0")
