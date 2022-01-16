This reposotory is created for Genotek test challenge

It contains several scripts for the following task:

Нужно написать скрипт, который будет парсить вот такой файл 
(https://github.com/clintval/sample-sheet/blob/master/tests/resources/single-end-colliding-sample-ids.csv)
и создавать tsv файл, в котором будет две колонки: sample_id, fastq_file
в fastq_file маска по шаблону*: {SAMPLE_ID}.{Experiment Name}.fastq.gz

Ориентироваться надо не на номера строк, а на названия, так, например, 'Experiment Name' строка может оказаться четвертой и от этого скрипт не должен падать.
Язык Python

* **Примечание: нужно также добавлять INDEX_ID**

***Описание скриптов***
1. csv_to_tsv.py - скрипт без оптимизации: нет функционального деления на задачи, все внутри одной функции;
  применены следующие модуль argparse;
  парсинг за счет базовых возможностей языка
2. csv_to_tsv_funct.py - оптимизированный скрипт: функциональное деление на задачи:
  подгружен модуль argpase;
  а) подсчет объема раздела description в файле + поиск названия эксперимента
  б) парсинг .csv и переформатирование с сохранением в .tsv
3. csv_to_tsv_os_long.py - скрипт с оптимизацией и использование синтаксиса bash/zash (UNIX системы)
  подгружены модули: argparse, os, sys
  \_long, так как парсинг файла с использованием bash происходит через создание промежуточного файла и через несколько шагов
4. csv_to_tsv_os_short.py - скрипт с оптимизацией и использованием синтаксиса bash/zash (UNIX системы)
  подгружены модули: argparse, os, sys
  \_short, так как парсинг сокращен до пайплайна в строку
  
 Скрипт запускается из любой директории, но парсит лишь при нахождении в папке с файлом.
 
 Пример запуска:
 ```bash
 python3 csv_to_tsv.py -i file.csv
 ```
 **! По умолчанию -i=single-end-colliding-sample-ids.csv:**
 ```bash
 python3 csv_to_tsv.py -i
 ```
