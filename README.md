# Parallel Task Processor

Konzolová Python aplikace, která zpracovává textové úlohy **paralelně pomocí multiprocessing**.
Jde o skutečnou paralelizaci, protože každý worker běží jako samostatný proces.

## 1. Autor
- **Albert Schurrer**
- **SPŠE Ječná**
- **albert.schurrer@gmail.com**

## 2. Popis aplikace
Uživatel zadává textové úlohy v konzoli.  
Každá úloha se vloží do `multiprocessing.Queue` a několik worker procesů ji paralelně zpracovává (např. převod textu na uppercase).  
Výsledky se vrací zpět přes druhou frontu a po příkazu `exit` se vše vypíše.

Projekt demonstruje:
- reálnou paralelizaci (multiprocessing),
- model producent–konzument,
- komunikaci procesů přes sdílené fronty,
- bezpečné ukončení worker procesů.

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
1. Kliknout pravým na `src/` → **Mark Directory as → Sources Root**
2. Spustit `main.py`

## 5. Princip
- Hlavní proces = producent  
- Worker procesy = konzumenti  
- Úlohy → fronta → paralelní zpracování → výsledky  

## 6. Možnosti rozšíření
- další typy textových úloh,
- ukládání výsledků do souboru,
- priority úloh,
- webové API.