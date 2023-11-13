from setuptools import setup, find_packages

setup(
    name='math_quiz_tk_dsss23_24',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz:main',
        ],
    },
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)