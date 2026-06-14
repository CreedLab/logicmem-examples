"""
The 5-line memory-enabled AI agent.

This is the simplest possible example of adding memory to an AI agent.
Store a decision, retrieve it later — that's the whole thing.

Run:
    pip install logicmem
    export LOGICMEM_API_KEY=lm_your_key_here
    python examples/01_quickstart.py
"""

from logicmem import MemoryClient

# Initialize — reads LOGICMEM_API_KEY from environment
client = MemoryClient()

# Store something important with an outcome score (0.0 = failed, 1.0 = succeeded)
# Higher outcome_score = more likely to be retrieved in similar future contexts
client.store("decided to use Stripe for payments", outcome_score=0.9)

# Retrieve relevant memories using natural language query
# The retrieval is semantic — "Stripe" matches even though you didn't say "Stripe" in the query
results = client.retrieve("what did we decide about payments?")

# Print the best match
print(results[0]["text"])  # → "decided to use Stripe for payments"

# Each result includes a 'score' field showing relevance (0.0 to 1.0)
print(f"Confidence: {results[0]['score']:.2f}")
