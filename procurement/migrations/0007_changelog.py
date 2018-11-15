# Generated by Django 2.0.8 on 2018-11-15 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procurement', '0006_delete_changelog'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeLog',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('SA_No', models.IntegerField(blank=True, null=True)),
                ('DateTime', models.DateTimeField(blank=True, null=True)),
                ('User', models.CharField(max_length=30)),
                ('Field', models.CharField(max_length=30)),
                ('Before', models.CharField(blank=True, max_length=50, null=True)),
                ('After', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
