# Generated by Django 2.1.4 on 2018-12-17 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20181217_1145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='history',
            new_name='arabic_history',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='since',
            new_name='arabic_name',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='name',
            new_name='mtm_meaning',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='title',
            new_name='mtm_name',
        ),
        migrations.AddField(
            model_name='home',
            name='arabic_since',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='mtm_history',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='mtm_since',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]