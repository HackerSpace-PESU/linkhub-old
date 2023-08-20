# LinkHub
Tired of hopping across several link management sites to realize none of them match your taste? Or is the free version hindering your creativity? Presenting LinkHub, a link manager-shortener template to create your own standalone link management site, with added customized shortened links!

## Specs
* Frontend: Tailwind CSS
* Backend: Flask
* Deployment specially made for [Vercel](https://vercel.com/)


## Instructions for use
* Create a new repository using this as a template using the `Use this template` button above. Name it whatever you want.
* There are many files in this repository, but we are concerned with only these particular files/folders:
    * api/static/data/
    * api/static/data/main.json
    * api/static/styles.css

### The main.json file
The main.json file is where all the main data about your site goes. It has two parts, the metadata and the pages.

main.json
```json
{
    "project_name": "Sample",
    
    "page_content": {
        "main_heading": "",
        "content": "",
        "styles": {
            "stylesheets": [
                "", 
                ""
            ],
            "body_classes": "",
            "heading_classes": "",
            "content_classes": "",
            "subhead_classes": "",
            "button_classes": ""
        }
    },

    "pages": [
        {
            "endpoint": "/",
            "title": "",
            "file": "index.json"
        },
        {
            "endpoint": "/newpage",
            "title": "",
            "file": "newpage.json"
        }
    ]
}
```

Here is a description about each property:
* `project_name`: The name of the project, shown in the title bar
* `main_heading`: Shown in large letters in each page you create
* `content`: Shown below the main_heading. Describe your site or organization.
* `stylesheets`: Add `<link>` tags to external stylesheets in multiple lines to use in the website.
* `body_classes`: Tailwind or custom classes to use to style the body
* `heading_classes`: Tailwind or custom classes to use to style the heading
* `content_classes`: Tailwind or custom classes to use to style the content
* `subhead_classes`: Tailwind or custom classes to use to style the subheadings
* `button_classes`: Tailwind or custom classes to use to style the buttons

The `pages` section lists the pages that should be in your website.