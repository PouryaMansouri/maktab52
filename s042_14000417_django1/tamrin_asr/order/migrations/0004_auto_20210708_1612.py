# Generated by Django 3.2.5 on 2021-07-08 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='status',
            field=models.CharField(choices=[('P', 'Pay'), ('N', 'Not Pay')], default='N', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('A', 'Accept'), ('P', 'Pending'), ('R', 'Reject')], default='P', max_length=10),
        ),
    ]
