# setup.py
import os
from setuptools import setup, find_packages

VERSION = os.getenv('PACKAGE_VERSION', '0.1.0')

setup(
    name="testatolibrary",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  # Agrega aquí las dependencias de tu biblioteca si las hay
    description="Una biblioteca de prueba para AWS CodeArtifact",
    author="Tu Nombre",
    author_email="tuemail@example.com",
    url="https://github.com/tuusuario/testatolibrary",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",  # Asegúrate de agregar Python 3.10 aquí
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',  # Especificar que necesita al menos Python 3.10
)
