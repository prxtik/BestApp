# Generated by Django 2.1.5 on 2019-02-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_requestlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='supply',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
