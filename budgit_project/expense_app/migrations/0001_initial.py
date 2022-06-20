# Generated by Django 2.2.4 on 2022-06-20 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('category', models.CharField(blank=True, choices=[('H', 'Housing'), ('T', 'Transportation'), ('F', 'Food'), ('I', 'Insurance'), ('U', 'Utilities'), ('E', 'Entertainment'), ('M', 'Medical/Healthcare'), ('S', 'Supplies/Toiletries'), ('P', 'Personal'), ('O', 'Other')], max_length=50)),
                ('recurring', models.BooleanField(default='False')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='users_app.User')),
            ],
        ),
    ]