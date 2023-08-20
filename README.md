# LinkHub
Tired of hopping across several link management sites to realize none of them match your taste? Or is the free version hindering your creativity? Presenting LinkHub, a link manager-shortener template to create your own standalone link management site, with added customized shortened links!

## Specs
* Frontend: Tailwind CSS
* Backend: Flask
* Deployment specially made for [Vercel](https://vercel.com/)


## Instructions for use
* Create a new repository using this as a template using the `Use this template` button above. Name it whatever you want.
* There are many files in this repository, but we are concerned with only these particular files/folders:
    * api/static/data/main.json
    * api/static/data/index.json
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
```json
{
    "endpoint": "/",
    "title": "",
    "file": "index.json"
}
```
The `endpoint` refers to the link that is used to visit the page. `title` is displayed in the title bar along with the `project_name`. The `file` is where the configuration of the page is stored, and should be under the `data/` directory.

---

### The index.json file
```json
{
    "components": [
        {
            "type": "heading",
            "label": "Heading"
        },

        {
            "type": "button",
            "label": "Button with Endpoint",
            "properties": {
                "link": "somelink.com",
                "endpoint": "/blah"
            }
        },

        {
            "type": "button",
            "label": "Button without Endpoint",
            "properties": {
                "link": "/newpage"
            }
        }
    ]
}

```

There are three types of components you can add to a page:
* **Heading:** This heading marks categories of buttons in the page.
* **Button with Endpoint:** This button opens a link, and the link is also added to the link shortener feature where you can access the link by visiting `domain.com/endpoint`.
* **Button without Endpoint:** This button opens a link to a page on the same website which already has an endpoint defined in `main.json`, so endpoint is not required.

Similarly, you can create multiple `.json` files for each page, and add the name in `main.json`.

---

## Working
Once the json files and the stylesheets are updated and pushed to the repository, a script runs in the background and generates all the endpoints required for the website to work. Once the generation happens for the first time, the repository can be used to deploy a site on Vercel. From then on, every push made to the repository automatically updates the files.


## Error Prevention
There is no error checking added yet, so ensure the following:
* The syntax of the json files is correct
* There are no duplicate endpoints


---
---

## Credits
Created by [SilicoFlare](https://github.com/SilicoFlare)<br>
Check out [LinkHub](https://github.com/SilicoFlare/linkhub) to create your own link manager-shortener.
