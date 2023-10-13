from setuptools import setup

setup(
    name="jiggler",
    version="0.0.1",
    py_modules=["jiggler"],
    entry_points={"console_scripts": ["jiggler = jiggler:main"]},
)
