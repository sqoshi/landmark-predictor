from setuptools import find_packages, setup

setup(
    name="Landmark Predictor",
    version="1.0.0",
    description="Python wrapper for dlib's landmark prediction model.",
    url="https://github.com/sqoshi/landmark-predictor",
    author="Piotr Popis",
    author_email="piotrpopis@icloud.com",
    license="MIT",
    py_modules=["run"],
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "wheel>=0.36.2",
        "termcolor>=1.1.0",
        "numpy>=1.21.1",
        "dlib>=19.22.0",
        "progressbar>=2.5",
        "opencv-python>=4.5.3.5",
    ],
)
