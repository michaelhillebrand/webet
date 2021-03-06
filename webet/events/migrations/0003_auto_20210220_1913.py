# Generated by Django 3.1.6 on 2021-02-21 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('events', '0002_eventteam_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='tags.Tag'),
        ),
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='tags.Tag'),
        ),
    ]
