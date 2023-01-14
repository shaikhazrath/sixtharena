from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))
]

handler404 = 'app.views.err_404'
handler500 = 'app.views.err_500'
