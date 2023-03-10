# Generated by Django 2.2.12 on 2023-01-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_rename_title_books_name_remove_books_categories_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AlterField(
            model_name='authors',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='authors',
            name='name',
            field=models.CharField(max_length=77),
        ),
        migrations.AlterField(
            model_name='books',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='books',
            name='name',
            field=models.CharField(max_length=66),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=111),
        ),
    ]
