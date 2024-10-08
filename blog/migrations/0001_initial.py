# Generated by Django 4.2.2 on 2024-09-02 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("heading", models.CharField(max_length=50, verbose_name="Заголовок")),
                (
                    "content_of_article",
                    models.TextField(verbose_name="Содержимое статьи"),
                ),
                (
                    "picture",
                    models.ImageField(upload_to="blog/", verbose_name="Изображение"),
                ),
                (
                    "number_of_views",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Количество просмотров"
                    ),
                ),
                (
                    "date_of_publication",
                    models.DateField(auto_now_add=True, verbose_name="Дата публикации"),
                ),
            ],
            options={
                "verbose_name": "Блог",
                "verbose_name_plural": "Блоги",
            },
        ),
    ]
