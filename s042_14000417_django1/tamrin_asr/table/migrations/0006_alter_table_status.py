# Generated by Django 3.2.5 on 2021-07-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0005_auto_20210708_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='status',
            field=models.CharField(choices=[('FU', 'full'), ('RE', 'reserve'), ('FR', 'free')], default='FR', max_length=10),
        ),
    ]
