# eliaseraphim.github.io-generator

Generator Repository for Github Page
- Page: https://eliaseraphim.github.io/
- Repository: https://github.com/eliaseraphim/eliaseraphim.github.io

## Instructions
### Installing Packages:
```
mkvirtualenv -a PATH_TO_PROJECT eliaseraphim.github.io-generator
source PATH_TO_VEN
pip install jinja2==3.1.2
```

### To Run
`python generator.py`

### To Add Files to Templates
- HTML
  - If page, create the file in `/templates/pages`.
    - Extend from `base.html`
  - If part of the structure, create the file in `/structure`.
    - Include the file in base.html.
    - If structure belongs to specific page:
      - Create subdirectory `/templates/structure/page` if it does not exist, and store file there.

### Update Generator
- For generator to work, you will need to update the settings at the top of the file.
  - `HTML_FILES`
    - Contains a dictionary of the HTML files to generate.
    - __Key__: Filename of output file.
    - __Value__: Filename of template file.
  - `STATIC_FILES`
    - Contains two entries, which hold dictionaries:
      - `'css'`
        - Contains a dictionary of the CSS files to generate.
        - __Key__: Filename of output file.
        - __Value__: Filename of template file.
      - `'js'`
        - Contains a dictionary of the JS files to generate.
        - __Key__: Filename of output file.
        - __Value__: Filename of template file.

## Dependencies
- Python
  - 3.10
- Packages
  - Jinja2==3.1.2
  - MarkupSafe==2.1.1