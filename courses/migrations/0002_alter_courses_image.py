# Generated by Django 5.0.6 on 2024-06-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses', verbose_name='картинка'),
        ),
    ]