from os import path

# Get the path for files
path_py = path.abspath(path.dirname(__file__))
path_images = path.normpath(path.join(path_py, '..', 'Images'))
path_font = path.normpath(path.join(path_py, '..', 'Fonts'))
path_level = path.normpath(path.join(path_py, '..', 'Levels'))
path_music = path.normpath(path.join(path_py, '..', 'Music'))

# Get an image file
def get_image(file):
    return path.join(path_images, file)
    
# Get a font file
def get_font(file):
    return path.join(path_font, file)
    
# Get a level
def get_level(file):
    return path.join(path_level, file)