import dramatiq
from dramatiq.brokers.stub import StubBroker
from dramatiq import Worker

# Create a stub broker (in-memory)
broker = StubBroker()

# Set the broker for the default dramatiq instance
dramatiq.set_broker(broker)

# Create a worker
worker = Worker()

# Register your task
worker.register(scrape_instagram_following_profile)

# Start the worker
worker.start()
