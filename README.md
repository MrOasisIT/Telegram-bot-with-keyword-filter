# Telegram-bot-with-keyword-filter
## Логирование: Полное отслеживание работы бота и ошибок.
## Технологии
 * Python 3.10+
 * aiogram 3.x (Asyncio)
 * python-dotenv
## Установка
 * Склонируйте репозиторий:
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)

 * Создайте и активируйте виртуальное окружение:
   python -m venv venv
source venv/bin/activate  # Для Linux/macOS
venv\Scripts\activate     # Для Windows

 * Установите зависимости:
   pip install -r requirements.txt

 * Создайте файл .env в корневой папке и добавьте туда ваш токен:
   TOKEN=ваш_токен_бота

## Использование
Бот автоматически отслеживает сообщения в группах и пересылает администратору те, что содержат заданные ключевые слова
