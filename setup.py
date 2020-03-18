import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wonderwords_mrmaxguns",
    version="0.0.1",
    author="Maxim Rebguns",
    author_email="mrmaxguns@gmail.com",
    description="A simple package for words in the english language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrmaxguns/wonderwordsmodule",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
