# Generated by Django 3.2.15 on 2022-09-14 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220914_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='difficulty',
            field=models.CharField(choices=[('easy', 'Easy'), ('moderate', 'Moderate'), ('challenging', 'Challenging')], default='none', max_length=55),
        ),
        migrations.AlterField(
            model_name='post',
            name='dog_friendly',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='none', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='environment',
            field=models.CharField(choices=[('coastal', 'Coastal'), ('woodland', 'Woodland'), ('countryside', 'Countryside'), ('moorland', 'Moorland'), ('hill', 'Hill'), ('mountain', 'Mountain'), ('peak', 'Peak'), ('other', 'Other')], default='none', max_length=55),
        ),
        migrations.AlterField(
            model_name='post',
            name='wc',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='none', max_length=20),
        ),
    ]
