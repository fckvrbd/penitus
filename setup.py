from setuptools import setup

if __name__ == "__main__":
    setup(
        name="penitus",
        version="1.0.0",
        description="Shows information about cryptocurrencies, like prices.",
        license="MIT",
        author="Gino Zanella",
        author_email="iosgino@hotmail.com",
        readme="README.md",
        repository="https://github.com/fckvrbd/penitus",
        python="^3.0",
        keywords=[
            "Cryptocurrency",
            "Finances",
            "Bitcoin",
            "Coinpaprika",
            "Investing"
        ],
        packages=["src/penitus"],
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
        install_requires=["requests"]
    )
