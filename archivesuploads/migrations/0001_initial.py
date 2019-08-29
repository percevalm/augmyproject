# Generated by Django 2.1.4 on 2019-03-19 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivesuploads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=2000, null=True)),
                ('title', models.TextField(blank=True, max_length=2000, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='archives')),
                ('size', models.CharField(blank=True, max_length=200, null=True)),
                ('url', models.URLField(blank=True, max_length=500, null=True)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('general_doi', models.CharField(max_length=2000)),
            ],
            options={
                'verbose_name_plural': 'Archive uploads',
            },
        ),
        migrations.CreateModel(
            name='Archivetypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=2000, null=True)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'verbose_name_plural': 'Archive types',
            },
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=2000, null=True)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Interests',
            },
        ),
        migrations.AddField(
            model_name='archivesuploads',
            name='archivetype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ArchiveType', to='archivesuploads.Archivetypes'),
        ),
        migrations.AddField(
            model_name='archivesuploads',
            name='journal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='InterestsType', to='archivesuploads.Interests'),
        ),
    ]
