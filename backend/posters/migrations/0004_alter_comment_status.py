# Generated by Django 4.1.2 on 2022-11-02 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0003_alter_category_options_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.IntegerField(null=True),
        ),
    ]
