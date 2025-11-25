from multiprocessing import Process, Queue
import uuid


class Task:
    """Reprezentuje jednu úlohu se vstupním textem."""

    def __init__(self, data: str):
        self.id = str(uuid.uuid4())[:8]
        self.data = data

    def execute(self) -> str:
        """
        Skutečné zpracování textu.
        Tady děláme převod na uppercase, ale klidně můžeš později přidat
        třeba počítání znaků, filtrování, atd.
        """
        return self.data.upper()


def worker_loop(task_queue: Queue, result_queue: Queue):
    """
    Funkce běžící v samostatném procesu.
    Odebírá Task z fronty, zpracuje ho a uloží výsledek do result_queue.
    """
    while True:
        task = task_queue.get()  # blokuje, dokud něco nepřijde

        # None = signál pro ukončení procesu
        if task is None:
            break

        result = task.execute()
        result_queue.put((task.id, task.data, result))


class TaskProcessor:
    """
    Spravuje frontu úloh, worker procesy a výsledky.
    Používá multiprocessing → reálná paralelizace.
    """

    def __init__(self, worker_count: int = 3):
        self.task_queue: Queue = Queue()
        self.result_queue: Queue = Queue()
        self.workers: list[Process] = []

        self.results: list[tuple[str, str, str]] = []
        self.submitted_tasks = 0  # kolik úloh bylo zadáno

        for _ in range(worker_count):
            p = Process(
                target=worker_loop,
                args=(self.task_queue, self.result_queue),
                daemon=True,
            )
            self.workers.append(p)

    def start(self):
        """Spustí všechny worker procesy."""
        for p in self.workers:
            p.start()

    def submit(self, text: str) -> str:
        """Vytvoří novou úlohu a vloží ji do fronty."""
        task = Task(text)
        self.task_queue.put(task)
        self.submitted_tasks += 1
        return task.id

    def wait_for_all_results(self):
        """
        Čeká, dokud nejsou zpracované všechny dosud zadané úlohy.
        Výsledky ukládá do self.results.
        """
        while len(self.results) < self.submitted_tasks:
            task_id, inp, out = self.result_queue.get()
            self.results.append((task_id, inp, out))

    def shutdown(self):
        """Pošle všem workerům signál k ukončení a počká na ně."""
        for _ in self.workers:
            self.task_queue.put(None)  # sentinel pro ukončení

        for p in self.workers:
            p.join()

    def print_results(self):
        """Vytiskne všechny zpracované úlohy."""
        print("\n=== VÝSLEDKY ===")
        if not self.results:
            print("Žádné úlohy nebyly zpracovány.")
        else:
            for tid, inp, out in self.results:
                print(f"[{tid}] '{inp}' -> '{out}'")
        print("================\n")
