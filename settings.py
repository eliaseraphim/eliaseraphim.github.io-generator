from os.path import abspath, dirname, join

# set html files to write here
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
        'output/static/js/tooltip.js': 'static/js/tooltip.js',
    },
}

# update file sets to include
FILENAME_SETS = (
    HTML_FILENAMES['root'],
    STATIC_FILENAMES['css'],
    STATIC_FILENAMES['js'],
)

# PATHS
BASE_DIR = dirname(abspath(__file__))  # base directory
TEMPLATE_DIR = join(BASE_DIR, 'templates')  # template directory
