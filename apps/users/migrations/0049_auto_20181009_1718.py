# Generated by Django 2.0.2 on 2018-10-09 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0048_rundocker_port'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rundocker',
            name='port',
            field=models.CharField(default='80', max_length=200, null=True, verbose_name='port'),
        ),
    ]
