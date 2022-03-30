import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="bcolors",
    version='1.0.3',
    author="Yogesh Sharma",
    author_email="yks0000@gmail.com",
    description="A module for coloring print statement.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yks0000/bcolors",
    project_urls={
        "Bug Tracker": "https://github.com/yks0000/bcolors/issues",
    },
    license='GNU General Public License v3.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        'Natural Language :: English',
    ],
    package_dir={"": "bcolors"},
    packages=setuptools.find_packages(where=""),
    python_requires=">=3.6",
)

