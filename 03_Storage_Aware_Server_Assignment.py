import bisect
import hashlib

def stable_hash(value):
    """Use MD5 to ensure consistent hash values across sessions."""
    return int(hashlib.md5(str(value).encode()).hexdigest(), 16)

class ConsistentHashModel:
    def __init__(self):
        self.server_hashes = []  # Sorted list of (hash, server_id)

    def add_server(self, server_id):
        h = stable_hash(server_id)
        bisect.insort(self.server_hashes, (h, server_id))

    def remove_server(self, server_id):
        h = stable_hash(server_id)
        self.server_hashes.remove((h, server_id))

    def get_server(self, key):
        if not self.server_hashes:
            return None
        h = stable_hash(key)
        idx = bisect.bisect_left(self.server_hashes, (h, None))
        if idx == len(self.server_hashes):
            idx = 0
        return self.server_hashes[idx][1]

class ConsistentController:
    def __init__(self, model):
        self.model = model

    def assign(self, video_id):
        return self.model.get_server(video_id)

class ConsistentView:
    def display(self, video_id, server_id):
        print(f"🎥 Video '{video_id}' → 🗄️ Server '{server_id}'")

# Sample usage
if __name__ == "__main__":
    model = ConsistentHashModel()
    controller = ConsistentController(model)
    view = ConsistentView()

    # Adding servers
    for sid in ["Server-A", "Server-B", "Server-C"]:
        model.add_server(sid)

    # Assign videos
    videos = ["vid001", "vid002", "vid003", "vidXYZ", "vidMNO"]
    for vid in videos:
        server = controller.assign(vid)
        view.display(vid, server)

    print("\n🛠️ Removing 'Server-B'...\n")
    model.remove_server("Server-B")

    # Re-assign after removal
    for vid in videos:
        server = controller.assign(vid)
        view.display(vid, server)
