"""setup http-server."""

from setuptools import setup

setup(
    name="http-server",
    description="An Implementation of the http-server function",
    version=0.1,
    author="Regenal Grant",
    author_email="regenal@mac.com",
    license="MIT",
    package_dir={'': './'},
    py_modules=['client, server'],
    install_requires=['numpy', 'faker', 'inquirer'],
    extras_require={
        "test": ["pytest", "pytest-watch", "pytest-cov", "tox"],
    },
    entry_points={
        "console_script": [
            "main = main:main",
        ],
    },
)