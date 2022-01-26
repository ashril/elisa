# Generated by Django 4.0 on 2022-01-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elisaapp', '0002_alter_pic_kontak_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keterangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keterangan', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_role', models.CharField(max_length=20)),
                ('fase', models.IntegerField(null=True)),
            ],
        ),
    ]
