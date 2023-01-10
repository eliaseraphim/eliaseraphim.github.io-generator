from jinja2 import Environment, FileSystemLoader
from settings import BASE_DIR, TEMPLATE_DIR, FILENAME_SETS

import os

TEMPLATE_ENVIRONMENT = Environment(
    autoescape=True,
    loader=FileSystemLoader(TEMPLATE_DIR),
)


def clean():
    def remove_file(_filename):
        file = os.path.join(BASE_DIR, _filename)
        if os.path.exists(file):
            os.remove(file)


    for filename_set in FILENAME_SETS:
        for filename in filename_set:
            remove_file(filename)


def create():
    def write_to_file(_filename):
        with open(_filename, 'w') as file:
            data = render_template(filename_set[filename], {})
            file.write(data)

    for filename_set in FILENAME_SETS:
        for filename in filename_set:
            create_file(filename)


def render_template(filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(filename).render(context)


def main():
    clean()
    create()


if __name__ == '__main__':
    main()
