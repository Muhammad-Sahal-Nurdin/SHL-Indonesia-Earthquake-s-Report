import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IndonesiaEarthquake'sReport",
    version="0.0.1",
    author="Muhammad Sahal Nurdin",
    author_email="sahalnurdin@gmail.com",
    description="This is a live earthquake report from Indonesian Agency for Meteorology, Climatology, and "
                "Geophysics' s data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Muhammad-Sahal-Nurdin/SHL-Indonesia-Earthquake-s-Report",
    project_urls={
        "Website": "https://sahaln.github.io/CV/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
    # package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
