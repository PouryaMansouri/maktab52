# Generated by Django 3.2.5 on 2021-07-08 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210708_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('A', 'Accept'), ('R', 'Reject'), ('P', 'Pending')], default='P', max_length=10),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='status',
            field=models.CharField(choices=[('N', 'Not Pay'), ('P', 'Pay')], default='N', max_length=10),
        ),
    ]