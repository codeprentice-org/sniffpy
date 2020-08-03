import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sniffpy",
    version="0.1-dev",
    author="Codeprentice",
    author_email="nb2838@columbia.edu",
    description="A package for mime-sniffing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codeprentice-org/sniffpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
