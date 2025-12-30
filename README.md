# VCard to iOS Converter / Конвертер контактов для iOS

**[English](#english) | [Русский](#русский)**

---

## English

A simple Python script to convert Google Contacts VCard (v2.1) exports into an iOS-compatible VCard (v3.0) format. It handles Quoted-Printable encoding (fixing Cyrillic characters) and ensures names and phone numbers are correctly recognized by iPhones.

### Features
- Converts VCard 2.1 to 3.0.
- Decodes Quoted-Printable characters (fixes broken text like `=D0=90...`).
- Preserves Name (`N`), Formatted Name (`FN`), and Phone Numbers (`TEL`).
- Maps phone types (CELL, HOME, WORK, etc.).

### Usage
1. **Install Python** (if not already installed).
2. **Run the script** in your terminal:
   ```bash
   python convert_contacts.py <input_file.vcf>
   ```
   *Example:* `python convert_contacts.py contacts.vcf`

3. **Result**: A new file named `<input_file>_ios.vcf` will be created. Send this file to your iPhone to import contacts.

---

## Русский

Простой скрипт на Python для конвертации контактов из Google (VCard v2.1) в формат, полностью совместимый с iOS (VCard v3.0). Скрипт исправляет кодировку (Quoted-Printable) и гарантирует правильное отображение имен и телефонов на iPhone.

### Возможности
- Конвертация VCard 2.1 в 3.0.
- Декодирование Quoted-Printable (исправляет "крякозябры" вида `=D0=90...`).
- Сохраняет Фамилию/Имя (`N`), Полное имя (`FN`) и Телефоны (`TEL`).
- Распознает типы номеров (Мобильный, Домашний, Рабочий и др.).

### Использование
1. **Установите Python** (если еще не установлен).
2. **Запустите скрипт** в терминале (командной строке):
   ```bash
   python convert_contacts.py <ваш_файл.vcf>
   ```
   *Пример:* `python convert_contacts.py contacts.vcf`

3. **Результат**: Будет создан новый файл с именем `<ваш_файл>_ios.vcf`. Отправьте этот файл себе на iPhone (через AirDrop, Telegram или почту) и откройте его для импорта.
