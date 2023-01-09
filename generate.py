import os
from jinja2 import Environment, FileSystemLoader

HTML_FILES = {
    'output/index.html': 'index.html',
    'output/about.html': 'about.html',
    'output/projects.html': 'projects.html',
}

STATIC_FILES = {
    'css': {'output/static/css/style.css': 'static/css/style.css'},
    'js': {'output/static/js/buttons.js': 'static/js/buttons.js'}
}

PATH = os.path.dirname(os.path.abspath(__file__))

ROOT_HTML_PATH = os.path.join(PATH, 'output')
STATIC_CSS_PATH = os.path.join(PATH, 'output/static/css')
STATIC_JS_PATH = os.path.join(PATH, 'output/static/js')

TEMPLATE_ENVIRONMENT = Environment(
    autoescape=True,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
)

def clear():
    root_html_directory = os.listdir(ROOT_HTML_PATH)
    static_css_directory = os.listdir(STATIC_CSS_PATH)
    static_js_directory = os.listdir(STATIC_JS_PATH)

    for item in root_html_directory:
        if item.endswith('.html'):
            os.remove(os.path.join(ROOT_HTML_PATH, item))

    for item in static_css_directory:
        if item.endswith('.css'):
            os.remove(os.path.join(STATIC_CSS_PATH, item))

    for item in static_js_directory:
        if item.endswith('.js'):
            os.remove(os.path.join(STATIC_JS_PATH, item))


def render_template(filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(filename).render(context)

def create_site():
    filename_sets = [HTML_FILES, STATIC_FILES['css'], STATIC_FILES['js']]

    for filename_set in filename_sets:
        for filename in filename_set:
            with open(filename, 'w') as file:
                data = render_template(filename_set[filename], {})
                file.write(data)


def main():
    clear()
    create_site()



if __name__=='__main__':
    main()
