"""
Research agent that remembers what it found.

Stop re-searching what you already know.
Check memory first, then research only what you don't have.

Run:
    pip install logicmem
    export LOGICMEM_API_KEY=lm_your_key_here
    python examples/03_research_agent.py
"""

from logicmem import MemoryClient

client = MemoryClient()

def research(topic: str):
    """
    Research agent with persistent memory.
    
    1. Check memory for existing knowledge
    2. If found, skip the expensive research step
    3. If not found, do the research and store it
    
    This pattern saves API calls, reduces latency, and builds
    institutional knowledge over time.
    """
    
    # First: check what we already know about this topic
    # The query doesn't need to match exactly — semantic search handles it
    existing = client.retrieve(f"what do we know about {topic}?")
    
    if existing:
        print(f"📚 Found in memory: {len(existing)} relevant item(s)")
        for item in existing:
            print(f"   → {item['text']}")
        return existing
    
    # No existing knowledge — time to research
    # In production: replace this with actual web search, API calls, etc.
    print(f"🔍 No memory found for '{topic}' — researching...")
    finding = f"Research result for '{topic}': Found that this topic connects to key industry trends."
    
    # Store the finding with HIGH outcome score (1.0 = important, valuable)
    # importance=9 means "this is a key finding, not casual info"
    client.store(f"Found: {finding}", outcome_score=0.95, importance=9)
    
    print(f"✅ Stored for next time")
    return [{"text": finding}]


# Demo the research agent
if __name__ == "__main__":
    print("=== Research Agent with Memory Demo ===\n")
    
    # First search for something — will trigger "research"
    topic = "AI agent frameworks"
    print(f"Researching: {topic}")
    result = research(topic)
    
    print("\n" + "="*50 + "\n")
    
    # Second search for the same thing — should find the memory
    print(f"Researching again: {topic}")
    result = research(topic)
