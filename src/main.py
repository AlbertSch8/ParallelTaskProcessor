from task_processor import TaskProcessor


def main():
    processor = TaskProcessor(worker_count=3)
    processor.start()

    print("=== Parallel Task Processor ===")
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
    processor.task_queue.join()

    processor.stop()
    processor.print_results()
    print("Hotovo. Ukončuji program.")


if __name__ == "__main__":
    main()
