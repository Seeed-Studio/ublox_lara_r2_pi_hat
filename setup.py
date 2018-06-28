#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup

with open('package_description.rst', 'r') as f:
	long_description = f.read()


setup(
      name='ublox-lara-r2',
      version='0.0.5',
      packages = find_packages(),
      description='LTE Pi Hat driver using celluar module ublox lara r2 LTE Cat.1.',
      long_description=long_description,
      author='Lambor',
      author_email='lanselambor@gmail.com',
      url='https://www.github.com/Seeed-Studio/ublox_lara_r2_pi_hat',
      license='MIT',
      scripts=["bin/rpirtscts"],
      classifiers=(
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "License :: OSI Approved :: MIT License",
          "Operating System :: POSIX :: Linux",
      ),
      keywords=['ublox lara r2', 'ublox', 'R211', 'R204', 'LTE', 'Cat.1'],
     )
