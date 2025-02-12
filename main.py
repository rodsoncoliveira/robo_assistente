import functions as fc, streamlit as st, pandas as pd

# path do sistema
# path_sys = fc.get_ini()
# if path_sys:
#     path_download = path_sys + '\Relatorios'

# Interface do Streamlit

# Fundo Preto
st.markdown(
    """
    <style>
        body {
            background-color: black;
            color: white;
        }
        
        /* Ajusta também os containers do Streamlit */
        .stApp {
            background-color: black;
        }

        /* Estiliza os títulos para melhorar a visibilidade */
        h1, h2, h3, h4, h5, h6, p, label, span {
            color: white !important;
        }

        /* Personaliza botões */
        .stButton>button {
            background-color: #333333;
            color: white;
            border-radius: 8px;
            border: 1px solid white;
        }

        /* Personaliza campos de entrada */
        .stTextInput>div>div>input {
            background-color: #222222;
            color: white;
            border-radius: 5px;
            border: 1px solid white;
        }

        /* Personaliza os selects */
        .stSelectbox>div>div {
            background-color: #222222;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.markdown("<h3 style='text-align: center;'>Sistema de extração de relatórios por Robô</h1>", unsafe_allow_html=True)

with col1:
    st.image("Logo.png", width=100)  # Ajuste o caminho e tamanho conforme necessário

# Adiciona a linha branca separando o cabeçalho do conteúdo
st.markdown("<hr style='border: 1px solid white; margin-top: 10px; margin-bottom: 10px;'>", unsafe_allow_html=True)

#st.title('Sistema de extração de relatórios por Robô')
# se o usuário estiver logado, exibe a área de login
if 'usuario_logado' in st.session_state:
    st.write(f"Seja bem vindo, {st.session_state['usuario_logado']}")
    col3, col4, col5 = st.columns([1,3,1])
    with col3:
        if st.button('Sair'):
            del st.session_state['usuario_logado']
            st.rerun()
    with col4:
        url = st.selectbox('Selecione o Sistema de origem',fc.lista_relatorio())
    with col5:
        if st.button('Executar Robô'): # EXECUTA EXTRAÇÃO DO RELATORIO
            driver = fc.get_url('Relatorios')
            driver.get(url)

    # Adiciona a linha branca separando o cabeçalho do conteúdo
    st.markdown("<hr style='border: 0.5px solid white; margin-top: 10px; margin-bottom: 10px;'>", unsafe_allow_html=True)

    # Criando as colunas
    col1, col2 = st.columns([1,3])

    # Menu Lateral
    with col1: 
        st.subheader('Menu')
        menu_option = st.radio('Escolha uma opção', ['URL do Sistema','Relatórios','Usuários'],index=0)

    # Area principal
    with col2:
        #st.subheader(f'Gerenciamento de {menu_option}')
        st.markdown(f"<p style='font-size:16px; font-weight:bold;'>Gerenciamento de {menu_option}</p>", unsafe_allow_html=True)
        # Opção com seleção de Inserir ou Visualizar
        action = st.radio('Escolha uma ação',['Inserir', 'Visualizar'], index=1, horizontal=True)

        if action == 'Inserir':
            if menu_option == 'Usuários':
                usr_usuarios = st.text_input('Usuário')
                snh_usuarios = st.text_input('Senha', type='password')
                if st.button('Adicionar Usuário'):
                    fc.registrar_usuario(usr_usuarios, snh_usuarios)
                    st.success('Usuário Inserido com Sucesso!')
                    st.rerun()
            elif menu_option == 'Relatórios':
                url_sistema = fc.lista_url()
                url = st.selectbox('Url do Sistema',url_sistema)
                url_rel = st.text_input('URL Do Relatório a ser Extraído')
                btn_export = st.text_input('Caminho XPATH do BOTÃO EXPORTAR')
                param01 = st.text_input('Caminho XPATH do 1º Parâmetro')
                btn_click01 = st.checkbox('É do tipo botão ou seleção?',key=1)
                conteudo01 = st.text_input('Valor para o Parâmetro 01')
                param02 = st.text_input('Caminho XPATH do 2º Parâmetro')
                btn_click02 = st.checkbox('É do tipo botão ou seleção?',key=2)
                conteudo02 = st.text_input('Valor para o Parâmetro 02')
                param03 = st.text_input('Caminho XPATH do 3º Parâmetro')
                btn_click03 = st.checkbox('É do tipo botão ou seleção?',key=3)
                conteudo03 = st.text_input('Valor para o Parâmetro 03')
                param04 = st.text_input('Caminho XPATH do 4º Parâmetro')
                btn_click04 = st.checkbox('É do tipo botão ou seleção?',key=4)
                conteudo04 = st.text_input('Valor para o Parâmetro 04')
                param05 = st.text_input('Caminho XPATH do 5º Parâmetro')
                btn_click05 = st.checkbox('É do tipo botão ou seleção?',key=5)
                conteudo05 = st.text_input('Valor para o Parâmetro 05')
                param06 = st.text_input('Caminho XPATH do 6º Parâmetro')
                btn_click06 = st.checkbox('É do tipo botão ou seleção?',key=6)
                conteudo06 = st.text_input('Valor para o Parâmetro 06')
                param07 = st.text_input('Caminho XPATH do 7º Parâmetro')
                btn_click07 = st.checkbox('É do tipo botão ou seleção?',key=7)
                conteudo07 = st.text_input('Valor para o Parâmetro 07')
                param08 = st.text_input('Caminho XPATH do 8º Parâmetro')
                btn_click08 = st.checkbox('É do tipo botão ou seleção?',key=8)
                conteudo08 = st.text_input('Valor para o Parâmetro 08')
                param09 = st.text_input('Caminho XPATH do 9º Parâmetro')
                btn_click09 = st.checkbox('É do tipo botão ou seleção?',key=9)
                conteudo09 = st.text_input('Valor para o Parâmetro 09')
                param10 = st.text_input('Caminho XPATH do 10º Parâmetro')
                btn_click10 = st.checkbox('É do tipo botão ou seleção?',key=10)
                conteudo10 = st.text_input('Valor para o Parâmetro 10')
                if st.button('Adicionar Relatório'):
                    if url_rel and param01 and btn_export:
                        fc.adicionar_registros('url_relatorio',(url, url_rel, param01, btn_click01, conteudo01, param02, btn_click02, conteudo02, param03, btn_click03, conteudo03, param04, btn_click04, conteudo04, param05, btn_click05, conteudo05, param06, btn_click06, conteudo06, param07, btn_click07, conteudo07, param08, btn_click08, conteudo08, param09, btn_click09, conteudo09, param10, btn_click10, conteudo10, btn_export))
                        st.success('Relatório inserido com sucesso!')
                        st.rerun()
            elif menu_option == 'URL do Sistema':
                url = st.text_input('URL do Sistema WEB')
                btn_acesso = st.text_input('Caminho XPATH do Botão de Acessar Sistema')
                usuario_sistema = st.text_input('Caminho XPATH do Campo USUARIO')
                conteudo_usuario = st.text_input('Usuário')
                senha_sistema = st.text_input('Caminho XPATH do Campo SENHA')
                conteudo_senha = st.text_input('Senha')
                btn_entrar = st.text_input('Caminho XPATH do BOTÃO ACESSAR')
                if st.button('Adicionar URL'):
                    if url and usuario_sistema and senha_sistema and conteudo_usuario and conteudo_senha:
                        fc.adicionar_registros('url',(url, btn_acesso, usuario_sistema, conteudo_usuario, senha_sistema, conteudo_senha, btn_entrar))
                        st.success('URL adicionada com sucesso!')
                        st.rerun()
        elif action == 'Visualizar':
            # Exibir tabela com dados já existentes
            st.markdown(f"<p style='font-size:16px; font-weight:bold;'>Exibindo dados de {menu_option}</p>", unsafe_allow_html=True)
            #st.subheader(f'Exibindo dados de {menu_option}')
            if menu_option == 'Usuários':
                table_name = 'usuarios'
            elif menu_option == 'URL do Sistema':
                table_name = 'url'
            elif menu_option == 'Relatórios':
                table_name = 'url_relatorio'
            df = fc.obter_dados(table_name)
            if not df.empty:
                for index, row in df.iterrows():
                    with st.expander(f"ID: {row['id']} - {row[1]}"):
                        col1, col2, col3 = st.columns([3,1,1])

                        with col1:
                            if menu_option == 'Usuários':
                               usr_edit = st.text_input('Usuário', value=row['usuario'], key=f"usuario_{row['id']}")
                               senha_edit = st.text_input("Senha", value=row["senha"], type="password", key=f"senha_{row['id']}")
                            elif menu_option == 'URL do Sistema':
                                url = st.text_input('URL', value=row['url'], key=f"url_{row['id']}")
                                btn_acesso = st.text_input('Botão de Acesso', value=row['btn_acesso'], key=f"btn_acesso_{row['id']}")
                                usuario_sistema = st.text_input('Caminho XPATH do campo Usuário', value=row['usuario'], key=f"usuario_{row['id']}")
                                conteudo_usuario = st.text_input('Usuário do Sistema', value=row['conteudo_usuario'], key=f"conteudo_usuario_{row['id']}")
                                senha = st.text_input('Caminho XPATH do campo Senha', value=row['senha'], key=f"senha_{row['id']}")
                                conteudo_senha = st.text_input('Senha', value=row['conteudo_senha'], key=f"conteudo_senha_{row['id']}")
                                btn_login = st.text_input('Botão de Login', value=row['btn_login'], key=f"btn_login_{row['id']}")
                            elif menu_option == 'Relatórios':
                                url = st.text_input('URL do Sistema', value=row['url'], key=f"url_{row['id']}")
                                url_rel = st.text_input('URL do Relatório', value=row['url_relatorio'], key=f"url_relatorio_{row['id']}")
                                btn_export = st.text_input('Botão Exportar', value=row['btn_export'], key=f"btn_export_{row['id']}")
                                param01 = st.text_input('Parametro 01', value=row['param01'], key=f"param01_{row['id']}")
                                btn_click01 = st.checkbox('É do Tipo botão ou seleção?',value= True if row['btn_click01'] == '1' else False, key=f"btn_click01_{row['id']}")
                                conteudo01 = st.text_input('Conteúdo Parametro 01', value=row['conteudo01'], key=f"conteudo01_{row['id']}")
                                param02 = st.text_input('Parametro 02', value=row['param02'], key=f"param02_{row['id']}")
                                btn_click02 = st.checkbox('É do Tipo botão ou seleção?',value= True if row['btn_click02'] == '1' else False, key=f"btn_click02_{row['id']}")
                                conteudo02 = st.text_input('Conteúdo Parametro 02', value=row['conteudo02'], key=f"conteudo02_{row['id']}")
                                param03 = st.text_input('Parametro 03', value=row['param03'], key=f"param03_{row['id']}")
                                btn_click03 = st.checkbox('É do Tipo botão ou seleção?',value= True if row['btn_click03'] == '1' else False, key=f"btn_click03_{row['id']}")
                                conteudo03 = st.text_input('Conteúdo Parametro 03', value=row['conteudo03'], key=f"conteudo03_{row['id']}")
                                param04 = st.text_input('Parametro 04', value=row['param04'], key=f"param04_{row['id']}")
                                btn_click04 = st.checkbox('É do Tipo botão ou seleção?',value= True if row['btn_click04'] == '1' else False, key=f"btn_click04_{row['id']}")
                                conteudo04 = st.text_input('Conteúdo Parametro 04', value=row['conteudo04'], key=f"conteudo04_{row['id']}")
                                param05 = st.text_input('Parametro 05', value=row['param05'], key=f"param05_{row['id']}")
                                btn_click05 = st.checkbox('É do Tipo botão ou seleção?',value= True if row['btn_click05'] == '1' else False, key=f"btn_click05_{row['id']}")
                                conteudo05 = st.text_input('Conteúdo Parametro 05', value=row['conteudo05'], key=f"conteudo05_{row['id']}")
                                param06 = st.text_input('Parametro 06', value=row['param06'], key=f"param06_{row['id']}")
                                btn_click06 = st.checkbox('É do Tipo botão ou seleção?',value= True if row['btn_click06'] == '1' else False, key=f"btn_click06_{row['id']}")
                                conteudo06 = st.text_input('Conteúdo Parametro 06', value=row['conteudo06'], key=f"conteudo06_{row['id']}")
                                param07 = st.text_input('Parametro 07', value=row['param07'], key=f"param07_{row['id']}")
                                btn_click07 = st.checkbox('É do Tipo botão ou seleção?',value= True if row['btn_click07'] == '1' else False, key=f"btn_click07_{row['id']}")
                                conteudo07 = st.text_input('Conteúdo Parametro 07', value=row['conteudo07'], key=f"conteudo07_{row['id']}")
                                param08 = st.text_input('Parametro 08', value=row['param08'], key=f"param08_{row['id']}")
                                btn_click08 = st.checkbox('É do Tipo botão ou seleção?',value= True if row['btn_click08'] == '1' else False, key=f"btn_click08_{row['id']}")
                                conteudo08 = st.text_input('Conteúdo Parametro 08', value=row['conteudo08'], key=f"conteudo08_{row['id']}")
                                param09 = st.text_input('Parametro 09', value=row['param09'], key=f"param09_{row['id']}")
                                btn_click09 = st.checkbox('É do Tipo botão ou seleção?',value= True if row['btn_click09'] == '1' else False, key=f"btn_click09_{row['id']}")
                                conteudo09 = st.text_input('Conteúdo Parametro 09', value=row['conteudo09'], key=f"conteudo09_{row['id']}")
                                param10 = st.text_input('Parametro 10', value=row['param10'], key=f"param10_{row['id']}")
                                btn_click10 = st.checkbox('É do Tipo botão ou seleção?',value= True if row['btn_click10'] == '1' else False, key=f"btn_click10_{row['id']}")
                                conteudo10 = st.text_input('Conteúdo Parametro 10', value=row['conteudo10'], key=f"conteudo10_{row['id']}")
                        with col2:
                            if st.button('Editar', key=f"edit_{row['id']}"):
                                if menu_option == 'Usuários':
                                    fc.editar_usuario(row['id'],usr_edit,senha_edit)
                                    #fc.editar_registro('usuarios',row['id'], (usr_edit, senha_edit))
                                elif menu_option == 'URL do Sistema':
                                    fc.editar_registro('url',row['id'],(url, btn_acesso, usuario_sistema, conteudo_usuario, senha, conteudo_senha, btn_login))
                                elif menu_option == 'Relatórios':
                                    fc.editar_registro('url_relatorio',row['id'],(url, url_rel, param01, btn_click01, conteudo01, param02, btn_click02, conteudo02, param03, btn_click03, conteudo03, param04, btn_click04, conteudo04, param05, btn_click05, conteudo05, param06, btn_click06, conteudo06, param07, btn_click07, conteudo07, param08, btn_click08, conteudo08, param09, btn_click09, conteudo09, param10, btn_click10, conteudo10, btn_export))
                                st.success('Registro Atualizado com Sucesso!')
                                st.rerun()
                        with col3:
                            if st.button('Excluir',key=f"delete_{row['id']}"):
                                if menu_option == 'Usuários':
                                    fc.apagar_registro('usuarios',row['id'])
                                if menu_option == 'URL do Sistema':
                                    fc.apagar_registro('url',row['id'])
                                if menu_option == 'Relatórios':
                                    fc.apagar_registro('url_relatorio',row['id'])
                                st.success('Registro apagado com sucesso.')
                                st.rerun()
            else:
                st.write('Nenhum dado encontrado.')




        
        # Formulário



else:
    menu = st.selectbox('Escolha uma opção:', ['Login','Registrar'])
    if menu == 'Login':
        usuario = st.text_input('Usuário')
        senha = st.text_input('Senha', type='password')
        if st.button('Entrar'):
            if fc.verificar_login(usuario,senha):
                st.session_state['usuario_logado'] = usuario
                st.rerun()
            else:
                st.error('Credenciais Inválidas!!')
    elif menu == 'Registrar':
        usuario = st.text_input('Usuário')
        senha = st.text_input('Senha', type='password')
        confirmar_senha = st.text_input('Confirmar Senha', type='password')
        if st.button('Registrar'):
            if senha == confirmar_senha:
                fc.registrar_usuario(usuario,senha)
                st.success('Usuário Registrado com Sucesso!!')
            else:
                st.error('As informações de senha não correspondem!')
    # else:
    #     st.text('Registro de Usuário')
    #     usuario = st.text_input('Usuário')
    #     senha = st.text_input('Senha', type='password')
    #     confirmar_senha = st.text_input('Confirmar Senha', type='password')
    #     if st.button('Registrar'):
    #         if senha == confirmar_senha:
    #             fc.registrar_usuario(usuario,senha)
    #             st.success('Usuário Carregados com Sucesso!!')
    #             st.rerun()
    #         else:
    #             st.error('As informações de senha não correspondem!')
