# Generated by Django 2.2.2 on 2019-06-24 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoplemanager', '0005_auto_20190624_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffdetail',
            name='qualification',
            field=models.CharField(blank=True, choices=[('BCom', 'BCom'), ('BTech', 'BTech'), ('BSc', 'BSc'), ('Hons', 'Hons'), ('Mtech', 'Mtech'), ('MSc', 'MSc'), ('PhD', 'PhD')], max_length=8, null=True),
        ),
    ]
