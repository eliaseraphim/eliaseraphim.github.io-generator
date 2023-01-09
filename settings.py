from os.path import abspath, dirname, join

# html files to write
HTML_FILENAMES = {
    'root': {
        'output/index.html': 'index.html',
        'output/about.html': 'about.html',
        'output/projects.html': 'projects.html',
    }
}

# static files to write
STATIC_FILENAMES = {
    'css': {
        'output/static/css/style.css': 'static/css/style.css',
    },
    'js': {
        'output/static/js/buttons.js': 'static/js/buttons.js',
    },
}

FILENAME_SETS = (
    HTML_FILENAMES['root'],
    STATIC_FILENAMES['css'],
    STATIC_FILENAMES['js'],
)

# PATHS
BASE_DIR = dirname(abspath(__file__))  # base directory

TEMPLATE_DIR = join(BASE_DIR, 'templates')  # template directory

OUTPUT_DIR = join(BASE_DIR, 'output')  # output directory

# output directories to write to
OUTPUT_ROOT_HTML_DIR = OUTPUT_DIR
OUTPUT_ROOT_CSS_DIR = join(OUTPUT_DIR, 'static/css')
OUTPUT_ROOT_JS_DIR = join(OUTPUT_DIR, 'static/js')

# set directories to write to here
OUTPUT_DIRS = {
    OUTPUT_ROOT_HTML_DIR: 'html',
    OUTPUT_ROOT_CSS_DIR: 'css',
    OUTPUT_ROOT_JS_DIR: 'js',
}
