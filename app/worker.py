import asyncio
import signal
import sys
from app.background.tasks import process_task_background


class Worker:
    def __init__(self):
        self.running = True

    async def start(self):
        """Start the worker"""
        print("Worker started...")
        
        while self.running:
            # In a real implementation, this would poll a queue (Redis/Celery)
            # For now, just keep the worker alive
            await asyncio.sleep(1)
        
        print("Worker stopped.")

    def stop(self):
        """Stop the worker"""
        self.running = False


def signal_handler(signum, frame):
    print("Received shutdown signal")
    worker.stop()


if __name__ == "__main__":
    worker = Worker()
    
    # Handle shutdown signals
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        asyncio.run(worker.start())
    except KeyboardInterrupt:
        print("Worker interrupted")
    finally:
        sys.exit(0)
