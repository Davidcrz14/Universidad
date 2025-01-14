# Generated by Django 5.1.3 on 2024-11-08 08:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institutos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('file', models.FileField(upload_to='files/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('career', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='institutos.career')),
                ('institute', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='institutos.institute')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='institutos.subject')),
            ],
        ),
    ]
