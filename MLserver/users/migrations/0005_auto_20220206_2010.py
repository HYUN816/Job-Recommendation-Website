# Generated by Django 3.2.11 on 2022-02-06 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_middle_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rec_cate1',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='rec_cate2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='rec_cate3',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
