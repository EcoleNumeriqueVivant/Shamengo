import dj_database_url

from shamengo.settings import *

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

SECRET_KEY = 'epwe3qx5k6xt3#w0w@5oa=&9ldsa(z65$-ncc(i%o(sne*^fju'

ALLOWED_HOSTS = ['zeshamengo.herokuapp.com']
