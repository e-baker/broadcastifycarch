from setuptools import setup, find_packages

setup(
    name='broadcastifycarchives',
    version='0.1.0',
    description='Download and parse Broadcastify.com call archives.',
    author='Eric Baker',
    author_email='e-baker@users.noreply.github.com',
    packages=find_packages(),
    namespace_packages=['broadcastifycarchives'],
    install_requires=[
        i.strip() for i in open("requirements.txt").readlines()
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.12',
)