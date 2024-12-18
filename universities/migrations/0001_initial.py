# Generated by Django 5.1.4 on 2024-12-16 06:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='University_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=100)),
                ('Est_Date', models.DateField()),
                ('University_Description', models.CharField(default='', max_length=200)),
                ('Vice_Chancellor', models.CharField(max_length=40)),
                ('Chancellor', models.CharField(max_length=40)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='university_detail_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='university_detail_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'University_Details',
                'verbose_name_plural': 'University_Details',
            },
        ),
        migrations.CreateModel(
            name='user_university',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_university_created_by', to=settings.AUTH_USER_MODEL)),
                ('university', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='universities.university_details')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_university_updated_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
