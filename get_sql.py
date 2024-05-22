import os
from treeviz import treeviz

root_directory = '/media/taweret/HOME/Projects/freelance_student/templates'

def create_django_directory_tree(root):
    tree = {}
    for root_dir, dirs, files in os.walk(root):
        current_dir = tree
        path = root_dir.split(os.sep)[1:] 
        for dir_name in path:
            if dir_name not in current_dir:
                current_dir[dir_name] = {}
            current_dir = current_dir[dir_name]
    return tree

django_tree = create_django_directory_tree(root_directory)

treeviz(django_tree)