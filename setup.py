from setuptools import setup

setup(
    name = 'terminal-minesweeper',
    description = 'A pure Python implementation of minesweeper using curses.',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    version = '0.1.0',
    author = 'Jerie Wang',
    author_email = 'mail@jerie.wang',
    url = 'https://github.com/jeriewang/terminal-minesweeper',
    python_requires = '>=3.8',
    packages = ['minesweeper'],
    entry_points = {
        'console_scripts': [
            'minesweeper = minesweeper.main:run'
        ]
    },
    install_requires = [
        "windows-curses ; platform_system == 'Windows'"
    ],
    license='GPLv3',
    classifiers=[
        'Environment :: Console :: Curses',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3',
        'Topic :: Games/Entertainment'
    ]
        
)
