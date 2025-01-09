# Generated by Django 4.2.15 on 2024-12-05 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('publication_year', models.PositiveIntegerField()),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('description', models.TextField()),
                ('cover_image_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
