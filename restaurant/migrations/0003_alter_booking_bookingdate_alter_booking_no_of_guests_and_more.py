# Generated by Django 5.0.3 on 2024-03-28 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_bookingdate_alter_booking_no_of_guests_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bookingDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(default=6),
        ),
    ]
