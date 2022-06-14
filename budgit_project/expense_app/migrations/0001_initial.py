# Generated by Django 2.2.4 on 2022-06-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Please include a name', max_length=50)),
                ('amount', models.IntegerField(help_text='Value must be at least $1')),
                ('category', models.CharField(blank=True, choices=[('H', 'Housing'), ('T', 'Transportation'), ('F', 'Food'), ('I', 'Insurance'), ('U', 'Utilities'), ('E', 'Entertainment'), ('M', 'Medical/Healthcare'), ('S', 'Supplies/Toiletries'), ('P', 'Personal'), ('O', 'Other')], max_length=50)),
                ('recurring', models.BooleanField(default='False')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
