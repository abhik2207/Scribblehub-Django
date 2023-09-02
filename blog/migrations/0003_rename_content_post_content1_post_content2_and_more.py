# Generated by Django 4.1.7 on 2023-04-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='content1',
        ),
        migrations.AddField(
            model_name='post',
            name='content2',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='content3',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='heading1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='heading2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='heading3',
            field=models.CharField(default='', max_length=100),
        ),
    ]