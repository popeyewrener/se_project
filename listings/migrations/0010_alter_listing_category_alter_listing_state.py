# Generated by Django 4.2.7 on 2023-11-21 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0009_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Cars', 'Cars'), ('Books&Sports', 'Books&Sports'), ('Furniture', 'Furniture'), ('Property', 'Property'), ('Mobiles', 'Mobiles'), ('Bikes', 'Bikes'), ('Jobs', 'Jobs'), ('Fashion', 'Fashion')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('WB', 'West Bengal'), ('TN', 'Tamil Nadu'), ('HP', 'Haryana'), ('KL', 'Kerala'), ('JH', 'Jharkhand'), ('OD', 'Odisha'), ('MH', 'Maharashtra'), ('AS', 'Assam'), ('ML', 'Meghalaya'), ('AR', 'Arunachal Pradesh'), ('TR', 'Tripura'), ('NL', 'Nagaland'), ('MI', 'Sikkim'), ('BR', 'Bihar'), ('UK', 'Uttarakhand'), ('GJ', 'Gujarat'), ('AP', 'Andhra Pradesh'), ('MN', 'Manipur'), ('CG', 'Chhattisgarh'), ('GA', 'Goa'), ('MZ', 'Mizoram'), ('PB', 'Punjab'), ('TS', 'Telegana'), ('UP', 'Uttar Pradesh'), ('RJ', 'Rajasthan'), ('KA', 'Karnataka'), ('MP', 'Madhya Pradesh')], max_length=100),
        ),
    ]
