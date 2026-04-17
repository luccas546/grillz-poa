import streamlit as st
import base64
import os

# --- 1. CONFIGURAÇÃO DE ALTO NÍVEL ---
st.set_page_config(
    page_title="Jóias Dentais | Grillz & Piercing Porto Alegre",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. MOTOR DE IMAGENS (BASE64) ---
def get_base64_image(image_path):
    """Converte imagens locais para exibição segura no Streamlit"""
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# Carregamento dos Ativos
foto1_b64 = get_base64_image("paciente1 (1).jpeg")
foto2_b64 = get_base64_image("paciente1 (2).jpeg")
foto3_b64 = get_base64_image("paciente1 (3).jpeg")
fundo1_b64 = get_base64_image("imagemfundogrillz1.jpg")
fundo2_b64 = get_base64_image("imagemfundogrillz2.jpg")

# --- 3. CSS CUSTOMIZADO (LÓGICA ALPHA BLINDADA) ---
st.markdown(f"""
    <style>
    /* FUNDO BASE */
    .stApp {{
        background-color: #000000;
        color: #E0E0E0;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }}

    /* LÓGICA DESKTOP (PC) */
    @media (min-width: 1024px) {{
        .stApp {{
            background-image: 
                radial-gradient(circle, rgba(0,0,0,0) 0%, rgba(0,0,0,0.8) 70%, rgba(0,0,0,1) 100%),
                linear-gradient(180deg, rgba(0, 0, 0, 0.6) 0%, rgba(0, 0, 0, 0.9) 100%),
                url("data:image/jpeg;base64,{fundo1_b64}"),
                url("data:image/jpeg;base64,{fundo2_b64}");
            background-position: center top, center, top left, bottom right;
            background-repeat: no-repeat;
            background-size: cover, cover, auto, auto;
            background-attachment: fixed;
        }}
    }}

    /* LÓGICA MOBILE (CELULAR) */
    @media (max-width: 1023px) {{
        .stApp {{
            background-image: 
                linear-gradient(180deg, 
                    rgba(0,0,0,0.9) 0%, 
                    rgba(0,0,0,0) 15%, 
                    rgba(0,0,0,0) 35%, 
                    rgba(0,0,0,1) 50%, 
                    rgba(0,0,0,1) 60%, 
                    rgba(0,0,0,0) 80%, 
                    rgba(0,0,0,0.9) 100%),
                url("data:image/jpeg;base64,{fundo1_b64}"),
                url("data:image/jpeg;base64,{fundo2_b64}");
            background-position: center, top center, bottom center;
            background-repeat: no-repeat;
            background-size: 100% 100%, 100% auto, 100% auto;
            background-attachment: scroll, fixed, scroll;
        }}
    }}

    /* CONTAINER PRINCIPAL RESPONSIVO */
    .block-container {{
        padding: 2rem 1rem !important;
        max-width: 800px;
    }}

    /* TÍTULOS DE SEÇÃO (DOURADO VIBRANTE) */
    h1, h2, h3, h4 {{
        color: #D4AF37 !important;
        font-weight: 900 !important;
        text-shadow: 4px 4px 8px rgba(0,0,0,0.9);
        text-transform: uppercase;
        letter-spacing: 2px;
    }}
    
    h1 {{ font-size: clamp(2rem, 8vw, 3.5rem) !important; margin-bottom: 0.5rem; text-align: center; }}
    h3 {{ text-align: center; margin-top: 2rem !important; }}

    /* RÓTULOS DOS CAMPOS (DOURADO SUAVE) */
    label, [data-testid="stWidgetLabel"] p {{
        color: #B8860B !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 0.85rem !important;
    }}

    /* CORREÇÃO DE ALINHAMENTO DO BLOCO DE PREÇO */
    div[data-testid="stVerticalBlock"] > div:has(div.stAlert) {{
        margin-top: 28px !important;
    }}

    /* FORÇAR COR DO TEXTO NOS INPUTS */
    input, textarea {{
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }}

    /* ESTILO DOS BLOCOS DE ENTRADA */
    div[data-baseweb="select"] > div, 
    div[data-baseweb="base-input"] > input,
    div[data-baseweb="input"] > input,
    div[data-basWeb="textarea"] > textarea {{
        background-color: rgba(30, 30, 30, 0.95) !important;
        border: 1px solid #D4AF37 !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
    }}

    /* TEXTO DENTRO DO SELECTBOX */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] {{
        color: #FFFFFF !important;
    }}
    
    /* MENU DE OPÇÕES (DROP DOWN) */
    div[role="listbox"] ul {{
        background-color: #003366 !important;
    }}

    div[role="listbox"] li {{
        color: #FFFFFF !important;
    }}

    div[role="listbox"] li:hover {{
        background-color: #0055AA !important;
    }}

    /* BOTÃO WHATSAPP ALPHA */
    .stButton>button {{
        background: linear-gradient(135deg, #D4AF37 0%, #F0D575 100%);
        color: #000000 !important;
        font-weight: 800 !important;
        border-radius: 50px;
        border: none;
        padding: 20px;
        width: 100%;
        height: 65px;
        text-transform: uppercase;
        box-shadow: 0 8px 25px rgba(212, 175, 55, 0.4);
        transition: all 0.3s ease;
    }}
    
    .stButton>button:hover {{
        transform: scale(1.02);
        box-shadow: 0 10px 30px rgba(212, 175, 55, 0.6);
    }}

    /* CARTÕES DE PORTFÓLIO COM EFEITO HOVER ALPHA */
    .portfolio-card {{
        background-color: rgba(10, 10, 10, 0.9);
        border: 2px solid #D4AF37;
        border-radius: 15px;
        margin-bottom: 2.5rem;
        overflow: hidden;
        transition: all 0.4s ease;
        box-shadow: 0 15px 35px rgba(0,0,0,0.7);
    }}
    
    .portfolio-card:hover {{
        transform: scale(1.03);
        box-shadow: 0 20px 45px rgba(212, 175, 55, 0.3);
        border-color: #F0D575;
    }}
    
    .portfolio-card img {{
        width: 100%;
        height: auto;
        display: block;
        aspect-ratio: 1 / 1;
        object-fit: cover;
        border-bottom: 2px solid #D4AF37;
    }}
    
    .portfolio-details {{
        padding: 1.5rem;
        background: linear-gradient(180deg, rgba(20,20,20,1) 0%, rgba(0,0,0,1) 100%);
    }}
    
    .portfolio-title {{ color: #D4AF37; font-weight: bold; font-size: 1.2rem; margin-bottom: 0.5rem; }}
    .portfolio-feedback {{ color: #FFFFFF; font-style: italic; font-size: 0.9rem; line-height: 1.5; opacity: 0.8; }}

    .stAlert {{ background-color: rgba(212, 175, 55, 0.1); border: 1px solid #D4AF37; color: #D4AF37 !important; border-radius: 12px; }}
    hr {{ border: 0; height: 1px; background: linear-gradient(90deg, transparent, #D4AF37, transparent); margin: 2rem 0; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. CABEÇALHO ---
st.markdown("<h1>💎 Jóias Dentais</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #B0B0B0;'>Estética de alto padrão com Grillz e Piercings premium em Porto Alegre.</p>", unsafe_allow_html=True)

# --- 5. SEÇÃO 1: SIMULADOR (ATUALIZADO COM VALORES DAS IMAGENS) ---
st.markdown("<h3>1. Simule o seu Projeto</h3>", unsafe_allow_html=True)
col_sim1, col_sim2 = st.columns([1, 1])

with col_sim1:
    tipo_servico = st.selectbox("Tipo de serviço:", ["Piercings Dentais (Cristais)", "Cap (1 dente)", "Mini Grillz (2 dentes)", "Limpeza"])
    
    if tipo_servico == "Piercings Dentais (Cristais)":
        material = st.selectbox("Quantidade de Cristais:", ["1 ou 2 cristais", "3 a 6 cristais", "7 a 10 cristais", "Mais de 10 cristais"])
    elif tipo_servico == "Limpeza":
        material = "Procedimento Clínico"
    else:
        material = st.selectbox("Material de preferência:", [
            "MCO (Dourado ou Prateado)", 
            "Prata 950", 
            "Banhado a Ouro", 
            "Cravejado (Zircônia com Prata)", 
            "Cravejado e Banhado", 
            "Ouro Maciço"
        ])

with col_sim2:
    if tipo_servico in ["Cap (1 dente)", "Mini Grillz (2 dentes)"]:
        quantidade = st.number_input("Quantidade de peças:", min_value=1, max_value=10, value=1)
    else:
        quantidade = 1

    # TABELA DE PREÇOS EXTRAÍDA DAS IMAGENS
    tabela_precos = {
        "Piercings Dentais (Cristais)": {"1 ou 2 cristais": 180.0, "3 a 6 cristais": 260.0, "7 a 10 cristais": 320.0, "Mais de 10 cristais": 450.0},
        "Cap (1 dente)": {
            "MCO (Dourado ou Prateado)": 500.0, "Prata 950": 600.0, "Banhado a Ouro": 650.0, 
            "Cravejado (Zircônia com Prata)": 950.0, "Cravejado e Banhado": 1150.0, "Ouro Maciço": 3000.0
        },
        "Mini Grillz (2 dentes)": { 
            "MCO (Dourado ou Prateado)": 600.0, "Prata 950": 650.0, "Banhado a Ouro": 700.0, 
            "Cravejado (Zircônia com Prata)": 1100.0, "Cravejado e Banhado": 1250.0, "Ouro Maciço": 3200.0
        },
        "Limpeza": {"Procedimento Clínico": 250.0}
    }
    
    estimativa_total = tabela_precos[tipo_servico][material] * quantidade
    st.info(f"💰 Investimento Estimado: R$ {estimativa_total:,.2f}")

# --- 6. SEÇÃO 2: CALL TO ACTION ---
st.markdown("<h3>2. Agendar Avaliação Especializada</h3>", unsafe_allow_html=True)
c_lead1, c_lead2 = st.columns(2)
with c_lead1:
    nome_cliente = st.text_input("Nome Completo:", placeholder="Digite seu nome...")
with c_lead2:
    obs_cliente = st.text_input("Alguma dúvida específica?", placeholder="Ex: Quanto tempo dura?")

# NÚMERO DA DRA. RAISA CONFORME IMAGEM
numero_doutora = "5551980376259" 
texto_base = (f"Olá Dra. Raisa! Realizei uma simulação no site 'Jóias Dentais'.\n\n*Serviço:* {tipo_servico}\n*Material/Opção:* {material}\n*Quantidade:* {quantidade}\n*Valor Estimado:* R$ {estimativa_total:,.2f}\n\n*Cliente:* {nome_cliente}\n*Dúvida:* {obs_cliente}")
url_whatsapp = f"https://wa.me/{numero_doutora}?text={texto_base.replace(' ', '%20').replace('\n', '%0A')}"

# CORREÇÃO ALPHA: JS PARA ABRIR EM NOVA ABA E EVITAR ERRO DE REFUSA DO NAVEGADOR
if st.button("ENVIAR PEDIDO PARA O WHATSAPP"):
    if nome_cliente:
        js = f"window.open('{url_whatsapp}', '_blank').focus();"
        st.markdown(f'<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=" onload="{js}">', unsafe_allow_html=True)
        st.success("Abrindo conversa no WhatsApp...")
    else:
        st.error("Alpha, informe o nome para que a Dra. possa dar o atendimento exclusivo!")

# --- 7. SEÇÃO 3: GALERIA ---
st.markdown("<h3>📸 Galeria de Resultados Reais</h3>", unsafe_allow_html=True)
with st.container():
    c_port1, c_port2, c_port3 = st.columns(3)
    dados_portfolio = [
        {"img": foto1_b64, "titulo": "Design Piercing Luxury", "txt": "Aplicação de cristais com brilho máximo."},
        {"img": foto2_b64, "titulo": "Grillz Silver Custom", "txt": "Peça personalizada em Prata 950."},
        {"img": foto3_b64, "titulo": "Procedimento VIP Combo", "txt": "Mix de estética dental para um sorriso imponente."}
    ]
    cols_port = [c_port1, c_port2, c_port3]
    for idx, col in enumerate(cols_port):
        with col:
            st.markdown(f"""
                <div class="portfolio-card">
                    <img src="data:image/jpeg;base64,{dados_portfolio[idx]['img']}" alt="Resultado">
                    <div class="portfolio-details">
                        <div class="portfolio-title">{dados_portfolio[idx]['titulo']}</div>
                        <div class="portfolio-feedback">"{dados_portfolio[idx]['txt']}"</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# --- 8. RODAPÉ ---
st.markdown("<br><br><p style='text-align: center; color: #444; font-size: 0.8rem;'>Tecnologia e Performance por Alpha Tech | 2026</p>", unsafe_allow_html=True)
