# Generated by Django 4.1.4 on 2022-12-30 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0002_alter_appuser_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('C', 'completed'), ('P', 'pending')], max_length=2)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_todo.appuser')),
            ],
        ),
    ]
