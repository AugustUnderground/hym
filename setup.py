import glob, os
from setuptools.command.build_py import build_py
from setuptools import setup, find_packages

package_name = 'oaceis'

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as req:
    requirements = req.read().splitlines()

class InstallHook(build_py):
    def run(self):
        os.system(f'coconut --force ./{package_name}')
        build_py.run(self)

setup( name                          = package_name
     , version                       = '0.0.1'
     , author                        = 'Yannick Uhlmann'
     , author_email                  = 'augustunderground@pm.me'
     , description                   = 'HTTP Adapter for GACE/ACE'
     , long_description              = long_description
     , long_description_content_type = 'text/markdown'
     , url                           = 'https://github.com/augustunderground/oaceis'
     , packages                      = find_packages()
     , classifiers                   = [ 'Development Status :: 2 :: Pre-Alpha'
                                       , 'Programming Language :: Python :: 3'
                                       , 'Operating System :: POSIX :: Linux' ]
     , python_requires               = '>=3.8'
     , install_requires              = requirements
     , entry_points                  = { 'console_scripts': [ f'ace-http = {package_name}.__main__:ace'
                                                            , f'gace-http = {package_name}.__main__:gace' ]}
     , package_data                  = { '': ['*.hy', '*.coco', '__pycache__/*']}
     , cmdclass                      = { 'build_py': InstallHook }
     , )
