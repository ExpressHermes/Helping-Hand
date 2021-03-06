# Generated by Django 3.1.4 on 2020-12-13 11:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_organizer', models.CharField(max_length=100)),
                ('event_name', models.CharField(max_length=100)),
                ('event_date', models.DateField()),
                ('place_name', models.CharField(max_length=350)),
                ('event_type', models.CharField(max_length=50)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('interested', models.ManyToManyField(blank=True, related_name='interested', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
