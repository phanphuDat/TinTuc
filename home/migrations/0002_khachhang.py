# Generated by Django 3.1.4 on 2020-12-11 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KhachHang',
            fields=[
                ('KH_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.TextField(blank=True, null=True)),
                ('tenDayDu', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
