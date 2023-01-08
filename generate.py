import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html():
    filename = "output/output.html"
    context = {
        'sidebar': TEMPLATE_ENVIRONMENT.get_template('structure/sidebar.html')
    }

    with open(filename, 'w') as file:
        html = render_template('pages/index.html', context)
        file.write(html)


def main():
    create_index_html()


if __name__=='__main__':
    main()
