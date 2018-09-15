from setuptools import setup, find_packages


setup(
    name='fizzbuzzn',
    version='0.0.1',
    description='like fizzbuzz program',
    author='kuronbo',
    author_email='kurinbo.i2o@gmail.com',
    license='MIT',
    packages=find_packages(exclude=('tests', 'venv')),
)
