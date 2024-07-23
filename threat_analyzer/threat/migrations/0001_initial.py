# Generated by Django 5.0 on 2024-07-02 13:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Devices",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("device_name", models.CharField(max_length=100, unique=True)),
                ("device_type", models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="SPWithDescription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sp_number", models.CharField(max_length=100, unique=True)),
                ("sp_description", models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="ThreatWithDescription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("possible_threats", models.CharField(max_length=1000, unique=True)),
                ("threat_description", models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="DevicesVariations",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("device_variation", models.CharField(max_length=1000)),
                (
                    "device_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="variations",
                        to="threat.devices",
                        to_field="device_name",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SPProtection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("protection_method", models.CharField(max_length=1000)),
                ("protection_realize", models.CharField(max_length=1000)),
                (
                    "sp_number",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="protections",
                        to="threat.spwithdescription",
                        to_field="sp_number",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SPDevices",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "device_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sp_devices",
                        to="threat.devices",
                        to_field="device_name",
                    ),
                ),
                (
                    "sp_number",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sp_devices",
                        to="threat.spwithdescription",
                        to_field="sp_number",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SPUBI",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sp_number",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ubis",
                        to="threat.spwithdescription",
                        to_field="sp_number",
                    ),
                ),
                (
                    "possible_threats",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="threat_descriptions",
                        to="threat.threatwithdescription",
                        to_field="possible_threats",
                    ),
                ),
            ],
        ),
    ]