# Generated by Django 2.2.6 on 2019-10-27 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0013_auto_20191027_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', models.TextField(blank=True, null=True)),
                ('image', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
