#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from setuptools import setup

setup(
    name='JackIt',
    version='0.1.0',
    author='infamy and phikshun',
    packages=['jackit', 'jackit.lib', 'jackit.plugins'],
    scripts=['bin/jackit'],
    url='https://github.com/insecurityofthings/jackit',
    license='BSD',
    description='Exploit framework for MouseJack vulnerability.',
    install_requires=[
        "click",
        "pyusb",
        "tabulate",
        "six"
    ],
)
