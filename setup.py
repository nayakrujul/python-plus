from setuptools import setup, find_packages

long_description = 'Update a graph while you plot - read the docs at https://www.github.com/nayakrujul/plot-on-the-go'

setup(
  name = 'plot-on-the-go',
  version = '2.0',
  license='Apache',
  description = 'Update a graph while you plot!',
  author = 'Rujul Nayak',
  author_email = 'rujulnayak@outlook.com',
  url = 'https://github.com/nayakrujul/plot-on-the-go',
  download_url = 'https://github.com/nayakrujul/plot-on-the-go/archive/refs/tags/v_01.tar.gz',
  keywords = ['plot', 'graph'],
  install_requires=[
    'pygame'
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
  packages = find_packages()
)
