from setuptools import setup, find_packages

setup(
    name="kom_python_logging",
    version="0.2",
    packages=find_packages(),
    install_requires=[],
    author="Jared Kominsky",
    author_email="83463012+jaredkominsky@users.noreply.github.com",
    description="A logging package for Python applications",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KominskyOrg/kom-python-logging",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
