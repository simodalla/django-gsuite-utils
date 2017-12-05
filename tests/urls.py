# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from gsuite_utils.urls import urlpatterns as gsuite_utils_urls

urlpatterns = [
    url(r'^', include(gsuite_utils_urls, namespace='gsuite_utils')),
]
