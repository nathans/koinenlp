Installation
============

Preparation
-----------

It is recommended to install in a Python `virtualenv
<https://virtualenv.readthedocs.org/en/latest/>`_:

.. code-block:: bash

   mkdir nlp
   cd nlp
   virtualenv -p python3 .
   source bin/activate

It is possible to install koine-nlp in your system environment if you
have sufficient access. That would require running as root or using
sudo in the portions below.

Option 1: Install via pip
-------------------------

The koine-nlp package is availale in `PyPi
<https://pypi.python.org/pypi>`_. It can be installed via pip:

.. code-block:: bash

   pip install koine-nlp

Option 2: Install from archive
------------------------------

Obtain the koine-nlp source archive by cloning its git repository:

.. code-block:: bash

   git clone https://github.com/nathans/koinenlp.git
   cd koine-nlp
   python setup.py install
