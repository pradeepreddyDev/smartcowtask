# Generated by Django 2.2.6 on 2019-10-27 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0011_auto_20191027_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='project',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
