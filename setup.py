#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup


setup(name='ublox-lara-r2',
      version='1.0.0',
      packages = find_packages(),
      description='LTE Pi Hat using celluar module ublox lara r2 LTE Cat.1 driver',
      author='Lmabor Fang',
      author_email='lanselambor@gmail.com',
      url='https://www.github.com/Seeed-Studio/ublox_lara_r2_pi_hat',
      license='MIT',
      scripts=["bin/rpirtscts"],
     )
