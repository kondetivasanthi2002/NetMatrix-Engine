from setuptools import setup, find_packages

setup(
    name="netmatrix-suite",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pydantic>=2.0.0",
        "fastapi>=0.100.0",
        "uvicorn>=0.20.0",
        "pytest>=7.0.0"
    ]
)
