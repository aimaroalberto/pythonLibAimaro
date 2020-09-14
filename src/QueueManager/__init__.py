import queue
class QueueManager:
    def Queuemanager(self):
        self.queue= queue.Queue(0)
        self.queue.put("one")
        self.queue.get()
