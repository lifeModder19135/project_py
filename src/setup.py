from setuptools import setup

setup(
    name = 'project',
    version = 0.1,
    packages = ['project', 'libpcli'],
    package_dir = {
        'project': 'project_cli',
        'libpcli': 'project_cli/lib'
    }
#    entry_points = '''
#        [console_scripts]
#        project=project:main:entrypoint
#    '''
)