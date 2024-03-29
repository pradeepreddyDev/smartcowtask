# Generated by Django 2.2.6 on 2019-10-27 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0005_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='photos/')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='project_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
