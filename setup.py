from setuptools import setup , find_packages
from typing import List

def get_requirements(path:str)->List[str]:
    requirements = []
    with open(path) as f:
        requirements=f.readlines()
        requirements = [req.replace('\n',' ') for req in requirements]

    if "-e ." in requirements:
        requirements.remove("-e .")



setup(
    name="mlproject",
    author='bhuvanesh_kp',
    author_email='bhuvaneshkpb@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/bhuvaneshkpb/mlproject',
    license='Apache License 2.0',
    install_requires=get_requirements('requirements.txt')
)