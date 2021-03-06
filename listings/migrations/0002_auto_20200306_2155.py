# Generated by Django 2.2.4 on 2020-03-06 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('BR', 'Bread/Bakery'), ('UT', 'utensils'), ('VEG', 'veggies'), ('SP', 'spices'), ('FR', 'fruits'), ('CG', 'CannedGoods'), ('BEV', 'bevrages'), ('M', 'meat'), ('OT', 'others'), ('DBG', 'Dry/BakingGoods'), ('PG', 'PaperGoods'), ('CL', 'cleaners'), ('DA', 'Dairy'), ('HE', 'herbs')], default=None, max_length=120),
        ),
    ]
