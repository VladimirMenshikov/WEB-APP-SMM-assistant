# WEB-APP-SMM-assistant
*Веб-приложение с использованием Flask, реализующее функционал генерации постов и изображений с последующей автопубликацией в ВКонтакте. Приложение поддерживает регистрацию и авторизацию пользователей, с сохранением кодов для доступа к сообществу ВК для автопубликации постов.*

## Описание работы веб-приложения

Наше веб-приложение — удобный инструмент для генерации контента и управления постами в ВКонтакте.

🔹 Регистрация и вход
При первом открытии необходимо зарегистрироваться, придумав логин и пароль. Вход в аккаунт осуществляется с этими данными, которые сохраняются на время сессии.

🔹 Настройки
В разделе "Настройки" можно ввести ID группы и API-ключ ВКонтакте. Если эти данные отсутствуют, приложение позволит создать текст и изображение, но без автопостинга.

🔹 Генерация контента
Во вкладке "Генерация" можно:

- Выбрать тему и тональность поста
- Определить, требуется ли публикация в ВК
- Настроить автоматическое создание изображения

🔹 Статистика
При наличии API-ключа и ID группы во вкладке "Статистика" отображаются аналитические данные сообщества ВКонтакте.

## Инструменты:
- **Фреймворк Flask** - для создания структуры веб приложения;
- **Сервис PythonAnywhere** - для публикации веб приложения в сети интернет
- **API OpenAI** - для генерации текста, промпта и изображения
- **Python** - для формирования логики приложения

## Веб приложение

- [**Доступ к веб приложению**](https://vladzc.pythonanywhere.com/): Демонстрация работы приложения.
- [**Скриншоты**]()
- [**Примеры файлов Python**]() 
