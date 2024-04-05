# Allure-Selenium
Автотесты на Selenium+Allure для сайта визитки https://kir-qa.github.io/

# Установка Python
Скачиваем файл-установщик с официального сайта https://www.python.org/downloads/
Во время установки пользователям Windows обязательно нужно поставить галочку «Add Python to PATH», затем Install Now
Установить библиотеки:

    pip install pytest
    pip install selenium
    pip install allure-pytest
    
Установка и настройка Visual Studio Code
Если у тебя еще не установлен VS Code, скачивай файл-установщик с официального сайта
https://code.visualstudio.com/
(если у тебя macOS, выбирай ссылку для мака со Stable)
Щелкай «Далее» до момента Выбора дополнительных задач
Здесь обязательно поставь галочку «Добавить в PATH» Открывай VS Code и переходи в Extensions (Расширения), вводи Python и нажимай Install

# Allure Report - установка для разных операционных систем разная
1. Для MacOS выполнить команды:
    
        brew install allure
  Если `brew` не установлен
  Установи Brew — это установщик всего остального.
  Запусти скрипт ниже в терминале
  
            jsx
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  - Если получаешь ошибку, типа `command not found: brew`
  - Про установку Homebrew: [Сылка](https://trofimovdigital.ru/blog/homebrew)
  - Как установить Homebrew на m1 [Сылка тута](https://it-here.ru/instruktsii/kak-ustanovit-i-ispolzovat-homebrew-na-m1-mac/)
2. Для Linux (на базе Debian)
        
        sudo apt-add-repository ppa:qameta/allure
        sudo apt-get update
        sudo apt-get install allure
        
3. Для Windows. [Скачиваем](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.19.0/allure-commandline-2.19.0.zip) и кладем **распакованный** каталог рядом с нашим проектом.
4. Запуск allure прост:
            
       - В Windows находим в каталоге *allure\bin* файл *allure.bat* и запускаем на выполнение
       - На Linux/Mac выполняем файл рядом *./allure*
    
5. Если при запуске Allure будет ошибка, связанная с отсутствием каких-то компонент, то необходимо установить [Java](https://www.java.com/ru/download/manual.jsp).
Скачать проект из github и открыть в IDE https://github.com/Kir-QA/Allure-Selenium Открыть проэкт в VS CODE
