from setuptools import setup, find_packages

setup(
    name='app',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'torch',
        'transformers'
    ],
    entry_points={
        'console_scripts': [
            'streamlit_app = streamlit_app:main'
        ]
    }
)
