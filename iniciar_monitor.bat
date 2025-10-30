@echo off
REM ===========================================================
REM  Script para iniciar o Monitor de Rede e o Dashboard
REM ===========================================================

REM Caminho do projeto
cd /d "C:\meu_projeto_monitor"

REM Ativar o ambiente virtual (ajuste o nome se for diferente)
call venv\Scripts\activate

REM Exibir status
echo =======================================
echo  Iniciando monitor de rede...
echo =======================================

REM Abrir o monitor de rede (em segundo plano)
start cmd /k "python monitor.py"

REM Esperar 5 segundos antes de iniciar o dashboard
timeout /t 5 /nobreak >nul

REM Iniciar dashboard (por exemplo, Flask ou Streamlit)
echo =======================================
echo  Iniciando dashboard...
echo =======================================

REM Caso use Flask
python -m streamlit run dashboard.py


REM Caso use Streamlit (descomente se for o caso)
REM start cmd /k "streamlit run dashboard.py"

REM Mostrar mensagem final
echo.
echo ================================
echo Monitor e Dashboard iniciados!
echo ================================
pause
