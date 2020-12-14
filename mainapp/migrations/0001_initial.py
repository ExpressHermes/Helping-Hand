# Generated by Django 3.1.4 on 2020-12-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('event_date', models.DateField()),
                ('place_name', models.CharField(max_length=350)),
                ('event_type', models.CharField(max_length=50)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
