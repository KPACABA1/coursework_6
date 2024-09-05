Здравствуйте мой проект на ос Linux Ubuntu.

Для того чтобы проект работал обязательно выполните в терминале команду 'python manage.py crontab add', без нее не будет работать переодическая расслыка.

Я использую виртуальное окружение Pipenv поэтому не забудьте установить все пакеты из requirements.txt.

В этом проекте я реализовал сервис управления рассылками, администрирования и получения статистики. Он заключается в том, что:
  1. Создан интерфейс заполнения рассылок, то есть CRUD-механизм для управления рассылками(немного модернизировал базовую форму так: при создании сообщения и клиентов им автоматически присваивается имя того кто их создал и при создании рассылки в полях сообщение и клиенты можно выбрать только те экземпляры модели, создатель которых соответсвует авторизованному пользователю);
  2. Реализован скрипт рассылки, который работает как из командной строки, так и по расписанию. Для того чтобы выполнить эту задачу я использовал планировщик задач crontab.
  Так же в скрипт рассылки я интегрировал анализ попыток рассылок, который исходя из периодичности рассылки записывает дату и время последней попытки рассылки, записывает статус попытки (успешно / не успешно).

Регистрация пользователя происходит по почте с обязательной верификациейю. Так же вы можете создать админа через команду csu, которая находится в директории users

Верификация происходит следующим образом: пользовать изначально является неактивным при регистрации, далее для него генерируется токен. Ссылка с этим токеном приходит ему на почту. Если пользователь перейдёт по ссылке с этим токеном, то он станет активным и сможет войти в систему

В проекте есть группа модераторов. Я сделал специальную фикстуру для этой группы, она находится в groups.json

У модераторов есть следующие права:
  1. Могут просматривать любые рассылки;
  2. Могут просматривать список пользователей сервиса;
  3. Могут блокировать пользователей сервиса;
  4. Могут отключать рассылки

А так же у модераторов присутствуют ограничения:
  1. Не могут редактировать рассылки;
  2. Не могут управлять списком рассылок;
  3. Не могут изменять сообщения

Пользователь не может изменить чужую рассылку, а так же может работать только со своим списком клиентов и со своим списком рассылок.

Реализована главная страница которая отражает:
  1. Количество рассылок всего;
  2. Количество активных рассылок;
  3. Количество уникальных клиентов для рассылок;
  4. Три случайные статьи из блога

Так же сделал кэширование контроллера для рассылок
  
