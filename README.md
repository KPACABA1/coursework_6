Здравствуйте мой проект на ос Linux Ubuntu.

Для того чтобы проект работал обязательно выполните в терминале команду 'python manage.py crontab add', без нее не будет работать переодическая расслыка.

Я использую виртуальное окружение Pipenv поэтому не забудьте установить все пакеты из requirements.txt.

В этом проекте я реализовал сервис управления рассылками, администрирования и получения статистики. Он заключается в том, что:
  1. Создан интерфейс заполнения рассылок, то есть CRUD-механизм для управления рассылками;
  2. Реализован скрипт рассылки, который работает как из командной строки, так и по расписанию. Для того чтобы выполнить эту задачу я использовал планировщик задач crontab.
  Так же в скрипт рассылки я интегрировал анализ попыток рассылок, который исходя из периодичности рассылки записывает дату и время последней попытки рассылки, записывает статус попытки (успешно / не успешно).

Регистрация пользователя происходит по почте с обязательной верификацией
