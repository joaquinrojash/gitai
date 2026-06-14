from setuptools import setup, find_packages

setup(
    name="gitai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "anthropic>=0.25.0",
        "click>=8.0.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "gitai=gitai.main:main",
        ],
    },
    author="Your Name",
    author_email="your@email.com",
    description="AI-powered git commit and PR description generator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/gitai",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Version Control :: Git",
    ],
    python_requires=">=3.10",
)