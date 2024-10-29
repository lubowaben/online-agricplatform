# Generated by Django 5.1 on 2024-08-27 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_supplier_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.supplier')),
            ],
        ),
    ]
