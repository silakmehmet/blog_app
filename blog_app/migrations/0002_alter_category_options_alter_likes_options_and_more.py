# Generated by Django 5.1 on 2024-08-22 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='likes',
            options={'verbose_name': 'Likes', 'verbose_name_plural': 'Likes'},
        ),
        migrations.AlterModelOptions(
            name='postviews',
            options={'verbose_name': 'Post View', 'verbose_name_plural': 'Post Views'},
        ),
    ]
