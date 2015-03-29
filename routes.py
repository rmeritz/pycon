# urls.py
from django.conf.urls import include, patterns


urlpatterns = patterns(
    '',
    (r'^jobs/', include("skill_and_love.job.urls")),
)


# job/urls.py
from django.conf.urls import url, patterns

from .views import CreateJobView


urlpatterns = patterns(
    '',
    url(r'^create/$', CreateJobView.as_view(), name='job_create'),
)
