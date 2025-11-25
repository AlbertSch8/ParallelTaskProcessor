# Parallel Task Processor

Jednoduchá konzolová Python aplikace, která zpracovává textové úlohy paralelně pomocí více vláken (model producent–konzument).

## 1. Autor
- **Albert Schurrer**
- **SPŠE Ječná**
- **albert.schurrer@gmail.com**

## 2. Popis aplikace
Uživatel zadává text, který se uloží jako úloha do thread-safe fronty.  
Několik worker vláken úlohy paralelně zpracovává (uppercase).  
Po příkazu `exit` aplikace počká na dokončení a vypíše výsledky.

## 3. Struktura projektu
src/
main.py
task_processor.py
doc/
DOKUMENTACE.pdf
README.md

shell
Zkopírovat kód

## 4. Spuštění
### Terminál:
python -m src.main

markdown
Zkopírovat kód

### PyCharm:
1. Označit `src/` jako **Sources Root**
2. Spustit `main.py`

## 5. Princip
- Hlavní vlákno = producent  
- Workeři = konzumenti  
- Úlohy → fronta → parallel processing → log výsledků  

## 6. Možnosti rozšíření
- více typů úloh  
- ukládání výsledků do souboru  
- statistiky a měření času  