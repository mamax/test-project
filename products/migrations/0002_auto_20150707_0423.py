# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u0442\u0432\u043e\u0440\u0435\u043d\u043d\u044f'),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_at',
            field=models.DateField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0437\u043c\u0456\u043d\u0435\u043d\u043d\u044f'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(verbose_name='\u0426\u0456\u043d\u0430', max_digits=5, decimal_places=2),
        ),
    ]
