from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name = "talepy",
    packages = [".", "talepy"],
    package_data={
        # root markdown files should be packaged
        '.': ['*.md'],
    },
    version = "0.5.0",
    description = "Distributed Transactions Helper",
    author = "Steve Brazier",
    author_email = "meadsteve@gmail.com",
    url = "https://github.com/meadsteve/talepy",
    keywords = ["saga", "distributed transaction"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        ],
    long_description = long_description,
    long_description_content_type='text/markdown'
)