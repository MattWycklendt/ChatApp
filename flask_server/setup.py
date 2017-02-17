from setuptools import setup

setup(
    name='Flask Chat App',
    version='1.0',
    long_description=__doc__,
    packages=['flask_server'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['flask', 'flask-socketio', 'gevent']
)
