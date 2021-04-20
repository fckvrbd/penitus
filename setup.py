import pathlib
from setuptools import setup

_path = pathlib.Path(__file__).parent

README = (_path / "README.md").read_text()


def _setup():
    setup(
        name="penitus",
        version="1.0.0",
        description="Shows information about cryptocurrencies, like prices.",
        long_description=README,
        long_description_content_type="text/markdown",
        license="MIT",
        author="Gino Zanella",
        author_email="iosgino@hotmail.com",
        readme="README.md",
        repository="https://github.com/fckvrbd/penitus",
        python="^3.0",
        install_requires=["requests"],
        packages=["src/penitus"],
        keywords=[
            "Cryptocurrency",
            "Finances",
            "Bitcoin",
            "Coinpaprika",
            "Investing"
        ],
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Development Status :: 4 - Beta",
            "Natural Language :: English",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Topic :: Software Development",
            "Topic :: Office/Business :: Financial :: Investment",
        ],
    )


if __name__ == "__main__":
    _setup()
