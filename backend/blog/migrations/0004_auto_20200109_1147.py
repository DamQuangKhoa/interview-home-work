# Generated by Django 3.0.2 on 2020-01-09 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200109_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblog',
            name='created_at',
            field=models.CharField(default=1576506719083, max_length=250),
            preserve_default=False,
        ),
    ]
