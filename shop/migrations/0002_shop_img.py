# Generated by Django 4.1.6 on 2023-07-18 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='img',
            field=models.ImageField(default='exit', upload_to=''),
            preserve_default=False,
        ),
    ]
