=====
Usage
=====

To use Django Gsuite Utils in a project, add it to your `INSTALLED_APPS`:

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
