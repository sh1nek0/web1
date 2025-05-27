from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_like_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
    ]
