# Generated by Django 2.0.2 on 2018-07-28 13:14

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_is_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='课程详情'),
        ),
    ]