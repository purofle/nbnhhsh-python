import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nbnhhsh",
    version="1.0",
    author="purofle",
    author_email="3272912942@qq.com",
    description="nbnhhsh的python版本",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/purofle/nbnhhsh-python",
    entry_points={
        'console_scripts': [
            'nbnhhsh=nbnhhsh.cmd:main',

        ],

    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4'
)
