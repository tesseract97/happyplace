from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)

import webbrowser
import json

@app.route("/")
@app.route("/<name>")
def goodmorning_message(name='Tessa', url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3a9fbf41-c8ae-4cd1-82d1-71b89bb8808f/depkg6m-6ab31913-dfdb-4eb6-b0cb-dbb92c8fe48c.jpg/v1/fill/w_1192,h_670,q_70,strp/ghostly_gate_by_andrewmaleskiart_depkg6m-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NzIwIiwicGF0aCI6IlwvZlwvM2E5ZmJmNDEtYzhhZS00Y2QxLTgyZDEtNzFiODliYjg4MDhmXC9kZXBrZzZtLTZhYjMxOTEzLWRmZGItNGViNi1iMGNiLWRiYjkyYzhmZTQ4Yy5qcGciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.uhbUKTI1xXRuakfG6Op4-0aOdqnszah7fovEpiz4SDI"):
    return render_template('basepage.html', name=name, url=url)

def opensites():
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    sites = open('favorite_sites.json')
    site_list = json.loads(sites)
    for i in site_list:
        return "<h1 style='color:blue'>Good morning</h1>"
    #urls = favorite_sites[sites]
    #print(urls)
    #webbrowser.get(chrome_path).open(url)


@app.route("/configs")
def addsite():
    #favorite_sites[sites]
    print("site added")

def deletesite():
    print("site deleted")

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="8088")

