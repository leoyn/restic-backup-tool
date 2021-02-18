from setuptools import setup, find_packages

setup(
    name="backup",
    version="1.0",
    packages=[
        "backup",
        "backup.connector",
        "backup.component.behaviour",
        "backup.component.structure",
    ],
    include_package_data=True,
    install_requires=[
        "click",
    ],
    package_data={"backup": ["*.plist"]},
    entry_points="""
        [console_scripts]
        backup=backup.connector.CommandLineConnector:main
    """,
)