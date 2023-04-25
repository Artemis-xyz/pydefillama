import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

with open("requirements.txt", "r") as requirements_file:
    requirements_text = requirements_file.read()

requirements = requirements_text.split()

setuptools.setup(
    name="pydefillama",
    version="1.0.3",
    description="Python Wrapper for DefiLlama endpoints",
    url="https://github.com/Artemis-xyz/DefiLlama-Python-Client",
    author="Artemis.xyz",
    author_email="team@artemis.xyz",
    license="MIT",
    packages=setuptools.find_packages(exclude="tests"),
    zip_safe=False,
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=requirements,
)
