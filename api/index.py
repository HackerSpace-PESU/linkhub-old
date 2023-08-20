from flask import Flask, render_template, url_for, redirect
import json

app = Flask(__name__)

components = {}

# PAGE ENDPOINTS

@app.route('/')
def index():
    with open('data/index.json', 'r') as data:
        components = json.loads(data.read())['components']
    return render_template('main.html', 
    project_name="Sample",
    main_heading="",
    content="",
    stylesheets=['', ''],
    body_classes="",
    heading_classes="",
    content_classes="",
    subhead_classes="",
    components=components
    )

@app.route('/newpage')
def newpage():
    with open('data/newpage.json', 'r') as data:
        components = json.loads(data.read())['components']
    return render_template('main.html', 
    project_name="Sample",
    main_heading="",
    content="",
    stylesheets=['', ''],
    body_classes="",
    heading_classes="",
    content_classes="",
    subhead_classes="",
    components=components
    )

@app.route('/blah')
def blah():
    return redirect('somelink.com')

@app.route('/random')
def random():
    return redirect('someotherlink.com')

