import json

main_code = '''from flask import Flask, render_template, url_for, redirect
import json

app = Flask(__name__)

components = {}

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
    project_name="{meta['project_name']}",
    main_heading="{meta['page_content']['main_heading']}",
    content="{meta['page_content']['content']}",
    stylesheets={meta['page_content']['styles']['stylesheets']},
    body_classes="{meta['page_content']['styles']['body_classes']}",
    heading_classes="{meta['page_content']['styles']['heading_classes']}",
    content_classes="{meta['page_content']['styles']['content_classes']}",
    subhead_classes="{meta['page_content']['styles']['subhead_classes']}",
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
