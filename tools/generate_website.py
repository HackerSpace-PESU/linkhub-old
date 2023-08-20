import json

main_code = '''from flask import Flask, render_template, url_for, redirect
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
        '<link rel="stylesheet" href="{{ url_for(\\'static\\', filename=\\'linkhub.css\\') }}"></link>'
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
        '<link rel="stylesheet" href="{{ url_for(\\'static\\', filename=\\'linkhub.css\\') }}"></link>'
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

'''

with open('data/main.json', 'r') as mainfile:
    meta = json.loads(mainfile.read())

    for page in meta['pages']:
        main_code += f'''@app.route(\'{page["endpoint"]}\')
def {page["endpoint"][1:].replace('/', '_') if page["endpoint"] != '/' else 'index'}():
    with open('data/{page["file"]}', 'r') as data:
        components = json.loads(data.read())['components']
    return render_template('main.html', 
    title="{page['title']}",
    project_name="{meta['project_name']}",
    main_heading="{meta['page_content']['main_heading']}",
    content="{meta['page_content']['content']}",
    stylesheets={meta['page_content']['styles']['stylesheets']},
    body_classes="{meta['page_content']['styles']['body_classes']}",
    heading_classes="{meta['page_content']['styles']['heading_classes']}",
    content_classes="{meta['page_content']['styles']['content_classes']}",
    subhead_classes="{meta['page_content']['styles']['subhead_classes']}",
    button_classes="{meta['page_content']['styles']['button_classes']}",
    components=components
    )

'''
        
with open('data/main.json', 'r') as meta:
    fileList = json.loads(meta.read())['pages']

    for file in fileList:
        with open(f'data/{file["file"]}', 'r') as data:
            components = json.loads(data.read())['components']

            for cmp in components:
                if cmp['type'] == 'button':
                    if cmp['properties'].get('endpoint') != None:
                        main_code += f'''@app.route(\'{cmp['properties'].get('endpoint')}\')
def {cmp['properties'].get('endpoint')[1:].replace('/', '_')}():
    return redirect(\'{cmp['properties'].get('link')}\')

'''

styles = ''
with open('data/styles.css', 'r') as st:
    styles = st.read()                    


# Write processed data to index.py
with open('api/index.py', 'w') as finale:
    finale.write(main_code)

with open('api/static/styles.css', 'w') as fin:
    fin.write(styles)
