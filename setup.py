from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="disnake-pagination",
    version="0.0.1",
    description="Easily create pagination for your embeds.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=["Paginator"],
    package_dir={'': "src"},
    url="https://github.com/SlumberDemon/disnake-Pagination",
    author="SlumberDemon",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ]
)
