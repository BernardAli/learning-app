# Generated by Django 3.2.4 on 2021-06-17 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('page', '0001_initial'),
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='pages',
            field=models.ManyToManyField(to='page.Page'),
        ),
        migrations.AlterField(
            model_name='module',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
