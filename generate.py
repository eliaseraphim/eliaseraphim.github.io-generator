from jinja2 import Environment, FileSystemLoader
from settings import BASE_DIR, FILENAME_SETS, TEMPLATE_DIR

import os

TEMPLATE_ENVIRONMENT = Environment(
    autoescape=True,
    loader=FileSystemLoader(TEMPLATE_DIR),
)


def clean():
    for filename_set in FILENAME_SETS:
        for filename in filename_set:
            file = os.path.join(BASE_DIR, filename)
            if os.path.exists(file):
                os.remove(file)


def create_site():
    for filename_set in FILENAME_SETS:
        for filename in filename_set:
            with open(filename, 'w') as file:
                data = render_template(filename_set[filename], {})
                file.write(data)


def render_template(filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(filename).render(context)


def main():
    clean()
    create_site()


if __name__ == '__main__':
    main()
