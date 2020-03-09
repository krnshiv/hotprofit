# Generated by Django 2.2.4 on 2020-03-09 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_auto_20200309_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('M', 'meat'), ('OT', 'others'), ('DBG', 'Dry/BakingGoods'), ('VEG', 'veggies'), ('BEV', 'bevrages'), ('DA', 'Dairy'), ('FR', 'fruits'), ('HE', 'herbs'), ('PG', 'PaperGoods'), ('CL', 'cleaners'), ('SP', 'spices'), ('UT', 'utensils'), ('CG', 'CannedGoods'), ('BR', 'Bread/Bakery')], default=None, max_length=120, null=True),
        ),
    ]
