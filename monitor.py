import sqlite3
import time
from datetime import datetime
from ping3 import ping
import speedtest as speedtest_cli

DB_PATH = "network_logs.db"
PING_INTERVAL = 10             # segundos
SPEEDTEST_INTERVAL = 300       # 5 minutos

# cria tabela
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS logs (
    timestamp TEXT,
    status TEXT,
    latency REAL,
    download REAL,
    upload REAL
)
""")
conn.commit()

last_speedtest = 0

def run_speedtest():
    try:
        st = speedtest_cli.Speedtest()
        st.get_best_server()
        download = st.download() / 1_000_000  # bits → Mbps
        upload = st.upload() / 1_000_000
        return {"download": download, "upload": upload}
    except Exception as e:
        print(f"[ERRO SPEEDTEST] {e}")
        return {"download": None, "upload": None}


while True:
    try:
        latency = ping("8.8.8.8", timeout=2)
        if latency is None:
            status = "offline"
            latency = 0
        else:
            status = "online"
            latency *= 1000  # segundos → ms
    except OSError as e:
        print(f"[ERRO PING] {e}")
        status = "offline"
        latency = 0

    now = time.time()
    download = upload = None

    # roda speedtest a cada 5 minutos, se online
    if status == "online" and (now - last_speedtest) > SPEEDTEST_INTERVAL:
        print("Executando speedtest...")
        result = run_speedtest()
        download, upload = result["download"], result["upload"]
        last_speedtest = now

    c.execute(
        "INSERT INTO logs VALUES (?, ?, ?, ?, ?)",
        (datetime.now().isoformat(), status, latency, download, upload)
    )
    conn.commit()

    print(f"[{datetime.now().strftime('%H:%M:%S')}] {status.upper()} | Latência: {latency:.1f} ms | "
          f"↓ {download if download else '-'} Mbps | ↑ {upload if upload else '-'} Mbps")

    time.sleep(PING_INTERVAL)
