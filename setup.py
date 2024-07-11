#!/usr/bin/env python

from distutils.core import setup

setup(
    name="abaqusrdo",
    version="1.0",
    description="",
    author="Kai Steltner",
    license="MIT License",
    packages=["abaqusrdo"],
    install_requires=["numpy>=2.0.0"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
)
