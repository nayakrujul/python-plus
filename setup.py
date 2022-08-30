from setuptools import setup, find_packages

long_description = 'Shorten your Python code with shorter syntax - read the docs at https://www.github.com/nayakrujul/python-plus'

setup(
  name = 'shorter-python',
  version = '5.0',
  license='Apache',
  description = 'Shorten your Python code with shorter syntax.',
  author = 'Rujul Nayak',
  author_email = 'rujulnayak@outlook.com',
  url = 'https://github.com/nayakrujul/python-plus',
  download_url = 'https://github.com/nayakrujul/python-pluso/archive/refs/tags/v_01.tar.gz',
  keywords = ['shorter', 'syntax'],
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  long_description=long_description,
  long_description_content_type='text/x-rst',
  packages = find_packages(),
  entry_points = {
    'console_scripts': [
      'pythonplus = python_plus.compiler:from_file'
    ]
  }
)
