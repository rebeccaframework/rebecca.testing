from setuptools import setup, find_packages
import os

version = '0.0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

requires = [
    "pyramid",
    "pytest",
]

tests_require = [
]


setup(name='rebecca.testing',
      version=version,
      description="",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        ],
      keywords='',
      author='Atsushi Odagiri',
      author_email='aodagx@gmail.com',
      url='https://github.com/rebeccaframework/rebecca.testing',
      license='MIT',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['rebecca'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=tests_require,
      extras_require={
          "testing": tests_require,
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
