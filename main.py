from flask import Flask, render_template, request, redirect

app = Flask("extendedScrapper")

@app.route("/")
def home():
  return render_template("test.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
  else:
    return redirect("/")
  return render_template("report.html",searchby=word)

#@app.route("/<username>")
#def contact(username):
#  return f"here is contact {username}"
app.run(host="0.0.0.0")
