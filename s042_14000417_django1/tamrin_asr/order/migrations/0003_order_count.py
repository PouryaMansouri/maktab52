# Generated by Django 3.2.5 on 2021-07-08 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
