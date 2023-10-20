import setuptools
from pathlib import Path


root_dir = Path(__file__).absolute().parent
with (root_dir / "VERSION").open() as f:
    version = f.read()
with (root_dir / "README.md").open() as f:
    long_description = f.read()
with (root_dir / "requirements.in").open() as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="{{cookiecutter.module_name}}",
    version=version,
    description="{{cookiecutter.module_description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    maintainer="{{cookiecutter.maintainer}}",
    maintainer_email="{{cookiecutter.maintainer_email}}",
    url="{{cookiecutter.url_repository}}",
    packages=setuptools.find_packages("backend"),
    package_dir={"": "backend"},
    package_data={"{{cookiecutter.module_package_name}}.migrations": ["data/*.sql"]},
    install_requires=requirements,
    zip_safe=False,
    entry_points={
        "gn_module": [
            "code = {{cookiecutter.module_package_name}}:MODULE_CODE",
            "picto = {{cookiecutter.module_package_name}}:MODULE_PICTO",
            "blueprint = {{cookiecutter.module_package_name}}.blueprint:blueprint",
            "config_schema = {{cookiecutter.module_package_name}}.conf_schema_toml:GnModuleSchemaConf",
            "migrations = {{cookiecutter.module_package_name}}:migrations",
        ],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
)
