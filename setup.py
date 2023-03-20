import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="guichu_ai",
    version="0.1.0",
    author="Yanbo Zhang",
    author_email="Zhang.Yanbo@asu.edu",
    description="GuichuAI, powered by OpenAI GPT-3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zhangyanbo/guichu_ai",
    project_urls={
        "Bug Tracker": "https://github.com/Zhangyanbo/guichu_ai/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['guichu_ai'],
    python_requires=">=3.6",
)