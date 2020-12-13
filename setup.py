from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='BA Flight System',
    packages=find_packages(include=['flightsystem']),
    version='1.0.0',
    description='none',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mossyegghead01/BA-Flight-System",
    author='mossy the mad guy, DistinctNoot',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='test_module',
)
