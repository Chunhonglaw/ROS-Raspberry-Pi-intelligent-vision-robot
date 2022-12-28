from setuptools import setup

package_name = 'vision_rpi_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='chunhonglaw',
    maintainer_email='chunhonglaw@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'chun_publihser_node = vision_rpi_bot.publisher:main',
                'chun_subscriber_node = vision_rpi_bot.subscriber:main',
                # = package name.file name
                
        ],
    },

)
