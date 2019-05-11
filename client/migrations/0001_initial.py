# Generated by Django 2.2 on 2019-05-11 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('AU', 'Admin'), ('NU', 'User')], default='NU', max_length=100, verbose_name='profile type')),
                ('status', models.CharField(choices=[('AC', 'Active'), ('IN', 'Inactive'), ('PE', 'Pending')], default='PE', max_length=30, verbose_name='status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]