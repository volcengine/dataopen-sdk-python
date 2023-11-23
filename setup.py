from setuptools import setup
import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dataopen-sdk-python",
    version="0.0.5",
    description="火山Dataopen python 语言sdk",
    author="caichengnan@bytedance.com",
    license="Apache-2.0",
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements
)