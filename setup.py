#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'ovos-intent-plugin-regex=ovos_intent_plugin_regex:RegexPipelinePlugin'
setup(
    name='ovos-intent-plugin-regex',
    version='0.0.1',
    description='A intent plugin for mycroft',
    url='https://github.com/OpenVoiceOS/ovos-intent-plugin-regex',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['ovos_intent_plugin_regex'],
    install_requires=["ovos-plugin-manager"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={'ovos.pipeline': PLUGIN_ENTRY_POINT}
)
