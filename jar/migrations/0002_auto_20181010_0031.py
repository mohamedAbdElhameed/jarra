# Generated by Django 2.1 on 2018-10-09 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderSchema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(default=85216, max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='myuser',
            name='order_id',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
