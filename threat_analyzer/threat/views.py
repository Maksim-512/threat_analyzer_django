from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView

from .forms import TextInputForm
from django.http import HttpResponseRedirect
from .nlp import device_detection
from .models import Devices, DevicesVariations, SPWithDescription


def error_404_view(request, exception):
    return render(request, 'threat/404.html', status=404)


class MainView(View):

    def get(self, request):
        form = TextInputForm(request.POST)
        return render(request,
                      'threat/main.html',
                      {'form': form})

    def post(self, request):
        form = TextInputForm(request.POST)
        if form.is_valid():
            input_str = form.cleaned_data['input_str']
            all_devices = DevicesVariations.objects.values_list('device_variation', flat=True)
            # print(all_devices)
            devices = device_detection(input_str, all_devices)
            # print(devices)
            request.session['devices'] = devices
            request.session['input_str'] = input_str
            return redirect('info_devices')
            # return redirect('info_devices', {'devices': devices})

        return render(request,
                      'threat/main.html',
                      {'form': form})


class InfAboutDevicesView(View):

    def get(self, request):
        all_devices = DevicesVariations.objects.all()
        devices = request.session.get('devices', '')
        for device in devices:
            device_var = DevicesVariations.objects.get(device_variation=device)
            print(
                f'Устройство {device_var.device_variation} относится к типу устройств {device_var.device_name.device_name}, которое входит в класс {device_var.device_name.device_type}')
            print(
                f'Этому устройству соответствуют следующие способы реализации угроз: {device_var.device_name.sp_devices.all()}')
        input_str = request.session.get('input_str', '')
        return render(request,
                      'threat/info_about_devices.html',
                      {'all_devices': all_devices,
                       'devices': devices,
                       'input_str': input_str})


class DescriptionUbiView(View):

    def get(self, request, sp_numb):
        sp = get_object_or_404(SPWithDescription, sp_number=sp_numb)

        return render(request,
                      'threat/info_ubi.html',
                      {'sp': sp})


class DescriptionProtectionMeasuresView(View):

    def get(self, request, sp_numb):
        protection = get_object_or_404(SPWithDescription, sp_number=sp_numb)

        return render(request,
                      'threat/description_protection_measures.html',
                      {'protection': protection})


class AllDevicesVariationsView(ListView):
    template_name = 'threat/all_devices_variations.html'
    model = DevicesVariations
    context_object_name = 'all_devices_variations'
