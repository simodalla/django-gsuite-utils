=============================
Django Gsuite Utils
=============================

.. image:: https://badge.fury.io/py/django-gsuite-utils.svg
    :target: https://badge.fury.io/py/django-gsuite-utils

.. image:: https://travis-ci.org/simodalla/django-gsuite-utils.svg?branch=master
    :target: https://travis-ci.org/simodalla/django-gsuite-utils

.. image:: https://codecov.io/gh/simodalla/django-gsuite-utils/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/simodalla/django-gsuite-utils

Your project description goes here

Documentation
-------------

The full documentation is at https://django-gsuite-utils.readthedocs.io.

Quickstart
----------

Install Django Gsuite Utils::

    pip install django-gsuite-utils

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'gsuite_utils.apps.GsuiteUtilsConfig',
        ...
    )

Add Django Gsuite Utils's URL patterns:

.. code-block:: python

    from gsuite_utils import urls as gsuite_utils_urls


    urlpatterns = [
        ...
        url(r'^', include(gsuite_utils_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
