# Generated by Django 4.1.5 on 2023-02-09 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_comment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]