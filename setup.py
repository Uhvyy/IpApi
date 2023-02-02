import setuptools

readme_file = open("README.md", "r")
readme_data = readme_file.read()
readme_file.close()

setuptools.setup(
    name='IpApi',
    packages=['IpApi'],
    version='1.0.0',
    license='MIT',
    description="IpApi is a simple module for obtaining information about an IP address by using IP-API.",
    long_description=readme_data,
    long_description_content_type='text/markdown',
    author="kuroki",
    url='https://github.com/Uhvyy/IpApi',
    keywords=["IpApi"],
    install_requires=[
        "aiohttp",
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)
