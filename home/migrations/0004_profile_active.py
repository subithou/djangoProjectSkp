# Generated by Django 3.2.9 on 2022-03-12 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auction_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='active',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]