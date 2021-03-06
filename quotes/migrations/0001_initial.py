# Generated by Django 3.1.3 on 2021-04-15 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_author', models.CharField(max_length=50)),
                ('quote_body', models.TextField()),
                ('context', models.CharField(blank=True, max_length=240)),
                ('source', models.CharField(blank=True, max_length=120)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
