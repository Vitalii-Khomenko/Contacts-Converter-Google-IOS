# VCard to iOS/macOS Converter / Конвертер контактов для iOS и macOS

**[English](#english) | [Русский](#русский)**

---

## English

### The Problem
When migrating contacts from Android (Google Contacts) to Apple devices (iPhone, MacBook), users often encounter significant issues:
1.  **Garbled Text:** Cyrillic or special characters appear as unreadable codes (e.g., `=D0=90...`) because Google exports in VCard 2.1 with Quoted-Printable encoding, which isn't always handled correctly during import.
2.  **Incomplete Imports:** The import process might stop halfway (e.g., importing only 355 out of 447 contacts). This happens because some contact fields contain hidden newline characters or formatting errors that break the VCard structure, causing macOS/iOS to abort the rest of the file.

### The Solution
This Python script solves these problems by:
-   **Converting VCard 2.1 to 3.0:** The standard format preferred by Apple devices.
-   **Decoding Quoted-Printable:** Automatically fixes broken text encoding.
-   **Sanitizing Data:** Removes invalid newline characters and fixes split lines that cause partial imports.

### Features
-   Converts `.vcf` files from version 2.1 to 3.0.
-   Decodes Quoted-Printable characters (fixes Cyrillic/UTF-8 issues).
-   **Fixes "Partial Import" bug:** Ensures all contacts are imported by removing structural errors.
-   Preserves Name (`N`), Formatted Name (`FN`), and Phone Numbers (`TEL`).
-   Maps phone types (CELL, HOME, WORK, etc.).

### Usage
1.  **Install Python** (if not already installed). No external libraries are required (uses standard libraries).
2.  **Run the script** in your terminal:
    ```bash
    python convert_contacts.py input_file.vcf
    ```
    *Example:* `python convert_contacts.py contacts.vcf`

3.  **Result**: A new file named `input_file_ios.vcf` will be created.
    -   **For iPhone:** Send this file to your device (AirDrop, Email, Telegram) and tap to import.
    -   **For macOS:** Double-click the file to import into the Contacts app.

---

## Русский

### Проблема
При переносе контактов с Android (Google Contacts) на устройства Apple (iPhone, MacBook) пользователи часто сталкиваются с проблемами:
1.  **"Крякозябры" в именах:** Кириллица отображается как набор символов (например, `=D0=90...`). Это происходит из-за того, что Google экспортирует контакты в старом формате VCard 2.1 с кодировкой Quoted-Printable.
2.  **Неполный импорт:** Импорт контактов может прерваться на середине (например, импортируется только 355 контактов из 447). Это случается, если внутри полей контакта (например, в имени) встречаются скрытые символы переноса строки, которые ломают структуру файла, и macOS/iOS перестают читать файл дальше.

### Решение
Этот скрипт исправляет файл контактов:
-   **Конвертирует VCard 2.1 в 3.0:** Формат, который "любят" устройства Apple.
-   **Декодирует Quoted-Printable:** Исправляет отображение имен.
-   **Чистит данные:** Удаляет лишние переносы строк и исправляет ошибки структуры, из-за которых терялась часть контактов.

### Возможности
-   Конвертация `.vcf` из версии 2.1 в 3.0.
-   Исправление кодировки (Quoted-Printable -> UTF-8).
-   **Исправление ошибки "Частичного импорта":** Гарантирует, что загрузятся все контакты, а не только первая половина.
-   Сохраняет Фамилию/Имя (`N`), Полное имя (`FN`) и Телефоны (`TEL`).
-   Распознает типы номеров (Мобильный, Домашний, Рабочий и др.).

### Использование
1.  **Установите Python** (если еще не установлен). Дополнительные библиотеки устанавливать не нужно.
2.  **Запустите скрипт** в терминале (командной строке):
    ```bash
    python convert_contacts.py ваш_файл.vcf
    ```
    *Пример:* `python convert_contacts.py contacts.vcf`

3.  **Результат**: Будет создан новый файл с именем `ваш_файл_ios.vcf`.
    -   **Для iPhone:** Отправьте файл себе (AirDrop, Telegram, почта) и откройте его.
    -   **Для macOS:** Просто дважды кликните по файлу, чтобы добавить контакты в адресную книгу.
