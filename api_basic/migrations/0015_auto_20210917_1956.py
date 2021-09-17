# Generated by Django 3.2.6 on 2021-09-17 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0014_auto_20210916_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enduseremail',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='api_basic.enduser'),
        ),
        migrations.AlterField(
            model_name='hrruser',
            name='end_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='api_basic.enduser'),
        ),
    ]