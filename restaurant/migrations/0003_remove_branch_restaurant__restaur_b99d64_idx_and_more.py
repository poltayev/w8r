# Generated by Django 4.1.7 on 2023-04-03 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_rename_branchingredients_branchingredient_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='branch',
            name='restaurant__restaur_b99d64_idx',
        ),
        migrations.RemoveIndex(
            model_name='branchingredient',
            name='restaurant__ingredi_a8839b_idx',
        ),
        migrations.RemoveIndex(
            model_name='menu',
            name='restaurant__branch__c29790_idx',
        ),
        migrations.RemoveIndex(
            model_name='menuposition',
            name='restaurant__menu_id_bb20bc_idx',
        ),
        migrations.RemoveIndex(
            model_name='order',
            name='restaurant__branch__a21e49_idx',
        ),
        migrations.RemoveIndex(
            model_name='orderitem',
            name='restaurant__order_i_7a61a8_idx',
        ),
        migrations.RemoveIndex(
            model_name='table',
            name='restaurant__branch__de0911_idx',
        ),
        migrations.RemoveIndex(
            model_name='waiter',
            name='restaurant__branch__2c071a_idx',
        ),
    ]