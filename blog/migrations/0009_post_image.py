# Generated by Django 5.1.1 on 2024-09-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_post_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="upload/"),
        ),
    ]
