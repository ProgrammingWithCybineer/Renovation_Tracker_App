# Generated by Django 3.2.5 on 2022-10-01 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebAppRenoTracker', '0004_auto_20221001_0226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newproject',
            old_name='afterPhoto1',
            new_name='after_Photo1',
        ),
        migrations.RenameField(
            model_name='newproject',
            old_name='afterPhoto2',
            new_name='after_Photo2',
        ),
        migrations.RenameField(
            model_name='newproject',
            old_name='afterPhoto3',
            new_name='after_Photo3',
        ),
        migrations.RenameField(
            model_name='newproject',
            old_name='afterPhoto4',
            new_name='after_Photo4',
        ),
        migrations.RenameField(
            model_name='newproject',
            old_name='beforePhoto1',
            new_name='before_Photo1',
        ),
        migrations.RenameField(
            model_name='newproject',
            old_name='beforePhoto2',
            new_name='before_Photo2',
        ),
        migrations.RenameField(
            model_name='newproject',
            old_name='beforePhoto3',
            new_name='before_Photo3',
        ),
        migrations.RenameField(
            model_name='newproject',
            old_name='beforePhoto4',
            new_name='before_Photo4',
        ),
        migrations.RenameField(
            model_name='newproject',
            old_name='author',
            new_name='updated_By',
        ),
    ]