# bootstrap easy_install
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

setup(
    name='pyzalgo',
    version='0.3',
    description="turn your text into ZALGO text",
    author="Mike Giarlo",
    author_email="michael.giarlo@gmail.com",
    url="http://github.com/mjgiarlo/pyzalgo",
    py_modules=['zalgo', 'ez_setup'],
    requires=["argparse"],
    scripts=['bin/zalgo'])
