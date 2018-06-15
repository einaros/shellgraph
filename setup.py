import setuptools

with open('README.md', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
  name='shellgraph',
  version='0.1.0',
  author='Einar Otto Stangvik',
  author_email='einaros@gmail.com',
  description='A simple tool to graph key distribution from stdin',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/einaros/shellgraph',
  packages=setuptools.find_packages(),
  classifiers=(
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ),
  scripts=['bin/shellgraph'],
  install_requires=[
    'blessings'
  ]
)
