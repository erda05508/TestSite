# Generated by Django 3.1.7 on 2021-11-15 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0002_product_users_wishlist"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("created_at",),
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="internalnumber",
            field=models.PositiveSmallIntegerField(
                blank=True, default=1, verbose_name="Внутренний номер"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="inventorynumber",
            field=models.IntegerField(
                blank=True, default=0, verbose_name="Инвентарный №"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="rozport",
            field=models.PositiveSmallIntegerField(
                blank=True, default=1, verbose_name="Розетка(порт)"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="serialnumber",
            field=models.CharField(
                blank=True, default=0, max_length=50, verbose_name="Серийниый №"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="signature",
            field=models.BooleanField(default=False, verbose_name="Роспись"),
        ),
    ]
