# Generated by Django 3.1.6 on 2021-02-21 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('players', '0002_auto_20210220_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tags.Tag'),
        ),
    ]
