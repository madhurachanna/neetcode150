"""
Time Based Key-Value Store

Implement a time-based key-value data structure that supports:

Storing multiple values for the same key at specified time stamps
Retrieving the key's value at a specified timestamp
Implement the TimeMap class:

TimeMap() Initializes the object.
void set(String key, String value, int timestamp) Stores the key key
with the value value at the given time timestamp.
String get(String key, int timestamp) Returns the most recent value of
key if set was previously called on it and the most recent timestamp
for that key prev_timestamp is less than or equal to the given timestamp
(prev_timestamp <= timestamp). If there are no values, it returns "".

Note: For all calls to set, the timestamps are in strictly increasing order.

Example 1:

Input:
["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1],
"get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

Output:
[null, null, "happy", "happy", null, "sad"]
"""

class TimeMap:

    def __init__(self):
        # {
        #     key: {
        #         sub_key: value,
        #.        sub_key_list: []
        #     }
        # }
        self.time_store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_store:
            self.time_store[key]['sub_key_list'].append(timestamp)
            self.time_store[key][timestamp] = value
        else:
            self.time_store[key] = {}
            self.time_store[key][timestamp] = value
            self.time_store[key]['sub_key_list'] = [timestamp]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.time_store:
            return ""

        arr = self.time_store[key]['sub_key_list']
        t = 0

        # Using binary search, execution speed can be increased further
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > timestamp:
                continue
            t = arr[i]
            break

        return "" if t == 0 else self.time_store[key][t]
