# Generated by Django 4.1.7 on 2023-04-04 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebTest', '0004_list_test_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='list_test',
            name='count_treing',
            field=models.IntegerField(default=0, verbose_name='Кол-во попыток в тесте'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='list_test',
            name='cover',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Абложка теста'),
        ),
    ]
