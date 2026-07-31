'''
enantKVStore (HashMap w/ tenants + resizing + removeTenant)

Context (HackerRank / Snowflake-ish):
You’re implementing a simplified in-memory key-value store used by a multi-tenant service. Each customer (tenant) has its own namespace. Keys are ASCII strings; values are integers.

You may not use built-in hash map/dict implementations for the core storage (you can use arrays/lists and your own nodes). You should implement collision handling and resizing.

APIs to implement

Implement a class TenantKVStore with:

put(tenantId: str, key: str, value: int) -> None
get(tenantId: str, key: str) -> Optional[int]
remove(tenantId: str, key: str) -> bool
removeTenant(tenantId: str) -> int
size() -> int
Semantics

put inserts or overwrites the value for (tenantId, key).

get returns the value if present, else None.

remove deletes (tenantId, key) if present and returns True; otherwise returns False.

removeTenant deletes all keys for that tenant and returns the number of deleted entries.

size returns total number of entries across all tenants.

Constraints / Requirements

Up to ~2,000,000 total entries across tenants.

Keys are ASCII strings of length 1..128; tenantId length 1..64.

Expected average time per operation: O(1).

Must support collisions.

Must support resizing (rehash) when load factor exceeds a threshold.

You may assume single-threaded (no concurrency required).

You should avoid direct addressing (keyspace is unbounded strings).

Suggested design choices (you choose one)

Option A (recommended): One global hash table keyed by (tenantId, key) using separate chaining.
Option B: Two-level map (tenant → per-tenant hash map).

If you choose Option A, you’ll likely want a secondary index to make removeTenant efficient.

Follow-ups (be prepared to explain)

What’s your hash function for strings? How do you combine (tenantId, key)?

What triggers resizing and how do you rehash?

What’s your expected and worst-case time?

How would you mitigate adversarial collisions (conceptually)?

Test cases (write your own)

Insert 3 keys under tenant A, 2 under tenant B. Verify size.

Overwrite existing key. Verify size unchanged and value updated.

Remove missing key returns false.

removeTenant(A) deletes only tenant A keys and returns correct count.

Ensure rehash preserves correctness after resizing.
'''

