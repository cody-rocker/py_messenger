# -*- coding: utf-8 -*-
from setuptools import setup

def readme():
	with open('README.rst') as f:
		return f.read()

setup(name='py_messenger',
	  version='0.1',
	  description='SMTP >> SMS client for Python',
	  long_description=readme(),
	  classifiers=[
	  	'Development Status :: 2 - Pre-Alpha',
	  	'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3'
      ],
	  url='',
	  author='Cody Rocker',
	  author_email='cody.rocker.83@gmail.com',
	  license='GNU/GPL',
	  packages=['messenger'],
	  install_requires=[],
	  scripts=['bin/py_messenger'],
	  include_package_data=True,
	  zip_safe=False)