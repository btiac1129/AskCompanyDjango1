from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView, RedirectView


class RootView(TemplateView):
    template_name = 'root.html'


urlpatterns = [
    # path('', TemplateView.as_view(template_name='root.html'), name='root',)
    # path('', RootView.as_view(), name='root'),
    path('', RedirectView.as_view(
        # url='/instagram/'
        pattern_name='instagram:post_list',  # django 선호
    ), name='root'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('instagram/', include('instagram.urls')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
# settings.MEDIA_URL
# settings.MEDIA_ROOT
