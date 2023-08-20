from flask import Flask, render_template, url_for, redirect
import json

app = Flask(__name__)

components = {}

# ERROR LINKS
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html',
    title="Not Found",
    project_name="Linkhub",
    main_heading="404",
    content="The requested URL was not found. Check the URL and try again.",
    stylesheets=[
        "<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono&family=Poppins&display=swap');</style>", 
        '<link rel="stylesheet" href="{{ url_for(\'static\', filename=\'linkhub.css\') }}"></link>'
    ],
    body_classes="font-pop",
    heading_classes="font-hsp",
    content_classes="font-pop",
    subhead_classes="",
    button_classes="rounded-md bg-black text-white",
    components=[
        {
            "type": "heading",
            "label": " "
        },
        {
            "type": "button",
            "label": "Go Back",
            "properties": {
                "link": "history.back()"
            }
        }
    ]
    )

@app.errorhandler(500)
def server_error(error):
    return render_template('error.html',
    title="Internal Server Error",
    project_name="Linkhub",
    main_heading="500",
    content="There was some error with the server. Please try later, or check for errors.",
    stylesheets=[
        "<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono&family=Poppins&display=swap');</style>", 
        '<link rel="stylesheet" href="{{ url_for(\'static\', filename=\'linkhub.css\') }}"></link>'
    ],
    body_classes="font-pop",
    heading_classes="font-hsp",
    content_classes="font-pop",
    subhead_classes="",
    button_classes="rounded-md bg-black text-white",
    components=[
        {
            "type": "heading",
            "label": " "
        },
        {
            "type": "button",
            "label": "Go Back",
            "properties": {
                "link": "history.back()"
            }
        }
    ]
    )
    
# PAGE ENDPOINTS

@app.route('/')
def index():
    with open('data/index.json', 'r') as data:
        components = json.loads(data.read())['components']
    return render_template('main.html', 
    title="",
    project_name="Sample",
    main_heading="",
    content="",
    stylesheets=['', ''],
    body_classes="",
    heading_classes="",
    content_classes="",
    subhead_classes="",
    button_classes="",
    components=components
    )

@app.route('/newpage')
def newpage():
    with open('data/newpage.json', 'r') as data:
        components = json.loads(data.read())['components']
    return render_template('main.html', 
    title="",
    project_name="Sample",
    main_heading="",
    content="",
    stylesheets=['', ''],
    body_classes="",
    heading_classes="",
    content_classes="",
    subhead_classes="",
    button_classes="",
    components=components
    )

@app.route('/blah')
def blah():
    return redirect('somelink.com')

@app.route('/random')
def random():
    return redirect('someotherlink.com')

