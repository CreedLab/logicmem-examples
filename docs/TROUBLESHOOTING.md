# Troubleshooting

Common issues and how to fix them.

## "Connection refused" on localhost:8423

**Cause:** LogicMem Open server isn't running.

**Fix:**
```bash
docker compose ps      # Check status
docker compose logs    # See error output
docker compose up -d   # Restart
```

## "Invalid API key" error

**Cause:** Wrong or missing API key.

**Fix:**
1. Get your key from [logicmem.io](https://logicmem.io)
2. Set it as environment variable:
   ```bash
   export LOGICMEM_API_KEY="your-key-here"
   ```
3. Or pass directly:
   ```python
   client = LogicMem(api_key="your-key-here")
   ```

## Memory not persisting between sessions

**Cause:** Not calling `session()` to load context.

**Fix:** At the start of each session:
```python
client = LogicMem(api_key="your-key")
context = client.session(client_id="user-123")
# Now use context['memories'] in your agent
```

## Rate limit errors (429)

**Cause:** Exceeded your plan's request limit.

**Fix:**
- Free tier: 1,000 ops/month
- Upgrade at [logicmem.io/pricing](https://logicmem.io/pricing)
- Or implement request batching to reduce calls

## "Recall returns empty" even with matching data

**Cause:** Query uses different wording than stored text.

**Fix:**
- Use more specific queries
- Check the exact wording in your `log()` calls
- Use the `tags` parameter for structured recall

## Docker: Port 8423 already in use

**Fix:**
```bash
# Find what's using the port
lsof -i :8423

# Kill it or change the port in docker-compose.yml
```

## Import errors after pip install

**Cause:** Package installed in wrong Python environment.

**Fix:**
```bash
pip install --upgrade logicmem
python3 -c "from logicmem import LogicMem; print('OK')"
```
