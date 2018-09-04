# Generated by Django 2.0.8 on 2018-09-03 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loteam', '0005_ymon_ycp4'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ymon',
            name='ycp4',
        ),
        migrations.AlterField(
            model_name='ymon',
            name='Material',
            field=models.ForeignKey(default='0000', on_delete=django.db.models.deletion.CASCADE, to='loteam.YCP4'),
        ),
    ]