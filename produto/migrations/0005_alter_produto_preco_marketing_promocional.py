# Generated by Django 5.1.5 on 2025-01-28 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_alter_produto_preco_marketing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(blank=True, default=0, verbose_name='Preço promo'),
        ),
    ]
