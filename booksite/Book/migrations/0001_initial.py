# Generated by Django 2.2 on 2022-04-03 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(default='uncategorized', max_length=200)),
                ('desc', models.CharField(max_length=1000)),
                ('rating', models.FloatField()),
                ('image', models.ImageField(default='images/none/noimg.jpg', upload_to='images')),
            ],
        ),
    ]