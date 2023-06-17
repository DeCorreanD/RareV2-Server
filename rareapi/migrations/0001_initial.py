# Generated by Django 4.2.2 on 2023-06-15 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_id', models.CharField(max_length=50)),
                ('author_id', models.CharField(max_length=50)),
                ('created_on', models.CharField(max_length=50)),
                ('ended_on', models.CharField(max_length=50)),

            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=50)),
                ('artist_id', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
