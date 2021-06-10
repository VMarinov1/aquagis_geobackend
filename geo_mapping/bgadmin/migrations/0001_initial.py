# Generated by Django 3.1.7 on 2021-03-05 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ekatte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=16)),
                ('ekatte', models.CharField(max_length=8)),
                ('tvm', models.CharField(max_length=8)),
                ('ekatte_name', models.CharField(max_length=32)),
                ('oblast', models.CharField(max_length=16)),
                ('obstina', models.CharField(max_length=16)),
                ('kmetstvo', models.CharField(max_length=16)),
                ('kind', models.CharField(max_length=16)),
                ('category', models.CharField(max_length=16)),
                ('altitude', models.CharField(max_length=16)),
                ('document', models.CharField(max_length=24)),
                ('tsb', models.CharField(max_length=16)),
                ('abc', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Ekdoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=16)),
                ('document', models.CharField(max_length=8)),
                ('doc_kind', models.CharField(max_length=32)),
                ('doc_name', models.CharField(max_length=256)),
                ('doc_inst', models.CharField(max_length=512)),
                ('doc_num', models.CharField(max_length=32)),
                ('doc_date', models.DateField()),
                ('doc_act', models.DateField()),
                ('dv_danni', models.CharField(blank=True, max_length=16, null=True)),
                ('dv_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Oblast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=16)),
                ('oblast', models.CharField(max_length=16)),
                ('ekatte', models.CharField(max_length=8)),
                ('obl_name', models.CharField(max_length=32)),
                ('region', models.CharField(max_length=8)),
                ('document', models.CharField(max_length=8)),
                ('abc', models.CharField(max_length=8)),
            ],
        ),
    ]
