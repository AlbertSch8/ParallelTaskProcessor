import threading
import queue
import time
import uuid


class Task:
    """Reprezentuje jednu úlohu se vstupním textem."""

    def __init__(self, data: str):
        self.id = str(uuid.uuid4())[:8]
        self.data = data

    def execute(self) -> str:
        """Simulace zpracování – chvilku 'počká' a vrátí text uppercase."""
        time.sleep(1)
        return self.data.upper()


class TaskProcessor:
    """Řídí frontu úloh a worker vlákna (producent–konzument)."""

    def __init__(self, worker_count: int = 3):
        self.task_queue = queue.Queue()
        self.result_log = []          # list of (id, input, output)
        self.lock = threading.Lock()  # na zápis do result_log
        self.workers = []
        self.running = True

        for _ in range(worker_count):
            t = threading.Thread(target=self.worker_loop, daemon=True)
            self.workers.append(t)

    def start(self):
        """Spustí všechna worker vlákna."""
        for w in self.workers:
            w.start()

    def stop(self):
        """Požádá worker vlákna o ukončení a počká na ně."""
        self.running = False
        for w in self.workers:
            w.join()

    def submit(self, text: str) -> str:
        """Vytvoří novou úlohu a vloží ji do fronty."""
        task = Task(text)
        self.task_queue.put(task)
        return task.id

    def worker_loop(self):
        """Hlavní smyčka worker vlákna – bere úlohy z fronty a zpracovává je."""
        while self.running:
            try:
                task = self.task_queue.get(timeout=0.5)
            except queue.Empty:
                continue

            result = task.execute()

            # kritická sekce – zápis do sdíleného logu
            with self.lock:
                self.result_log.append((task.id, task.data, result))

            self.task_queue.task_done()

    def print_results(self):
        """Vytiskne všechny zpracované úlohy."""
        print("\n=== VÝSLEDKY ===")
        if not self.result_log:
            print("Žádné úlohy nebyly zpracovány.")
        for tid, inp, out in self.result_log:
            print(f"[{tid}] '{inp}' -> '{out}'")
        print("================\n")
