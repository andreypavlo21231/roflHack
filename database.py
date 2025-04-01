import os

class TextDatabase:
    def __init__(self, filepath):
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            self._save("")
    
    def _load(self):
        with open(self.filepath, "r", encoding="utf-8") as file:
            return file.read()

    def _save(self, data):
        with open(self.filepath, "w", encoding="utf-8") as file:
            file.write(data)

    def insert(self, key, value):
        data = self._load()
        lines = data.split("\n") if data else []
        lines.append(f"{key}:{value}")
        self._save("\n".join(lines))

    def get(self, key):
        data = self._load()
        for line in data.split("\n"):
            # print(key,line)
            if line.startswith(f"{key}:"):
                return line.split(f"{key}:", 1)[1]
        return None

    def update(self, key, value):
        data = self._load()
        lines = data.split("\n")
        for i, line in enumerate(lines):
            if line.startswith(f"{key}:"):
                lines[i] = f"{key}:{value}"
                self._save("\n".join(lines))
                return
        raise KeyError(f"Ключ '{key}' не найден!")

    def delete(self, key):
        data = self._load()
        lines = [line for line in data.split("\n") if not line.startswith(f"{key}:")]
        self._save("\n".join(lines))

    def all(self):
        return self._load()


# db.insert("user1", "name=Иван, age=30")
# db.insert("user2", "name=Анна, age=25")
# print(db.get("user1"))
# db.update("user1", "name=Иван, age=31")
# db.delete("user2")
# print(db.all())