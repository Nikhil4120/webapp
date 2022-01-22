# Generated by Django 3.1.7 on 2022-01-19 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=10)),
                ('product_description', models.CharField(max_length=150)),
                ('product_image', models.ImageField(upload_to='')),
                ('color', models.CharField(max_length=10)),
                ('size', models.CharField(max_length=5)),
                ('price', models.DecimalField(decimal_places=3, max_digits=3)),
                ('sku_id', models.CharField(max_length=10)),
                ('is_trending', models.BooleanField(default=0)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
                ('subcategory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subcategory')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]
