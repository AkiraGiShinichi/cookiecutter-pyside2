from setuptools import setup

requirements = [
    # TODO: put your package requirements here
    'pyqt5',
    'wheel',
    'sphinx'
]

setup(
    name='{{ cookiecutter.repo_name }}',
    version='{{ cookiecutter.version }}',
    description="{{ cookiecutter.project_short_description }}",
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=['{{ cookiecutter.package_name }}', '{{ cookiecutter.package_name }}.images',
              '{{ cookiecutter.package_name }}.tests'],
    package_data={'{{ cookiecutter.package_name }}.images': ['*.png']},
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.application_title }}={{ cookiecutter.package_name }}.{{ cookiecutter.application_name }}:main'
        ]
    },
    install_requires=requirements,
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest', 
        'pytest-cov',
        'pytest-faulthandler',
        'pytest-mock',
        'pytest-qt',
        'pytest-xvfb'
    ],
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8 NOT compatible',
    ],
)
