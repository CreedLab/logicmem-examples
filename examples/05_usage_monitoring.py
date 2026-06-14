"""
Monitor your usage and upgrade when ready.

Keep users informed about their operation counts.
Show upgrade prompts at the right moment (80% threshold).

Run:
    pip install logicmem
    export LOGICMEM_API_KEY=lm_your_key_here
    python examples/05_usage_monitoring.py
"""

from logicmem import MemoryClient

client = MemoryClient()

def check_usage_and_warn():
    """
    Check current usage and alert if approaching limit.
    
    Returns a dict with:
    - used: operations used this period
    - limit: total operations allowed
    - pct: percentage used (as int)
    - reset_date: when the period resets
    """
    usage = client.usage()
    
    print(f"📊 Usage: {usage['used']}/{usage['limit']} operations")
    print(f"   Period: {usage.get('period', 'monthly')}")
    print(f"   {usage['pct']}% used")
    
    if usage["reset_date"]:
        print(f"   Resets: {usage['reset_date']}")
    
    # Alert thresholds
    if usage["pct"] >= 90:
        print("\n🚨 CRITICAL: 90%+ usage — upgrade immediately!")
        print(f"   → https://logicmem.io/pricing")
        return "critical"
    elif usage["pct"] >= 80:
        print("\n⚠️  WARNING: 80%+ usage — consider upgrading soon")
        print(f"   → https://logicmem.io/pricing")
        return "warning"
    elif usage["pct"] >= 50:
        print("\n💡 Notice: 50%+ usage — plan ahead")
        return "notice"
    else:
        print("\n✅ Healthy usage — you're good")
        return "healthy"


def embed_warning(embed_threshold: int = 800):
    """
    Embed a usage warning in your agent's response.
    
    Call this before any client-facing operation to ensure
    they know where they stand.
    """
    usage = client.usage()
    
    if usage["used"] > embed_threshold:
        return (
            f" Heads up: You've used {usage['used']}/{usage['limit']} "
            f"operations this month ({usage['pct']}%). "
            f"Upgrade at https://logicmem.io/pricing"
        )
    return ""


# Demo the usage monitoring
if __name__ == "__main__":
    print("=== Usage Monitoring Demo ===\n")
    
    status = check_usage_and_warn()
    
    print("\n" + "="*50 + "\n")
    
    # Show the embedded warning format
    print("Embedded warning example:")
    warning = embed_warning(embed_threshold=800)
    if warning:
        print(f"   [Agent says]: '{warning}'")
    else:
        print("   (No warning needed at current usage)")
    
    print("\n" + "="*50 + "\n")
    print("💡 In production: call check_usage_and_warn() at session start,")
    print("   or embed_warning() before expensive operations.")
