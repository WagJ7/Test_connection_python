# 📡 Network Monitor

Um sistema simples e eficiente para **monitoramento de conexão de rede** com histórico de latência, velocidade (download/upload) e status em tempo real, desenvolvido com **Python + Streamlit**.

---

## 🚀 Funcionalidades

- 🟢 **Monitoramento contínuo** da conexão (online/offline)  
- ⚡ **Medição de latência (ping)** em intervalos automáticos  
- 🚀 **Teste de velocidade** (download e upload) com histórico  
- 📊 **Dashboard em tempo real** via Streamlit  
- 💾 **Armazenamento local em SQLite**  
- 🔄 Atualização automática a cada 10 segundos  
- 🧠 Detecção de falhas na rede e tratamento automático de erros  

---

## 🧰 Tecnologias Utilizadas

- [Python 3.12+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Ping3](https://pypi.org/project/ping3/)
- [Speedtest-cli](https://pypi.org/project/speedtest-cli/)
- [SQLite3](https://www.sqlite.org/)
- [Pandas](https://pandas.pydata.org/)

---

## ⚙️ Instalação

1. **Clone o repositório**

   ```bash
   git clone https://github.com/seuusuario/network-monitor.git
   cd network-monitor
Crie e ative o ambiente virtual

bash
Copiar código
python -m venv .venv
.venv\Scripts\activate   # no Windows
# ou
source .venv/bin/activate  # no Linux/Mac
Instale as dependências

bash
Copiar código
pip install -r requirements.txt
▶️ Execução
Inicie o dashboard com:

bash
Copiar código
python -m streamlit run dashboard.py
Ou, se preferir, crie um arquivo iniciar.bat (para Windows):

bat
Copiar código
@echo off
cd /d "C:\caminho\para\seu\projeto"
python -m streamlit run dashboard.py
pause
Depois basta clicar duas vezes no arquivo .bat para iniciar o monitor.

🗄️ Estrutura do Projeto
bash
Copiar código
📁 network-monitor/
│
├── dashboard.py           # Dashboard principal (interface Streamlit)
├── monitor.py             # Script de monitoramento e gravação no banco
├── network_logs.db        # Banco de dados SQLite (gerado automaticamente)
├── requirements.txt       # Dependências do projeto
├── iniciar.bat            # Script opcional para execução automática
└── README.md              # Documentação
🧩 Banco de Dados (SQLite)
Os logs são armazenados localmente em network_logs.db, com os seguintes campos:

Campo	Descrição
timestamp	Data e hora do registro
status	online/offline
latency	Latência (ms)
download	Velocidade de download (Mbps)
upload	Velocidade de upload (Mbps)

📊 Exemplo de Dashboard
O painel mostra em tempo real:

Status atual da conexão

Latência média e uptime

Gráficos de histórico de latência e velocidade

Últimos registros de conexão

⚠️ Observações
Caso apareça o erro OSError: [WinError 10051], ele indica que a rede está temporariamente inacessível (o app continuará tentando novamente).

O banco é atualizado automaticamente, não é necessário reiniciar o dashboard.


Desenvolvido com 💀 por Wagner Silvestre!

