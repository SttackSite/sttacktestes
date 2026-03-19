import streamlit as st

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Sprint - Transformação Profissional",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS PARA REPLICAR O DESIGN 100% (DARK & NEON)
style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    /* Esconder elementos Streamlit */
    [data-testid="stHeader"], [data-testid="stDecoration"] { display: none; }
    .main { padding: 0 !important; }
    
    body {
        background-color: #000000;
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    /* Cores */
    :root {
        --neon-green: #97ff00;
        --dark-bg: #0a0a0a;
        --gray-text: #a0a0a0;
    }

    /* SEÇÃO HERO */
    .hero-section {
        background: radial-gradient(circle at 70% 30%, #1a3300 0%, #000000 70%);
        padding: 60px 10%;
        min-height: 80vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .sprint-logo { color: var(--neon-green); font-weight: 900; font-size: 24px; margin-bottom: 40px; }
    .hero-title { font-size: 56px; font-weight: 900; line-height: 1.1; max-width: 600px; }
    .hero-title span { color: var(--neon-green); }
    .hero-subtitle { color: var(--gray-text); font-size: 18px; max-width: 500px; margin: 30px 0; }

    /* BOTÃO NEON */
    .btn-neon {
        background-color: var(--neon-green);
        color: #000 !important;
        padding: 18px 40px;
        border-radius: 5px;
        font-weight: 900;
        font-size: 16px;
        text-decoration: none;
        display: inline-block;
        text-transform: uppercase;
        transition: 0.3s;
        text-align: center;
    }
    .btn-neon:hover { transform: scale(1.05); box-shadow: 0 0 20px rgba(151, 255, 0, 0.4); }

    /* BARRA DE DESTAQUE */
    .highlight-bar {
        background-color: var(--neon-green);
        color: #000;
        padding: 15px;
        text-align: center;
        font-weight: 700;
        font-size: 14px;
    }

    /* CARDS DE PILARES */
    .pillar-card {
        background-color: #111;
        padding: 40px 20px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #222;
        height: 100%;
    }
    .pillar-icon { font-size: 40px; color: var(--neon-green); margin-bottom: 20px; }
    .pillar-title { font-weight: 900; font-size: 20px; margin-bottom: 15px; }
    .pillar-desc { color: var(--gray-text); font-size: 14px; }

    /* CHECKOUT CARD */
    .checkout-container {
        border: 2px solid var(--neon-green);
        background: #000;
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        max-width: 500px;
        margin: 50px auto;
    }
    .price-old { text-decoration: line-through; color: var(--gray-text); font-size: 18px; }
    .price-main { color: var(--neon-green); font-size: 64px; font-weight: 900; margin: 10px 0; }
    .price-parcel { font-size: 20px; color: #fff; }

    /* RESPONSIVIDADE */
    @media (max-width: 768px) {
        .hero-title { font-size: 32px; }
        .hero-section { text-align: center; align-items: center; }
    }
</style>
"""
st.markdown(style, unsafe_allow_html=True)

# --- ESTRUTURA DA PÁGINA ---

# 1. HERO
st.markdown(f'''
<div class="hero-section">
    <div class="sprint-logo">SPRINT</div>
    <div class="hero-title">Seja o profissional mais desejado e <span>bem pago</span> do mercado!</div>
    <div class="hero-subtitle">
        Desenvolva sua COMUNICAÇÃO, LIDERANÇA e saiba utilizar a 
        INTELIGÊNCIA ARTIFICIAL para aumentar sua produtividade.
    </div>
    <a href="#checkout" class="btn-neon">Garantir minha vaga!</a>
</div>
''', unsafe_allow_html=True)

# 2. BARRA VERDE
st.markdown('<div class="highlight-bar">Todo nosso conhecimento reunido em um único lugar! ▼</div>', unsafe_allow_html=True)

# 3. OS 3 PILARES
st.markdown("<br><br><h2 style='text-align:center; font-weight:900;'>Domine os <span style='color:#97ff00'>3 pilares</span> do profissional do futuro.</h2><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('''<div class="pillar-card">
        <div class="pillar-icon">📢</div>
        <div class="pillar-title">Comunicação</div>
        <div class="pillar-desc">Técnicas de assertividade e oratória para engajar audiências e vender suas ideias.</div>
    </div>''', unsafe_allow_html=True)
with col2:
    st.markdown('''<div class="pillar-card">
        <div class="pillar-icon">⚙️</div>
        <div class="pillar-title">Produtividade</div>
        <div class="pillar-desc">Implementação de ferramentas de IA para otimizar seu tempo e dobrar sua entrega.</div>
    </div>''', unsafe_allow_html=True)
with col3:
    st.markdown('''<div class="pillar-card">
        <div class="pillar-icon">🤝</div>
        <div class="pillar-title">Liderança</div>
        <div class="pillar-desc">Gestão de equipes de alto desempenho e inteligência emocional estratégica.</div>
    </div>''', unsafe_allow_html=True)

# 4. CHECKOUT (OFERTA)
st.markdown('<div id="checkout"></div>', unsafe_allow_html=True)
st.markdown(f'''
<div class="checkout-container">
    <div style="font-weight:700; margin-bottom:20px;">OFERTA EXCLUSIVA</div>
    <div class="price-old">De: R$ 697</div>
    <div class="price-parcel">12x</div>
    <div class="price-main">28,85</div>
    <div style="margin-bottom:30px;">Ou R$ 297,00 à vista</div>
    <a href="#" class="btn-neon" style="width:100%">Quero aproveitar a promoção!</a>
    <div style="margin-top:20px; font-size:12px; color:#666;">🔒 Pagamento Seguro | Acesso Imediato</div>
</div>
''', unsafe_allow_html=True)

# 5. MENTOR (SUBSTITUIÇÃO DA FOTO POR TEXTO ESTILIZADO)
st.write("---")
mcol1, mcol2 = st.columns([1, 2])
with mcol1:
    st.markdown("<div style='background:#222; height:300px; border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:50px;'>👤</div>", unsafe_allow_html=True)
with mcol2:
    st.markdown('''
    <h2 style="font-weight:900;">Quem vai ser o <span style="color:#97ff00">meu mentor?</span></h2>
    <p style="color:#aaa;">
        Especialista em alta performance com mais de 10 anos de mercado. 
        Já treinou grandes líderes e empresas do setor de tecnologia e marketing digital. 
        Referência em produtividade e comportamento humano aplicado ao trabalho.
    </p>
    <a href="#" class="btn-neon">Garantir minha vaga!</a>
    ''', unsafe_allow_html=True)

# FOOTER
st.markdown("<br><br><div style='text-align:center; padding:40px; color:#444; font-size:12px;'>© 2026 Sprint Treinamentos. Todos os direitos reservados.</div>", unsafe_allow_html=True)
