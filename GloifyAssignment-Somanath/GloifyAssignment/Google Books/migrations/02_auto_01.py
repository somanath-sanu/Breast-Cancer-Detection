# Generated by Django 2.2.4 on 2019-08-11 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlebooks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='id',
        ),
        migrations.AddField(
            model_name='books',
            name='ID',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='detail',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]