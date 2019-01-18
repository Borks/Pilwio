import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pilwio-api",
    version="1.0.0",
    author="Borka Martin Orlov",
    author_email="borka.orlov@gmail.com",
    description="Python API wrapper for pilw.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Borks/Pilwio",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)