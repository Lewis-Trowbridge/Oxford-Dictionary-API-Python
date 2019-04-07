import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Oxford Dictionaries API",
    version="0.0.1",
    author="Lewis Trowbridge",
    author_email="lewbob9927@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/lewbob9927/Oxford-Dictionary-API-Python",
    packages=setuptools.find_packages()
)