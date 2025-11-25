from task_processor import TaskProcessor


def main():
    processor = TaskProcessor(worker_count=3)
    processor.start()

    print("=== Parallel Task Processor (multiprocessing) ===")
    print("Zadávej texty k paralelnímu zpracování.")
    print("Napiš 'exit' pro ukončení.\n")

    try:
        while True:
            text = input(">> ")

            if text.strip().lower() == "exit":
                break

            if not text.strip():
                continue

            task_id = processor.submit(text)
            print(f"Úloha #{task_id} byla přidána do fronty.\n")

    except KeyboardInterrupt:
        print("\nPřerušeno uživatelem (Ctrl+C).")

    print("Čekám na dokončení všech úloh...")

    # počkáme, než se zpracují všechny dosud zadané úlohy
    processor.wait_for_all_results()

    # korektně ukončíme worker procesy
    processor.shutdown()

    # vypíšeme výsledky
    processor.print_results()
    print("Hotovo. Ukončuji program.")


if __name__ == "__main__":
    # kvůli multiprocessing na Windows tohle MUSÍ být
    main()
