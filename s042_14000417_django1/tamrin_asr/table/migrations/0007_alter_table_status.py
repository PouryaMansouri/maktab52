# Generated by Django 3.2.5 on 2021-07-08 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0006_alter_table_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='status',
            field=models.CharField(choices=[('FU', 'full'), ('RE', 'reserve'), ('FR', 'free')], default='FR', max_length=10),
        ),
    ]
