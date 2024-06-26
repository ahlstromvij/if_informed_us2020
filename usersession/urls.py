from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, ResultsView, IntroPageView, MoreInfoView

urlpatterns = [
	# path('', HomePageView.as_view(), name='home'),
	path('', views.questions, name='home'),
	path('intro/', IntroPageView.as_view(), name='intro'),
    # path('questions/', views.questions, name='questions'),
	path('results/', ResultsView.as_view(), name='results'),
	path('more_info/', MoreInfoView.as_view(), name='more_info'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
