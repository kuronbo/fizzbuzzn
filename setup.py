from setuptools import setup, find_packages


setup(
    name='fizzbuzzn',
    version='0.0.2',
    description='like fizzbuzz program',
    author='kuronbo',
    author_email='kurinbo.i2o@gmail.com',
    license='MIT',
    packages=find_packages(exclude=('tests')),
    tests_require=['pytest'],
    test_suite='pytest'
)
