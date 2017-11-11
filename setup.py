from setuptools import setup, find_packages

setup(
    name="mariocli",
    description='Another package management tool; works well with endpointer.',
    license="MIT",
    version='0.0.1',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Communications',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=['documentation', 'hugo', 'static-content'],
    install_requires=[
        'pyyaml',
        'jsonschema',
        'click',
    ],
    extras_require={
        'dev': [
            'pylint',
        ]
    },
    python_requires='~=3.6',
    entry_points = {
        'console_scripts': ['mario=mario.cli:cli'],
    },
    test_suite="tests",
)
