# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('slug', models.SlugField(verbose_name='\u041a\u043e\u0440\u043e\u0442\u043a\u0430 \u043d\u0430\u0437\u0432\u0430-\u043c\u0456\u0442\u043a\u0430')),
                ('description', models.CharField(max_length=256, verbose_name='\u041e\u043f\u0438\u0441')),
                ('price', models.FloatField(verbose_name='\u0426\u0456\u043d\u0430')),
                ('created_at', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0441\u0442\u0432\u043e\u0440\u0435\u043d\u043d\u044f')),
                ('modified_at', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0437\u043c\u0456\u043d\u0435\u043d\u043d\u044f', blank=True)),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442',
                'verbose_name_plural': '\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u0438',
            },
        ),
    ]
