from setuptools import setup, find_packages

setup(
    name='saas_co',
    version='0.12',
    license='MIT',
    author="David Schwartz",
    author_email='david.schwartz@devfactory.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/dschwartz/saas-co-cur',
    keywords='cost optimization cur',
    install_requires=[
          'boto3',
          'botocore',
          'pandas',
          'awswrangler'
      ],
)
