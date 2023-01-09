from jinja2 import Environment, FileSystemLoader
from settings import FILENAME_SETS, TEMPLATE_DIR, OUTPUT_DIRS

import os

TEMPLATE_ENVIRONMENT = Environment(
    autoescape=True,
    loader=FileSystemLoader(TEMPLATE_DIR),
)

def clear():
    for directory in OUTPUT_DIRS:
        directory_contents = os.listdir(directory)
        for item in directory_contents:
            if item.endswith(OUTPUT_DIRS[directory]):
                os.remove(os.path.join(directory, item))


def render_template(filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(filename).render(context)


def create_site():
    for filename_set in FILENAME_SETS:
        for filename in filename_set:
            with open(filename, 'w') as file:
                data = render_template(filename_set[filename], {})
                file.write(data)


def main():
    clear()
    create_site()


if __name__=='__main__':
    main()
