# Generated by Django 2.0.8 on 2018-09-10 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loteam', '0018_auto_20180907_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ymon',
            name='ycp4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loteam.YCP4'),
        ),
    ]