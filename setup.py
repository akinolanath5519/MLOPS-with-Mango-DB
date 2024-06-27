from setuptools import setup, find_packages

def get_requirements(file_name: str) -> list:
    with open(file_name, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('-e')]

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.4"
REPO_NAME = "MlopsMangoDBpackage"
PKG_NAME = "mangoDBdatabaseautomation"
AUTHOR_USER_NAME = "akinolanath5519"
AUTHOR_EMAIL = "akinolanathaniel3026@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("requirements.txt"),
)
