from django.urls import path
from django.views.defaults import page_not_found
from . import views

def custom_404_template(request):
    return page_not_found(request, None)


urlpatterns = [
    path('', views.PhotoListView.as_view(), name='homepage'),
    path('search', views.SearchView.as_view(), name='search'),
    path('photos/<slug:slug>', views.PhotoDetailView.as_view(), name='photoDetail'),
    path('<slug:collection_slug>', views.CollectionView.as_view(), name='collection'),
    path('404', custom_404_template,),
]