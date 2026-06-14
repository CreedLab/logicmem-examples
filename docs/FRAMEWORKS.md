# Framework Integrations

Connect LogicMem to your favorite AI framework in minutes.

## LangChain

```python
from langchain.memory import ConversationBufferMemory
from logicmem import LogicMem

# Swap LangChain's in-memory buffer for LogicMem
memory = LogicMem(api_key="your-key", client_id="user-123")

# In your chain:
memory.log("User asked about pricing", category="interaction")
context = memory.recall("pricing", limit=5)
```

## AutoGPT

```python
from logicmem import LogicMem

memory = LogicMem(api_key="your-key", client_id="autogpt-agent")

# At start of each goal:
context = memory.session(client_id="autogpt-agent")

# After each action:
memory.log(f"Completed: {action}", category="goal_progress")
```

## CrewAI

```python
from logicmem import LogicMem

memory = LogicMem(api_key="your-key")

# In your crew's task executor:
def execute_task(task, agent_id):
    memory.log(f"Agent {agent_id} executing: {task.description}")
    result = agent.execute(task)
    memory.log(f"Agent {agent_id} completed: {result}", category="task_result")
    return result
```

## n8n

Use the HTTP Request node with LogicMem's REST API:

```
POST https://api.logicmem.io/memory/log
Headers:
  Authorization: Bearer YOUR_API_KEY
  Content-Type: application/json
Body:
{
  "text": "Invoice #1234 paid by Acme Corp",
  "category": "payment",
  "client_id": "acme-corp"
}
```

## Voice Agents (VAPI, Retell AI, Bland AI)

```python
from logicmem import LogicMem

memory = LogicMem(api_key="your-key")

def on_voice_call_start(call_id: str, user_id: str):
    session = memory.session(client_id=user_id)
    return session  # Agent knows who this is + history

def on_voice_message(user_id: str, transcript: str):
    memory.log(transcript, category="voice_call", tags=["voice"])
```

## Custom Agent

```python
from logicmem import LogicMem

class MyAgent:
    def __init__(self, api_key: str):
        self.memory = LogicMem(api_key=api_key)
    
    def think(self, prompt: str, client_id: str):
        # Get relevant context
        context = self.memory.recall(prompt, client_id=client_id)
        
        # Reason about the response
        reasoning = self.memory.reason(
            question=prompt,
            context=context
        )
        
        return reasoning["answer"]
    
    def learn(self, text: str, client_id: str):
        self.memory.log(text, client_id=client_id)
```
