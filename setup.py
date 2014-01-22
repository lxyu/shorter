from setuptools import setup, find_packages

version = "0.1"


setup(name="shorter",
      version=version,
      description="Simple web app to create a short url service.",
      long_description=open("README.rst").read(),
      classifiers=[],
      keywords="url short shorter flask",
      author="Lx Yu",
      author_email="i@lxyu.net",
      url="",
      license="MIT",
      packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
      include_package_data=True,
      zip_safe=False,
      entry_points={"console_scripts": ["shorter = shorter:main"]},
      install_requires=[
          "Flask-SQLAlchemy>=1.0",
          "Flask>=0.10.1",
          "SQLAlchemy>=0.9.1"
      ])
