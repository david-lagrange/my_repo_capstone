# Generated by Django 3.2.8 on 2021-12-15 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='zip_code',
            field=models.CharField(default='53074', max_length=11),
            preserve_default=False,
        ),
    ]