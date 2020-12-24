"""
djangoflutterwave default settings are defined here and determined in combination
with what has been defined in django.conf.settings.
"""

# stdlib import

# django imports
from django.conf import settings

# 3rd party imports

# project imports

FLW_SANDBOX = getattr(settings, "FLW_SANDBOX", True)

if FLW_SANDBOX:
    FLW_PUBLIC_KEY = getattr(settings, "FLW_SANDBOX_PUBLIC_KEY", "FLWPUBK_TEST-35a71b88c1e953215554f69b7f8e90fc-X")
    FLW_SECRET_KEY = getattr(settings, "FLW_SANDBOX_SECRET_KEY", "FLWSECK_TEST-8773b4c230a919b4450740d56db32adc-X")
else:
    FLW_PUBLIC_KEY = getattr(settings, "FLW_PRODUCTION_PUBLIC_KEY", "FLWPUBK-117de317b5786e42b8d785aea75efa04-X")
    FLW_SECRET_KEY = getattr(settings, "FLW_PRODUCTION_SECRET_KEY", "FLWSECK-3157de239cf84f7b0d57d8f48ec02adf-X")
