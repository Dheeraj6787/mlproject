from setuptools import find_packages, setup

def get_requirements(file_path: str):
    requirements=[]
    with open(file_path) as data:
        requirements=data.readlines()
        requirements=[each.replace('\n',"") for each in requirements]
    return requirements[:-1]

setup(
    name="mlproject",
    version='0.0.1',
    author="Dheeraj Ragala",
    author_email="dheerajragala@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

) 