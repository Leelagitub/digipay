# Generated by Django 4.2.4 on 2023-09-07 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccounts', '0004_alter_kyc_identity_image_alter_kyc_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc',
            name='identity_image',
            field=models.ImageField(upload_to='userimg/'),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='image',
            field=models.ImageField(upload_to='userimg/'),
        ),
        migrations.AlterField(
            model_name='kyc',
            name='signature',
            field=models.ImageField(upload_to='userimg/'),
        ),
    ]
