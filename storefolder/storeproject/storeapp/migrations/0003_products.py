# Generated by Django 4.2.3 on 2023-08-02 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_courses_features_trainers_remove_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desptn', models.TextField()),
            ],
        ),
    ]
