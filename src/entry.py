from typing import List


class Entry:
    buffer: List[str]
    anchors: List[str]
    sort: int
    name: str  # The localized name of this entry
    id: str  # The full name, <category>/<entry>
    rel_id: str  # Just the entry name, <entry>

    def __init__(self):
        self.buffer = []
        self.anchors = []
        self.sort = -1
        self.name = ''
    
    def push(self, text: str):
        self.buffer.append(text)

    def __repr__(self) -> str: return str(self)
    def __str__(self) -> str: return self.name
