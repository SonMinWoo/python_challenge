from flask import Flask, render_template, request, redirect
from day9_stackoverflow import get_jobs

app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
  return render_template("index.html") #rendering html file

@app.route("/report")
def report():
  word = request.args.get("word")
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs:
      jobs = existingJobs
    else:
      jobs = get_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")
  return render_template("report.html", searchingBy=word, resultsNumber=len(jobs),
  jobs=jobs) #it can give variable/list/objects to html!

"""
@app.route("/<username>")
def contact(username):
  return f"Hello your name is {username} how are you?"
"""
app.run(host="0.0.0.0")