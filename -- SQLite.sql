-- SQLite
CREATE TABLE usuarios (
id INTEGER PRIMARY KEY AUTOINCREMENT,
usuario TEXT NOT NULL,
senha TEXT NOT NULL
)

-- SQLite
CREATE TABLE url (
id INTEGER PRIMARY KEY AUTOINCREMENT,
url TEXT NOT NULL,
btn_acesso TEXT NULL,
usuario TEXT NOT NULL,
conteudo_usuario TEXT NOT NULL,
senha TEXT NOT NULL,
conteudo_senha TEXT NOT NULL,
btn_login TEXT NOT NULL
)


-- SQLite
CREATE TABLE url_relatorio (
id INTEGER PRIMARY KEY AUTOINCREMENT,
url TEXT NOT NULL,
url_relatorio TEXT NOT NULL,
param01 TEXT NULL,
btn_click01 TEXT NULL,
conteudo01 TEXT NULL,
param02 TEXT NULL,
btn_click02 TEXT NULL,
conteudo02 TEXT NULL,
param03 TEXT NULL,
btn_click03 TEXT NULL,
conteudo03 TEXT NULL,
param04 TEXT NULL,
btn_click04 TEXT NULL,
conteudo04 TEXT NULL,
param05 TEXT NULL,
btn_click05 TEXT NULL,
conteudo05 TEXT NULL,
param06 TEXT NULL,
btn_click06 TEXT NULL,
conteudo06 TEXT NULL,
param07 TEXT NULL,
btn_click07 TEXT NULL,
conteudo07 TEXT NULL,
param08 TEXT NULL,
btn_click08 TEXT NULL,
conteudo08 TEXT NULL,
param09 TEXT NULL,
btn_click09 TEXT NULL,
conteudo09 TEXT NULL,
param10 TEXT NULL,
btn_click10 TEXT NULL,
conteudo10 TEXT NULL,
btn_export TEXT NOT NULL
)