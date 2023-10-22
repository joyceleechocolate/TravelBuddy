# Generated by Django 4.2.6 on 2023-10-18 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_date_begin', models.DateField()),
                ('travel_date_end', models.DateField()),
                ('travel_location', models.CharField(max_length=255)),
                ('travel_duration', models.CharField(max_length=255)),
                ('detail_itinerary', models.TextField()),
                ('trip_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip_app.trips')),
            ],
        ),
    ]