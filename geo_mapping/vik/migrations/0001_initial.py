# Generated by Django 3.1.7 on 2021-03-05 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Select',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user_name', models.CharField(blank=True, max_length=64, null=True)),
                ('geom', models.TextField()),
                ('inside_only', models.BooleanField(default=False)),
            ],
        ),
    ]
