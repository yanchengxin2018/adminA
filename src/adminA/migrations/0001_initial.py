# Generated by Django 4.2.1 on 2024-06-29 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminAConfModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(help_text='项目代码', max_length=100)),
                ('data', models.TextField(help_text='配置数据', null=True)),
                ('close', models.BooleanField(default=False, help_text='禁用')),
            ],
        ),
    ]
