import glob, os
from setuptools.command.build_py import build_py
from setuptools import setup, find_packages

package_name = 'hym'

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as req:
    requirements = req.read().splitlines()

class InstallHook(build_py):
    def run(self):
        os.system(f'coconut --force ./{package_name}')
        build_py.run(self)

setup( name                          = package_name
     , version                       = '0.0.2'
     , author                        = 'Yannick Uhlmann'
     , author_email                  = 'augustunderground@pm.me'
     , description                   = 'HTTP Adapter for gym, mostly GACE/ACE'
     , long_description              = long_description
     , long_description_content_type = 'text/markdown'
     , url                           = 'https://github.com/augustunderground/hym'
     , packages                      = find_packages()
     , classifiers                   = [ 'Development Status :: 2 :: Pre-Alpha'
                                       , 'Programming Language :: Python :: 3'
                                       , 'Operating System :: POSIX :: Linux' ]
     , python_requires               = '>=3.9'
     , install_requires              = requirements
     , entry_points                  = { 'console_scripts': [ f'ace-http = {package_name}.__main__:ace'
                                                            , f'gym-http = {package_name}.__main__:gym'
                                                            , f'gace-http = {package_name}.__main__:gace' ]}
     , package_data                  = { '': ['*.hy', '*.coco', '__pycache__/*']}
     , cmdclass                      = { 'build_py': InstallHook }
     , )
