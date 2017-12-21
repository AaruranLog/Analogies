from setuptools import setup, find_packages

setup(
    name='analogies',
    version='0.1.2.dev',
    description="Analogy solver, with Flask front-end",
    author="Aaruran Elamurugaiyan",
    url="https://github.com/AaruranE/Analogies",
    packages=find_packages(".", exclude=["tests"]),
    include_package_data=True,
    license="MIT"
)
