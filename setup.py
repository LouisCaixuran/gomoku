from setuptools import setup, find_packages

setup(name='gomoku',
      version='0.1',
      url='https://github.com/LouisCaixuran/gomoku',
      license='Apache',
      author='Louis Caixuran',
      author_email='louiscaixuran@163.com',
      description='Use Monte Carlo/AI/... method to play gomoku',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False,
      
      entry_points={
          'console_scripts':[
  	      'play-go = gomoku.run:run',
	    ]
      }
)
