# coding:utf-8
from setuptools import setup, find_packages
import sys, os

version = '0.2.0'

setup(name='iyi',
      version=version,
      description="a terminal tool for youdao dictionary",
      long_description="""a terminal tool for youdao dictionary""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python youdao dictionary terminal',
      author='bonfy',
      author_email='foreverbonfy@163.com',
      url='https://github.com/bonfy/iyi',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'termcolor',
        'requests',
      ],
      entry_points={
        'console_scripts':[
            'iyi = iyi.iyi:main'
        ]
      },
)