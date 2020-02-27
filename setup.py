from setuptools import setup, find_packages
from pathlib import Path

with Path('README.md').open() as readme:
    readme = readme.read()

version = "0.1"

setup(
    name='pysexpr',
    version=version if isinstance(version, str) else str(version),
    keywords=
    "Python, RBNF.hs, DSL, Novel, GalGame",
    description="GalNovel Doc DSL",
    long_description=readme,
    long_description_content_type="text/markdown",
    license='mit',
    python_requires='>=3.5.0',
    url='https://github.com/GalMaker/PyNovelDoc',
    author='lfkdsk',
    author_email='lfkdsk@gmail.com',
    packages=find_packages(),
    entry_points={"console_scripts": []},
    install_requires=['attrs', 'rbnf-rts>=1.0'],
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)
