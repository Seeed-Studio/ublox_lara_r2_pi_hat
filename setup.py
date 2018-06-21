#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
	from distutils.core import setup


setup(name='ublox_lara_r2',
      version='1.0.0',
      description='LTE Pi Hat using celluar module ublox lara r2 LTE Cat.1 driver',
      author='Lmabor Fang',
      author_email='',
      url='https://www.github.com/Seeed-Studio/LTE_Pi_Hat_ublox_lara_r2_python_module',
      license='MIT',
      scripts=["bin/rpirtscts"],
     )
