# Generated by Django 3.2 on 2023-01-26 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enter', '0002_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.RemoveField(
            model_name='record',
            name='date',
        ),
        migrations.AddField(
            model_name='record',
            name='status',
            field=models.CharField(default='IN', max_length=4),
        ),
        migrations.AlterField(
            model_name='record',
            name='entrytime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='exittime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
