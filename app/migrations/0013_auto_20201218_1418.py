# Generated by Django 3.1.3 on 2020-12-18 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_auto_20201210_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_item', to='app.item'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_currency', to='app.currency'),
        ),
        migrations.AlterField(
            model_name='money',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='money_currency', to='app.currency'),
        ),
        migrations.AlterField(
            model_name='money',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='money_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='offer',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offer_item', to='app.item'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offer_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='price',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='item_price', to='app.item'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trade_item', to='app.item'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='watchlist_items', to='app.Item'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist_user', to=settings.AUTH_USER_MODEL),
        ),
    ]