from setuptools import setup, find_packages
setup(
    name="garbage",
    version="1.0",
    packages=find_packages(),
    install_requires=[
    "pandas", # Add other dependencies as needed
    ],
    author="NguyenVan Huan",
    author_email="nvhuan2907@gmail.com",
    description= "Garbage dataloader",
    long_description="Garbage dataset is taken from Internet",
    long_description_content_type="text/markdown",
    url="https://github.com/huanUITk16/GARBAGE.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)