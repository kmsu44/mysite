# Generated by Django 4.0.3 on 2022-05-21 12:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0003_delete_answer_delete_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Modify_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 5, 21, 12, 14, 5, 966893, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
