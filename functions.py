import os, sqlite3, streamlit as st, pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from werkzeug.security import generate_password_hash, check_password_hash

# # Função que cria o arquivo de inicialização
# def create_ini(sys_file):
#     # Obtém o caminho da pasta do usuário
#     user_folder = os.path.expanduser("~")

#     # Define o caminho do arquivo dentro da pasta do usuário
#     file_path = os.path.join(user_folder, "robots.ini")

#     # Cria e escreve no arquivo
#     with open(file_path, "w") as f:
#         f.write(sys_file)

# # Função que verifica se o arquivo ini já foi criado
# def get_ini():
#     # Obtém o caminho da pasta do usuário
#     user_folder = os.path.expanduser("~")
#     # Define o caminho do arquivo dentro da pasta do usuário
#     file_path = os.path.join(user_folder, "robots.ini")
#     if os.path.exists(file_path):
#         with open(file_path, 'r') as f:
#             file = f.read()
#         return file

# # Função para pegar o caminho do banco de dados
# def get_saved_path(conn):
#     cursor = conn.cursor()
#     cursor.execute ('SELECT caminho FROM configuracoes LIMIT 1')
#     row = cursor.fetchone()
#     return row[0] if row else None

# # Função para salvar o caminho no banco de dados
# def save_bd_path(conn, caminho):
#     cursor = conn.cursor()
#     cursor.execute('INSERT INTO configuracoes (caminho) VALUES (?)', (caminho,))
#     conn.commit()

# # Função para criação do banco de dados
# def setup_database(path_sys):
#     #if not get_ini():
#     if len(path_sys) == 2:
#         path_sys = os.path.join(path_sys,'\Robts')
#         caminho_relatorio = os.path.join(path_sys,'\Relatorios')
#     if not os.path.exists(path_sys):
#         os.makedirs(path_sys, exist_ok=True)
#         os.makedirs(caminho_relatorio, exist_ok=True)

#     db_path = os.path.join(path_sys,'DataBase')
#     os.makedirs(db_path, exist_ok=True)

#     db_file = os.path.join(db_path,'robts.db')
#     if not os.path.exists(db_file):
#         conn = sqlite3.connect(db_file)
#         cursor = conn.cursor()
#         cursor.execute('''
#                         CREATE TABLE IF NOT EXISTS configuracoes (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         caminho TEXT NOT NULL
#                     )
#                     ''')
#         # Cria tabelas
#         for i in [script for script in os.listdir(os.getcwd()) if '.txt' and 'table' in script]:
#             with open (i, 'r', encoding='utf8') as f:
#                 query = f.read()
#             cursor.execute(query)
#         conn.commit()

#         ret_save_path = get_saved_path(conn)
#         if not ret_save_path:
#             save_bd_path(conn, path_sys)
#         conn.close()
#         create_ini(path_sys)

# Função para criar conexão com o banco
def get_bd_connection():
    path_ini = os.getcwd()
    path_db = os.path.join(path_ini,'DataBase')
    file_db = os.path.join(path_db,'robts.db')
    conn = sqlite3.connect(file_db)
    return conn

# Função para Registrar novo usuário
def registrar_usuario(usuario, senha):
    conn = get_bd_connection()
    cursor = conn.cursor()
    # hash da senha
    senha_hash = generate_password_hash(senha)

    cursor.execute('INSERT INTO usuarios (usuario, senha) VALUES (?, ?)', (usuario, senha_hash))
    conn.commit()
    conn.close()

# Função para Verificar se os dados inseridos são válidos
def verificar_login(usuario, senha):
    conn = get_bd_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT usuario, senha FROM usuarios WHERE usuario = ? LIMIT 1', (usuario,))
    usuario = cursor.fetchone()
    conn.close()
    if usuario and check_password_hash(usuario[1],senha):
        return True
    return False

