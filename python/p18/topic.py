from xmlrpc.server import SimpleXMLRPCServer

topik_data = {}

def terbitkan(nama_topik, event):
    topik_data.setdefault(nama_topik, []).append(event)
    print(f"[TOPIK:{nama_topik}] Masuk: {event}", flush=True)
    return True

def tarik(nama_topik):
    if topik_data.get(nama_topik):
        return topik_data[nama_topik].pop(0)
    return ""

server = SimpleXMLRPCServer(("0.0.0.0", 8000))
server.register_function(terbitkan)
server.register_function(tarik)
print("[TOPIC] Aktif di port 8000...", flush=True)
server.serve_forever()