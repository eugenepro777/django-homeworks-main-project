# Generated by Django 4.2.9 on 2024-02-11 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_options_alter_product_added_date_and_more'),
        ('customers', '0002_alter_customer_options_alter_customer_address_and_more'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer', verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='products.product', verbose_name='Товары'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма заказа'),
        ),
    ]
