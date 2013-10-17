__author__ = 'elip'

import setuptools
setuptools.setup(
    zip_safe=True,
    name='cosmo-plugin-openstack-provisioner',
    version='0.1.0',
    author='elip',
    author_email='itaif@gigaspaces.com',
    packages=['openstack_host_provisioner'],
    license='LICENSE',
    description='Plugin for provisioning openstack nova hosts',
    install_requires=[
        "kombu==3.0"
    ]
)

