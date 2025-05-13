from setuptools import setup, find_packages

setup(
    name='MISA_pySLIME',
    version='2.0.6',
    description="""Millstone Hill Incoherent Scatter Radar Spatial-Linear Ionospheric Modeling Engine""",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mateo Cardona Serrano (them)',
    author_email='mcardonaserrano@berkeley.edu',
    url='https://github.com/mcardonaserrano/MISA_pySLIME',
    packages=find_packages(),
    include_package_data=True,
    package_data={'MISA_pySLIME': ['data/*.txt']},
    install_requires=[
        'numpy',
        'requests',
        'scikit-learn',
        'pandas',
        'xarray',
        'tqdm',
        'scipy',
        'requests'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
