# Generated by Django 4.0.4 on 2022-05-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0011_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='Media/images/default.jpg', null=True, upload_to='images/'),
        ),
    ]
