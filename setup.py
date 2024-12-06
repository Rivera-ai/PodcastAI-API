import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="podcastai",
    version="0.1.0",
    author="Rivera.ai/Fredy",
    author_email="riveraaai200678@gmail.com",
    description="Client API PodcastAI Studio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rivera-ai/PodcastAI-API",
    package_dir={"": "src"},  # Indica que los paquetes están en src/
    packages=setuptools.find_packages(where="src"),  # Busca paquetes en src/
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "requests>=2.25.0",
    ],
)