


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_auto_20220108_2132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-date']},
        ),
    ]
