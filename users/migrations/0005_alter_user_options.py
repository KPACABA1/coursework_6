# Generated by Django 4.2.2 on 2024-08-29 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_user_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "permissions": [
                    ("may_block_users", "Может заблокировать пользователя"),
                    (
                        "can_view_list_of_users",
                        "Может просматривать список пользователей сервиса",
                    ),
                ],
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]
