from django.conf.urls import url
import code_analyze.views

urlpatterns = [
    url('analyze',
        code_analyze.views.CodeAnalyzeApi.as_view(),
        name="code_analyze")
]
