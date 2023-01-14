# Generated by Django 4.1.5 on 2023-01-14 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_cart_size_shoes_remove_cart_size_shirt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('On the Way', 'On the way'), ('ACCEPTED', 'ACCEPTED'), ('Deliverd', 'Deliverd'), ('Packed', 'Packed'), ('cancel', 'cancel')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('BW', 'Bottomwear'), ('W', '\tWATCH'), ('TW', 'Topwear'), ('SH', 'SHOES')], max_length=50),
        ),
    ]
