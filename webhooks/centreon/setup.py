from setuptools import setup, find_packages

version = '1.0.0'

setup(
    name="alerta-centreon",
    version=version,
    description='Centreon Webhook for Alerta',
    author='Skander REDJEL',
    author_email='skander.redjel@gmail.com',
    packages=find_packages(),
    py_modules=['alerta_centreon'],
    install_requires=[],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.webhooks': [
            'centreon = alerta_centreon:CentreonWebhook'
        ]
    }
)