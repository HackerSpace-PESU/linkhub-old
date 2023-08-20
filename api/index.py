from flask import Flask, render_template, url_for, redirect
import json

app = Flask(__name__)

components = {}

# PAGE ENDPOINTS

@app.route('/')
def index():
    with open('api/static/data/index.json', 'r') as data:
        components = json.loads(data.read())['components']
    return render_template('main.html', 
    project_name="Sample",
    main_heading="HackerSpace",
    content="Some random shit",
    font_data="@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,700;1,400;1,700&family=Poppins&display=swap');",
    body_classes="font-pop",
    heading_classes="font-mono",
    content_classes="font-pop",
    subhead_classes="font-mono",
    components=components
    )

@app.route('/newpage')
def newpage():
    with open('api/static/data/newpage.json', 'r') as data:
        components = json.loads(data.read())['components']
    return render_template('main.html', 
    project_name="Sample",
    main_heading="HackerSpace",
    content="Some random shit",
    font_data="@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,700;1,400;1,700&family=Poppins&display=swap');",
    body_classes="font-pop",
    heading_classes="font-mono",
    content_classes="font-pop",
    subhead_classes="font-mono",
    components=components
    )

@app.route('/blah')
def blah():
    return redirect('somelink.com')

@app.route('/random')
def random():
    return redirect('someotherlink.com')

