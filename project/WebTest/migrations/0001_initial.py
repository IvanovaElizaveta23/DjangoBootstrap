# Generated by Django 4.1.7 on 2023-03-23 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='List_test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name='Название теста')),
                ('time_start', models.DateTimeField(verbose_name='Время начало теста')),
                ('time_end', models.DateTimeField(verbose_name='Время окончания теста')),
                ('count_answer', models.IntegerField(verbose_name='Кол-во вопросов в тесте')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebTest.category', verbose_name='Категория теста')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.CharField(max_length=5000000, verbose_name='Ответы на тест')),
                ('status', models.CharField(max_length=20, verbose_name='Статус теста')),
                ('time', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Время прохождения теста')),
                ('list_test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebTest.list_test', verbose_name='Название теста')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя пользователя')),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результаты',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(max_length=1500, verbose_name='Вопрос')),
                ('answer1', models.TextField(max_length=1500, verbose_name='Ответ 1')),
                ('answer2', models.TextField(max_length=1500, verbose_name='Ответ 2')),
                ('answer3', models.TextField(max_length=1500, verbose_name='Ответ 3')),
                ('answer4', models.TextField(max_length=1500, verbose_name='Ответ 4')),
                ('trueAnswer', models.CharField(max_length=20, verbose_name='Номер правильного ответа')),
                ('ltest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebTest.list_test', verbose_name='Название теста')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]
