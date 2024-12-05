from rest_framework import routers

from core_root_api.job_api.viewset.application_form import ApplicationFormViewset

router=routers.SimpleRouter()
router.register(r'apply',ApplicationFormViewset,basename='apply')


urlpatterns=[
    *router.urls
]

