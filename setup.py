from setuptools import setup

setup(
    name='BloxsPyHook',
    version='0.1.0',    
    description='A simple webhook script intended for macros',
    url='https://github.com/EvilPiza/Bloxs-Webhook-Package',
    author='Christian Fillmore',
    author_email='ilikefreeminecraft@gmail.com',
    license='MIT License',
    packages=['Pillow', 'Discord', 'tkinter', 'asyncio', 'pyscreeze', 'aiohttp', 'datetime'],
    install_requires=['Pillow',
                      'Discord',
                      'tkinter',   
                      'asyncio',
                      'pyscreeze',
                      'aiohttp',
                      'datetime'                 
                      ],

    classifiers=[
        'Development Status :: 1 - Testing',
        'Intended Audience :: Roblox Macros',  
        'Operating System :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
