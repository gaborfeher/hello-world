import setuptools

setuptools.setup(
    name="hallo-world-gfeher",
    version="0.0.7",
    author="Gabor Feher",
    author_email="feherga@gmail.com",
    description="A small example package",
    long_description='Long description',
    long_description_content_type="text/plain",
    url="https://github.com/gaborfeher/hello-world",
    py_modules=['hello'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

