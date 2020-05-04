import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wonderwords",
    version="1.1.8",
    author="Maxim Rebguns",
    author_email="mrmaxguns@gmail.com",
    include_package_data=True,
    description="A python package for random words and sentences in the english language (random word and sentence generator)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrmaxguns/wonderwordsmodule",
    packages=setuptools.find_packages(),
    package_data={'wonderwords': ['*.txt']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points = {
        'console_scripts': [
            'wonderwords = wonderwords.cmdline:main'
        ]
    }
)
