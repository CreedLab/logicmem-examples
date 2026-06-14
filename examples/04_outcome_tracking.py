"""
Track what actually worked — the DPO (Direct Preference Optimization) pattern.

Store decisions/actions with outcome scores. When you retrieve later,
the successful outcomes get boosted automatically.

This is how AI agents learn from experience without retraining.

Run:
    pip install logicmem
    export LOGICMEM_API_KEY=lm_your_key_here
    python examples/04_outcome_tracking.py
"""

from logicmem import MemoryClient

client = MemoryClient()

def track_sales_outcome(sales_action: str, outcome: str, outcome_score: float):
    """
    Store a sales action and its outcome.
    
    outcome_score: 0.0 = complete failure, 1.0 = perfect success
    
    The magic: when you retrieve similar contexts later,
    the successful patterns bubble up automatically.
    """
    client.store(f"Action: {sales_action} | Outcome: {outcome}", outcome_score=outcome_score)
    print(f"📝 Stored: '{sales_action}' → outcome_score={outcome_score}")


def get_recommended_action(query: str) -> str:
    """
    Retrieve the best-performing action for a given context.
    
    Returns the action with the highest weighted score,
    considering both semantic relevance AND outcome history.
    """
    results = client.retrieve(query)
    
    if not results:
        return "No historical data — use your best judgment"
    
    best = results[0]
    print(f"🎯 Best match: {best['text']}")
    print(f"   Relevance: {best['score']:.2f}, Outcome: {best.get('outcome_score', 'N/A')}")
    
    return best["text"]


# Demo the DPO pattern
if __name__ == "__main__":
    print("=== DPO Pattern: Learning from Outcomes ===\n")
    
    # --- Scenario: Enterprise sales pitch ---
    
    # Test 1: Monthly plan suggestion (failed)
    track_sales_outcome(
        sales_action="Suggested monthly plan to enterprise client",
        outcome="Client said too expensive, left",
        outcome_score=0.0
    )
    
    # Test 2: Annual plan with discount (succeeded)
    track_sales_outcome(
        sales_action="Suggested annual plan with 20% discount to enterprise client",
        outcome="Client accepted, signed 1-year deal",
        outcome_score=1.0
    )
    
    # Test 3: Premium tier with ROI analysis (succeeded)
    track_sales_outcome(
        sales_action="Presented premium tier with ROI calculator",
        outcome="Enterprise client upgraded to premium",
        outcome_score=0.95
    )
    
    print("\n" + "="*50 + "\n")
    
    # Now ask: what should we suggest to enterprise clients?
    print("Query: what should we suggest to enterprise clients?")
    recommendation = get_recommended_action("what should we suggest to enterprise clients?")
    
    print("\n" + "="*50 + "\n")
    print("📊 What the system learned:")
    print("   Monthly plan = bad (0.0)")
    print("   Annual + discount = good (1.0)")
    print("   Premium + ROI = good (0.95)")
    print("\n   → Retrieval surfaces the SUCCESSFUL patterns first")
