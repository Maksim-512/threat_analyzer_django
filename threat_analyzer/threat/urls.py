from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("main", views.MainView.as_view(), name='main'),
    path("all_devices_variations", views.AllDevicesVariationsView.as_view(), name='all_devices_variations'),
    path("info_devices", views.InfAboutDevicesView.as_view(), name='info_devices'),
    path("info_ubi/<str:sp_numb>", views.DescriptionUbiView.as_view(), name='info_ubi'),
    path("info_protection/<str:sp_numb>", views.DescriptionProtectionMeasuresView.as_view(), name='info_protect'),
    # path("info_devices/<str:devices>", views.InfAboutDevicesView.as_view(), name='info_devices'),
]