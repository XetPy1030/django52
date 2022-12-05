# Generated by Django 4.1.1 on 2022-12-05 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('content', models.CharField(max_length=300, verbose_name='content')),
                ('url', models.CharField(max_length=50, verbose_name='url')),
            ],
        ),
    ]