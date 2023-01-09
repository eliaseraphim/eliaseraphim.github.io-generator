# eliaseraphim.github.io-generator

Generator Repository for Github Page
- Page: https://eliaseraphim.github.io/
- Repository: https://github.com/eliaseraphim/eliaseraphim.github.io

## Instructions
### Installing Packages:
```
mkvirtualenv -a PATH_TO_PROJECT eliaseraphim.github.io-generator
source PATH_TO_VENV
pip install jinja2==3.1.2
```

You can choose to include system site packages if you wish.

### To Add Files to Templates
- HTML
  - If page, create the file in `/templates.
    - Extend from `base.html`
  - If part of the structure, create the file in `/structure`.
    - Include the file in base.html.
    - If structure belongs to specific page:
      - Create subdirectory `/templates/structure/page` if it does not exist, and store file there.

### Update Generator
- For generator to work, you will need to update the `settings.py` file.
  - First update the following settings variables.
    - `HTML_FILENAMES`
      - `'root'`
        - Contains a dictionary of the HTML files to generate.
        - __Key__: Filename of output file, from `BASE_DIR`.
        - __Value__: Filename of template file, from `TEMPLATE_DIR`.
    - `STATIC_FILENAMES`
      - Contains two entries, which hold dictionaries:
        - `'css'`
          - Contains a dictionary of the CSS files to generate.
          - __Key__: Filename of output file, from `BASE_DIR`.
          - __Value__: Filename of template file, from `TEMPLATE_DIR`.
        - `'js'`
          - Contains a dictionary of the JS files to generate.
          - __Key__: Filename of output file from `BASE_DIR`.
          - __Value__: Filename of template file `TEMPLATE_DIR`.
  - Next, update `FILENAME_SETS` if you have created any new dictionaries for other directories.

### To Generate
`python generator.py`

## Dependencies
- Python
  - 3.10
- Packages
  - Jinja2==3.1.2
  - MarkupSafe==2.1.1