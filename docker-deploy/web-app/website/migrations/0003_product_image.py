# Generated by Django 3.0.5 on 2020-04-23 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200418_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='loading.png', upload_to=''),
        ),
    ]
