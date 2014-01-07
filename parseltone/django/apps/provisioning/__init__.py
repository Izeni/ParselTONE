from django.conf.urls import *
from parseltone.django.apps.provisioning import polycom

urls = (patterns('',
    (r'^polycom/', include(polycom.urls)),
), 'provisioning', 'provisioning')
