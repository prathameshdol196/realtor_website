# Generated by Django 5.1.4 on 2024-12-30 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('address', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='listings/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
