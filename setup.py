import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent.resolve()

PACKAGE_NAME = "MinePlayer"
AUTHOR = "SamHacker"
AUTHOR_EMAIL = "xux510208@gmail.com"
URL = "https://github.com/510208/minePlayer"
DOWNLOAD_URL = "https://pypi.org/project/mineplayer/"

LICENSE = "GNU General Public License v3.0"
VERSION = "1.0.3"
DESCRIPTION = "A module to parse Minecraft player information"
LONG_DESCRIPTION = (HERE / "docs" / "README.md").read_text(encoding="utf8")
LONG_DESC_TYPE = "text/markdown"

requirements = (HERE / "requirements.txt").read_text(encoding="utf8")
INSTALL_REQUIRES = [s.strip() for s in requirements.split("\n")]

dev_requirements = (HERE / "dev_requirements.txt").read_text(encoding="utf8")
EXTRAS_REQUIRE = {"dev": [s.strip() for s in dev_requirements.split("\n")]}

CLASSIFIERS = [f"Programming Language :: Python :: 3.{str(v)}" for v in range(7, 12)]
PYTHON_REQUIRES = ">=3.7"

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    packages=find_packages(),
    classifiers=CLASSIFIERS,
    project_urls={
        "Source": "https://github.com/510208/minePlayer",
    },
)