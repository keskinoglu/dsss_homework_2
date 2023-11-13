from setuptools import setup

setup(
    name='math_quiz',
    version='0.5',
    py_modules=['math_quiz'],
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