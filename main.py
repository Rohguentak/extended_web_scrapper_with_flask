from flask import Flask, render_template, request

app = Flask("extendedScrapper")

@app.route("/")
def home():
  return render_template("test.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  return render_template("report.html",searchby=word)

#@app.route("/<username>")
#def contact(username):
#  return f"here is contact {username}"
app.run(host="0.0.0.0")
