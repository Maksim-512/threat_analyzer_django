from django.db import models


class Devices(models.Model):
    device_name = models.CharField(max_length=100, unique=True)
    device_type = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.device_name} - {self.device_type}'


class DevicesVariations(models.Model):
    device_name = models.ForeignKey(Devices, on_delete=models.CASCADE, to_field='device_name', related_name='variations')
    device_variation = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.device_name.device_name} - {self.device_variation}"


class SPWithDescription(models.Model):
    sp_number = models.CharField(max_length=100, unique=True)
    sp_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.sp_number


class SPDevices(models.Model):
    device_name = models.ForeignKey(Devices, on_delete=models.CASCADE, to_field='device_name', related_name='sp_devices')
    sp_number = models.ForeignKey(SPWithDescription, on_delete=models.CASCADE, to_field='sp_number', related_name='sp_devices')

    def __str__(self):
        return f"{self.device_name.device_name} - {self.sp_number.sp_number}"


class SPProtection(models.Model):
    sp_number = models.ForeignKey(SPWithDescription, on_delete=models.CASCADE, to_field='sp_number', related_name='protections')
    protection_method = models.CharField(max_length=1000)
    protection_realize = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.sp_number.sp_number}'


class ThreatWithDescription(models.Model):
    possible_threats = models.CharField(max_length=1000, unique=True)
    threat_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.threat_description


class SPUBI(models.Model):
    sp_number = models.ForeignKey(SPWithDescription, on_delete=models.CASCADE, to_field='sp_number', related_name='ubis')
    possible_threats = models.ForeignKey(ThreatWithDescription, on_delete=models.CASCADE, to_field='possible_threats', related_name='threat_descriptions')

    def __str__(self):
        return self.sp_number.sp_number

