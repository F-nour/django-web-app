# Generated by Django 4.1.2 on 2022-10-15 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listings'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='like_new',
            field=models.BooleanField(default=True),
        ),
    ]