"""
Add memory to any chatbot in ~20 lines.

Every conversation becomes context for the next one.
No more "I don't know what you mentioned before."

Run:
    pip install logicmem
    export LOGICMEM_API_KEY=lm_your_key_here
    python examples/02_chatbot.py
"""

from logicmem import MemoryClient

client = MemoryClient()

def chat(message: str) -> str:
    """
    Simple chatbot that remembers context from previous conversations.
    
    - Stores each user message with a neutral outcome score (0.5)
    - Retrieves relevant history to build context
    - In production: feed context to your LLM instead of returning it directly
    """
    
    # Store user message with neutral outcome score
    # outcome_score = 0.5 means "neither success nor failure" — just information
    client.store(f"User said: {message}", outcome_score=0.5)
    
    # Retrieve relevant conversation history based on current message
    # This finds memories semantically similar to the current message
    history = client.retrieve(message)
    
    # Build context string for the LLM
    if history:
        context = "\n".join([f"- {h['text']}" for h in history])
        print(f"[Memory retrieved {len(history)} relevant items]")
    else:
        context = "(No relevant history found)"
    
    # In production, you'd pass this context to your LLM
    # For demo purposes, we return a formatted response
    return f"Context from memory:\n{context}\n\nUser: {message}"


# Demo the chatbot
if __name__ == "__main__":
    print("=== Memory-Enabled Chatbot Demo ===\n")
    
    # Simulate a conversation across multiple turns
    responses = [
        chat("I'm looking for project management software"),
        chat("Does it integrate with Slack?"),
        chat("What about pricing?"),
    ]
    
    for i, response in enumerate(responses, 1):
        print(f"\n--- Turn {i} ---")
        print(response)
