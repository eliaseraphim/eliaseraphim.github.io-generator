import os
from jinja2 import Environment, FileSystemLoader

FILES = {
    'output/index.html': 'pages/index.html',
    'output/projects.html': 'pages/projects.html',
}

PATH = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(PATH, 'output')

TEMPLATE_ENVIRONMENT = Environment(
    autoescape=True,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
)

def clear():
    output_directory = os.listdir(OUTPUT_PATH)
    for item in output_directory:
        if item.endswith('.html'):
            os.remove(os.path.join(OUTPUT_PATH, item))

def render_template(filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(filename).render(context)

def create_site():
    for filename in FILES:
        with open(filename, 'w') as file:
            html = render_template(FILES[filename], {})
            file.write(html)


def main():
    clear()
    create_site()



if __name__=='__main__':
    main()
