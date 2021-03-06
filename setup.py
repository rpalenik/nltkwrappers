from setuptools import setup, find_packages

setup(
    name='nltkwrappers',
    version='1.0',

    description='Wrappers for nltk',

    author='Richard Palenik',
    author_email='rpalenik2@gmail.com',

    # url='http://git.openstack.org/cgit/openstack/stevedore',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=['nltkwrappers',
              ],

    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'nltkwrappers.nltk': [
            'tokenizer = basicnltk.nltkwrappers:Tokenizer',
            'normalizer = basicnltk.nltkwrappers:Normalizer',
            'senttokenizer = basicnltk.nltkwrappers:SentTokenizer',
        ],
    },

    zip_safe=False,
)
