from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Returns a list of requirements from the given requirements file.
    Removes lines like '-e .' and ignores empty lines or comments.
    """
    requirements = []
    with open(file_path, 'r') as file_obj:
        for line in file_obj:
            line = line.strip()
            if line and not line.startswith('-e') and not line.startswith('#'):
                requirements.append(line)
    return requirements

setup(
    name='mlprojects',
    version='0.0.1',
    author='Satyam',
    author_email='satyamsbindhani@gmail.com',
    packages=find_packages(),  # Finds all Python packages (folders with __init__.py)
    install_requires=get_requirements('requirements.txt')
)
