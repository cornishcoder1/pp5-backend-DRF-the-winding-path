# Generated by Django 3.2.15 on 2022-08-29 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
        ('comments_gallery', '0002_alter_gallerycomment_gallery_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerycomment',
            name='gallery_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.gallery'),
        ),
    ]