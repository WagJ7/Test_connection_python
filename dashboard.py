import streamlit as st
import pandas as pd
import sqlite3
import time

DB_PATH = "network_logs.db"

st.set_page_config(page_title="Monitor de Conexão", layout="wide", page_icon="📡")
st.title("📡 Monitor de Conexão de Rede")

def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM logs ORDER BY timestamp DESC LIMIT 1000", conn)
    conn.close()
    if df.empty:
        return pd.DataFrame(columns=["timestamp", "status", "latency", "download", "upload"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")
    return df

df = load_data()

if not df.empty:
    current = df.iloc[-1]
    status = "🟢 Online" if current["status"] == "online" else "🔴 Offline"
    latency = f"{current['latency']:.2f} ms" if current["status"] == "online" else "N/A"
    last_update = current["timestamp"].strftime("%d/%m/%Y %H:%M:%S")
    uptime = df["status"].value_counts(normalize=True).get("online", 0) * 100
else:
    status, latency, uptime, last_update = "Sem dados", "N/A", 0, "—"

col1, col2, col3, col4 = st.columns(4)
col1.metric("Status Atual", status)
col2.metric("Latência", latency)
col3.metric("Uptime", f"{uptime:.1f}%")
col4.metric("Última Atualização", last_update)

st.divider()

if not df.empty:
    # mantém última velocidade até próxima medição (evita picos 0)
    df["download"] = df["download"].fillna(method="ffill")
    df["upload"] = df["upload"].fillna(method="ffill")

    recent = df.dropna(subset=["download", "upload"]).tail(5)
    avg_down = recent["download"].mean() if not recent.empty else 0
    avg_up = recent["upload"].mean() if not recent.empty else 0

    st.subheader("🚀 Velocidade de Conexão (média dos últimos testes)")
    c1, c2 = st.columns(2)
    c1.metric("Download Médio", f"{avg_down:.2f} Mbps")
    c2.metric("Upload Médio", f"{avg_up:.2f} Mbps")

    st.divider()
    st.subheader("📈 Histórico de Latência")
    st.line_chart(df.set_index("timestamp")["latency"])

    st.subheader("📡 Histórico de Velocidade")
    st.line_chart(df.set_index("timestamp")[["download", "upload"]])

    st.divider()
    st.subheader("📜 Logs Recentes")
    st.dataframe(
        df.tail(30).sort_values("timestamp", ascending=False),
        use_container_width=True,
        hide_index=True,
    )
else:
    st.info("Nenhum dado disponível ainda. Aguarde o monitor coletar informações.")

st.caption("🔄 Atualiza automaticamente a cada 10 segundos.")
time.sleep(10)
st.rerun()