# Função para Adicionar novos registros
def adicionar_registros(tabela,dados):
    conn = get_bd_connection()
    cursor = conn.cursor()

    if tabela == 'url':
        cursor.execute('INSERT INTO url (url, btn_acesso, usuario, conteudo_usuario, senha, conteudo_senha, btn_login) VALUES (?,?,?,?,?,?,?)', dados)
    elif tabela == 'url_relatorio':
        cursor.execute('INSERT INTO url_relatorio (url, url_relatorio, param01, btn_click01, conteudo01, param02, btn_click02, conteudo02, param03, btn_click03, conteudo03, param04, btn_click04, conteudo04, param05, btn_click05, conteudo05, param06, btn_click06, conteudo06, param07, btn_click07, conteudo07, param08, btn_click08, conteudo08, param09, btn_click09, conteudo09, param10, btn_click10, conteudo10, btn_export) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', dados)

    conn.commit()
    conn.close()

# Função para obter os dados das tabelas
def obter_dados(tabela):
    conn = get_bd_connection()
    df = pd.read_sql(f'SELECT * FROM {tabela}', conn)
    conn.close()
    return df

# Função Editar Usuário
def editar_usuario(id_registro,usuario,senha):
    conn = get_bd_connection()
    cursor = conn.cursor()
    # hash da senha
    senha_hash = generate_password_hash(senha)
    cursor.execute('UPDATE usuarios SET usuario = ?, senha = ? WHERE id = ?',(usuario,senha_hash,id_registro))
    conn.commit()
    conn.close()

# Função para editar o registro
def editar_registro(tabela, id_registro, novos_dados):
    conn = get_bd_connection()
    cursor = conn.cursor()
    if tabela == 'url':
        cursor.execute('UPDATE url SET url = ?, btn_acesso =  ?, usuario = ?, conteudo_usuario = ?, senha = ?, conteudo_senha = ?, btn_login = ? WHERE id = ?', (*novos_dados, id_registro))
    elif tabela == 'url_relatorio':
        cursor.execute('UPDATE url_relatorio SET url = ?, url_relatorio = ?, param01 = ?, btn_click01 = ?, conteudo01 = ?, param02 = ?, btn_click02 = ?, conteudo02 = ?, param03 = ?, btn_click03 = ?, conteudo03 = ?, param04 = ?, btn_click04 = ?, conteudo04 = ?, param05 = ?, btn_click05 = ?, conteudo05 = ?, param06 = ?, btn_click06 = ?, conteudo06 = ?, param07 = ?, btn_click07 = ?, conteudo07 = ?, param08 = ?, btn_click08 = ?, conteudo08 = ?, param09 = ?, btn_click09 = ?, conteudo09 = ?, param10 = ?, btn_click10 = ?, conteudo10 = ?, btn_export = ? where id = ?', (*novos_dados, id_registro))
    elif tabela == 'usuarios':
        cursor.execute('UPDATE usuarios SET usuario = ?, senha = ? WHERE id = ?',(*novos_dados, id_registro))
    conn.commit()
    conn.close()

# Função para apagar registro
def apagar_registro(tabela,id_registro):
    conn = get_bd_connection()
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {tabela} WHERE id = ?',(id_registro,))
    conn.commit()
    conn.close()

# Função para listar todas as URL's existentes
def lista_url():
    conn = get_bd_connection()
    df = pd.read_sql('SELECT url FROM url', conn)
    conn.close
    return df

# Função para listar todos os relatórios cadastrados
def lista_relatorio():
    conn = get_bd_connection()
    df = pd.read_sql('SELECT url FROM url_relatorio', conn)
    conn.close
    return df

# Função para acessar a url
def get_url():
    caminho_download = os.path.join(os.getcwd,'Relatorios')
    # Inicializa o driver do Selenium fora da função
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    # Enganar a detecção de automação
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    prefs = {
        "profile.default_content_settings.popups": 0,
        "download.default_directory": caminho_download,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "profile.content_settings.exceptions.automatic_downloads.*.setting": 1
    }
    chrome_options.add_experimental_option("prefs", prefs)
    #service = Service(caminho_driver)
    return webdriver.Chrome(options=chrome_options)

