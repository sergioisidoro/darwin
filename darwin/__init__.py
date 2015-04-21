# -*- encoding: utf-8 -*-

from __future__ import absolute_import
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.


from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
