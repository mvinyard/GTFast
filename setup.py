from setuptools import setup
import re
import os
import sys


setup(
    name="GTFast",
    version="0.0.2",
    python_requires=">3.6.0",
    author="Michael E. Vinyard - Harvard University - Massachussetts General Hospital - Broad Institute of MIT and Harvard",
    author_email="mvinyard@broadinstitute.org",
    url="https://github.com/mvinyard/GTFast",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    description="GTFast - cache and subset a `.gtf` file as a `.csv` for faster subsequent use.",
    packages=[
        "gtfast",
    ],
    
    install_requires=[
	"gtfparse>=1.2.1",
	"pandas>=1.3.5",
	"pydk>=0.0.4",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    license="MIT",
)
