# Generated by Django 4.2.1 on 2023-05-30 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_parafernalia_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parafernalia',
            name='imagen',
            field=models.ImageField(null=True, upload_to='items'),
        ),
    ]