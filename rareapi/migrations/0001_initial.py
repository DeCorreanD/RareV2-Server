# Generated by Django 3.2 on 2023-06-20 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateField()),
                ('image_url', models.URLField()),
                ('content', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=100)),
                ('profile_image_url', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('created_on', models.DateField()),
                ('active', models.BooleanField(blank=True, null=True)),
                ('uid', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField()),
                ('ended_on', models.DateField()),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_id', to='rareapi.user')),
                ('follower_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_id', to='rareapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.post')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.tag')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='rare_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.user'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(blank=True, null=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.user')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.post')),
            ],
        ),
    ]
