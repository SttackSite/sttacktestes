import streamlit as st

st.set_page_config(page_title="QuiteJá - Suas Dívidas sob Controle", page_icon="💚", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&display=swap');

:root {
    --green: #059669;
    --green-light: #10b981;
    --green-pale: #d1fae5;
    --green-dark: #065f46;
    --bg: #f8fffe;
    --white: #ffffff;
    --text: #0f1a15;
    --muted: #6b7280;
    --border: #d1fae5;
    --border-gray: #e5e7eb;
    --yellow: #f59e0b;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Sora', sans-serif;
}
[data-testid="stHeader"] { display: none; }
[data-testid="stSidebar"] { display: none; }
.main .block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stVerticalBlock"] { gap: 0 !important; }

/* NAV */
.nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 999;
    display: flex; align-items: center; justify-content: space-between;
    padding: 1rem 6%; background: rgba(248,255,254,0.92); backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--border);
}
.nav-logo { display: flex; align-items: center; gap: 0.5rem; }
.nav-logo-icon { background: var(--green); color: white; width: 34px; height: 34px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 0.9rem; font-weight: 700; }
.nav-logo-text { font-size: 1.2rem; font-weight: 800; color: var(--text); }
.nav-logo-text span { color: var(--green); }
.nav-btns { display: flex; gap: 1rem; align-items: center; }
.nav-link { color: var(--muted); text-decoration: none; font-size: 0.875rem; font-weight: 600; }
.nav-link:hover { color: var(--green); }
.nav-dl { display: flex; gap: 0.5rem; }
.dl-btn { background: white; border: 1px solid var(--border-gray); color: var(--text); padding: 0.5rem 1rem; border-radius: 8px; font-size: 0.8rem; font-weight: 600; text-decoration: none; transition: all 0.3s; }
.dl-btn:hover { border-color: var(--green); color: var(--green); }
.nav-cta { background: var(--green); color: white; padding: 0.6rem 1.4rem; border-radius: 8px; font-size: 0.875rem; font-weight: 700; text-decoration: none; }

/* HERO */
.hero { padding: 8rem 6% 4rem; display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 4rem; align-items: center; }
.hero-tag { display: inline-flex; align-items: center; gap: 0.5rem; background: var(--green-pale); color: var(--green-dark); border-radius: 50px; padding: 0.4rem 1rem; font-size: 0.8rem; font-weight: 700; margin-bottom: 1.5rem; }
.hero h1 { font-size: clamp(2.5rem, 4.5vw, 4rem); font-weight: 800; line-height: 1.1; color: var(--text); margin-bottom: 1.5rem; }
.hero h1 span { color: var(--green); }
.hero p { color: var(--muted); font-size: 1rem; line-height: 1.75; margin-bottom: 1.5rem; }
.app-badges { display: flex; gap: 0.75rem; flex-wrap: wrap; margin-bottom: 1.5rem; }
.app-badge { background: var(--text); color: white; padding: 0.6rem 1.2rem; border-radius: 10px; font-size: 0.8rem; font-weight: 600; text-decoration: none; display: flex; align-items: center; gap: 0.5rem; transition: all 0.3s; }
.app-badge:hover { background: var(--green); }
.hero-rating { display: flex; align-items: center; gap: 0.75rem; }
.stars { color: var(--yellow); font-size: 1rem; }
.rating-text { font-size: 0.875rem; color: var(--muted); }
.rating-text strong { color: var(--text); }

.hero-visual { position: relative; }
.phone-mockup {
    background: linear-gradient(135deg, #065f46, #059669);
    border-radius: 36px; padding: 2.5rem 2rem;
    color: white; max-width: 300px; margin: 0 auto;
    box-shadow: 0 40px 80px rgba(5,150,105,0.3);
}
.phone-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; }
.phone-logo { font-weight: 800; font-size: 1rem; }
.phone-btn { background: rgba(255,255,255,0.2); border: none; color: white; padding: 0.4rem 0.8rem; border-radius: 8px; font-size: 0.75rem; cursor: pointer; }
.phone-balance { text-align: center; margin-bottom: 1.5rem; }
.pb-label { opacity: 0.7; font-size: 0.8rem; margin-bottom: 0.25rem; }
.pb-amount { font-size: 2.5rem; font-weight: 800; }
.phone-list { display: flex; flex-direction: column; gap: 0.75rem; }
.phone-item { background: rgba(255,255,255,0.1); border-radius: 12px; padding: 0.9rem 1rem; display: flex; justify-content: space-between; align-items: center; }
.pi-name { font-size: 0.85rem; font-weight: 600; }
.pi-date { font-size: 0.75rem; opacity: 0.6; }
.pi-amount { font-size: 0.9rem; font-weight: 700; color: #6ee7b7; }
.phone-add-btn { width: 100%; background: white; color: var(--green); border: none; padding: 0.9rem; border-radius: 14px; font-weight: 800; font-size: 0.9rem; margin-top: 1.5rem; cursor: pointer; font-family: 'Sora', sans-serif; }

.float-badge { position: absolute; background: white; border-radius: 14px; padding: 1rem 1.2rem; box-shadow: 0 16px 40px rgba(0,0,0,0.12); border: 1px solid var(--border-gray); }
.fb-top { top: -20px; right: -30px; }
.fb-bottom { bottom: 30px; left: -30px; }
.fb-icon { font-size: 1.2rem; margin-bottom: 0.25rem; }
.fb-value { font-weight: 800; font-size: 1rem; color: var(--text); }
.fb-label { font-size: 0.75rem; color: var(--muted); }

/* WHY */
.why-section { padding: 6rem 6%; }
.section-center { text-align: center; margin-bottom: 3.5rem; }
.section-pill { display: inline-block; background: var(--green-pale); color: var(--green-dark); padding: 0.35rem 1rem; border-radius: 50px; font-size: 0.8rem; font-weight: 700; margin-bottom: 1rem; }
.section-title { font-size: clamp(2rem, 3.5vw, 2.8rem); font-weight: 800; color: var(--text); line-height: 1.2; margin-bottom: 1rem; }
.section-title span { color: var(--green); }
.section-sub { color: var(--muted); font-size: 0.95rem; line-height: 1.7; max-width: 500px; margin: 0 auto; }
.why-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
.why-card { background: white; border: 1px solid var(--border-gray); border-radius: 20px; padding: 2rem; transition: all 0.3s; }
.why-card:hover { border-color: var(--green); transform: translateY(-4px); box-shadow: 0 16px 40px rgba(5,150,105,0.1); }
.why-icon { width: 52px; height: 52px; border-radius: 16px; background: var(--green-pale); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin-bottom: 1.2rem; }
.why-title { font-weight: 700; font-size: 1rem; color: var(--text); margin-bottom: 0.5rem; }
.why-desc { color: var(--muted); font-size: 0.875rem; line-height: 1.7; }

/* HOW */
.how-section { padding: 6rem 6%; display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; align-items: center; }
.how-visual { order: 2; }
.how-text { order: 1; }
.how-steps { display: flex; flex-direction: column; gap: 2rem; margin-top: 2.5rem; }
.how-step { display: flex; gap: 1.5rem; }
.how-step-num { width: 40px; height: 40px; border-radius: 50%; background: var(--green); color: white; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 0.9rem; flex-shrink: 0; }
.how-step-title { font-weight: 700; font-size: 0.95rem; margin-bottom: 0.35rem; }
.how-step-desc { color: var(--muted); font-size: 0.875rem; line-height: 1.6; }

.simplify-card { background: var(--green-dark); border-radius: 24px; padding: 2.5rem; color: white; }
.sc-title { font-weight: 800; font-size: 1.1rem; margin-bottom: 1.5rem; text-align: center; }
.sc-steps { display: flex; flex-direction: column; gap: 1rem; }
.sc-step { background: rgba(255,255,255,0.08); border-radius: 12px; padding: 1rem 1.2rem; display: flex; align-items: center; gap: 1rem; }
.sc-step-num { width: 32px; height: 32px; border-radius: 50%; background: var(--green-light); color: white; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 0.8rem; flex-shrink: 0; }
.sc-step-text strong { display: block; font-size: 0.875rem; margin-bottom: 0.2rem; }
.sc-step-text span { font-size: 0.8rem; opacity: 0.6; }

/* TESTIMONIALS */
.testimonials-section { padding: 6rem 6%; background: white; }
.t-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-top: 3rem; }
.t-card { border: 1px solid var(--border-gray); border-radius: 20px; padding: 2rem; transition: all 0.3s; }
.t-card:hover { border-color: var(--green); }
.t-stars { color: var(--yellow); margin-bottom: 1rem; }
.t-text { color: var(--muted); font-size: 0.875rem; line-height: 1.7; margin-bottom: 1.5rem; }
.t-author { display: flex; align-items: center; gap: 0.75rem; }
.t-av { width: 42px; height: 42px; border-radius: 50%; background: var(--green); display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 0.9rem; flex-shrink: 0; }
.t-name { font-weight: 700; font-size: 0.875rem; }
.t-role { color: var(--muted); font-size: 0.8rem; }

/* STATS */
.stats-section { padding: 5rem 6%; background: var(--green-dark); color: white; }
.stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; text-align: center; }
.stat-num { font-size: 3rem; font-weight: 800; color: var(--green-light); margin-bottom: 0.5rem; }
.stat-label { opacity: 0.7; font-size: 0.875rem; }

/* CTA */
.cta-section { padding: 6rem 6%; text-align: center; }
.cta-inner { background: var(--green); border-radius: 28px; padding: 5rem 3rem; color: white; position: relative; overflow: hidden; }
.cta-inner::before { content: '💚'; position: absolute; top: -30px; right: 5%; font-size: 8rem; opacity: 0.1; }
.cta-inner h2 { font-size: clamp(2rem, 4vw, 3rem); font-weight: 800; margin-bottom: 1rem; }
.cta-inner p { opacity: 0.85; font-size: 1rem; margin-bottom: 2rem; }
.cta-badges { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
.cta-btn { background: white; color: var(--green); padding: 0.9rem 2rem; border-radius: 12px; font-weight: 800; font-size: 0.95rem; text-decoration: none; transition: all 0.3s; }
.cta-btn:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,0.2); }

/* FOOTER */
.footer { padding: 3rem 6%; background: var(--text); color: white; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; }
.footer-links { display: flex; gap: 2rem; }
.footer-links a { color: rgba(255,255,255,0.4); text-decoration: none; font-size: 0.85rem; }
.footer-links a:hover { color: var(--green-light); }
.footer-copy { color: rgba(255,255,255,0.3); font-size: 0.8rem; }

@media (max-width: 900px) {
    .hero, .how-section { grid-template-columns: 1fr; }
    .why-grid, .t-grid, .stats-grid { grid-template-columns: 1fr 1fr; }
    .how-visual { order: 1; }
    .how-text { order: 2; }
}
</style>

<nav class="nav">
    <div class="nav-logo">
        <div class="nav-logo-icon">💚</div>
        <div class="nav-logo-text">Quite<span>Já</span></div>
    </div>
    <div class="nav-btns">
        <div class="nav-dl">
            <a href="#" class="dl-btn">📱 App Store</a>
            <a href="#" class="dl-btn">🤖 Google Play</a>
        </div>
        <a href="#" class="nav-cta">Baixar Grátis</a>
    </div>
</nav>

<section class="hero">
    <div>
        <div class="hero-tag">🏆 App #1 de Controle de Dívidas</div>
        <h1>Todas as suas<br><span>Dívidas</span><br>em um lugar só</h1>
        <p>Gerencie, organize e quite suas dívidas de forma inteligente. O QuiteJá te ajuda a recuperar o controle financeiro da sua vida.</p>
        <div class="app-badges">
            <a href="#" class="app-badge">🍎 App Store</a>
            <a href="#" class="app-badge">🤖 Google Play</a>
        </div>
        <div class="hero-rating">
            <div class="stars">★★★★★</div>
            <div class="rating-text"><strong>4.9</strong> · mais de 100K downloads</div>
        </div>
    </div>
    <div class="hero-visual">
        <div class="phone-mockup">
            <div class="phone-header">
                <div class="phone-logo">💚 QuiteJá</div>
                <button class="phone-btn">+ Adicionar</button>
            </div>
            <div class="phone-balance">
                <div class="pb-label">Total em Dívidas</div>
                <div class="pb-amount">R$ 12.840</div>
            </div>
            <div class="phone-list">
                <div class="phone-item">
                    <div><div class="pi-name">Cartão Nubank</div><div class="pi-date">Vence em 15 dias</div></div>
                    <div class="pi-amount">R$ 3.200</div>
                </div>
                <div class="phone-item">
                    <div><div class="pi-name">Empréstimo Banco</div><div class="pi-date">Vence em 8 dias</div></div>
                    <div class="pi-amount">R$ 6.800</div>
                </div>
                <div class="phone-item">
                    <div><div class="pi-name">Financiamento Auto</div><div class="pi-date">Vence em 22 dias</div></div>
                    <div class="pi-amount">R$ 2.840</div>
                </div>
            </div>
            <button class="phone-add-btn">📊 Ver Plano de Quitação</button>
        </div>
        <div class="float-badge fb-top">
            <div class="fb-icon">🔔</div>
            <div class="fb-value">Lembrete!</div>
            <div class="fb-label">Pagamento em 3 dias</div>
        </div>
        <div class="float-badge fb-bottom">
            <div class="fb-icon">✅</div>
            <div class="fb-value">Dívida quitada!</div>
            <div class="fb-label">R$ 2.400 pagos</div>
        </div>
    </div>
</section>

<section class="why-section">
    <div class="section-center">
        <div class="section-pill">💡 Por que QuiteJá?</div>
        <div class="section-title">Por que tantas pessoas<br>escolhem o <span>QuiteJá</span>?</div>
        <div class="section-sub">Simples, poderoso e feito para quem quer sair das dívidas de uma vez por todas.</div>
    </div>
    <div class="why-grid">
        <div class="why-card">
            <div class="why-icon">⚡</div>
            <div class="why-title">Fácil de Usar</div>
            <div class="why-desc">Adicione dívidas com todos os detalhes — valor, moeda, motivo e credor — em segundos. Interface intuitiva para qualquer pessoa.</div>
        </div>
        <div class="why-card">
            <div class="why-icon">🔔</div>
            <div class="why-title">Lembretes Automáticos</div>
            <div class="why-desc">Configure notificações personalizadas para nunca perder um pagamento. Chega de multas e juros por esquecimento.</div>
        </div>
        <div class="why-card">
            <div class="why-icon">🌍</div>
            <div class="why-title">Múltiplas Moedas</div>
            <div class="why-desc">Gerencie dívidas em real, dólar, euro e muito mais. Conversão automática em tempo real com taxas atualizadas.</div>
        </div>
    </div>
</section>

<section class="how-section">
    <div class="how-text">
        <div class="section-pill">📱 Como Funciona</div>
        <div class="section-title">Simplifique<br>suas <span>Dívidas</span></div>
        <div class="how-steps">
            <div class="how-step">
                <div class="how-step-num">1</div>
                <div>
                    <div class="how-step-title">Crie uma conta</div>
                    <div class="how-step-desc">Abra sua conta em passos simples ou faça login na sua conta existente.</div>
                </div>
            </div>
            <div class="how-step">
                <div class="how-step-num">2</div>
                <div>
                    <div class="how-step-title">Adicione seus credores</div>
                    <div class="how-step-desc">Seja uma pessoa ou loja, adicione com todos os detalhes necessários.</div>
                </div>
            </div>
            <div class="how-step">
                <div class="how-step-num">3</div>
                <div>
                    <div class="how-step-title">Adicione os detalhes da dívida</div>
                    <div class="how-step-desc">Informe o valor, moeda, motivo e configure os lembretes de pagamento.</div>
                </div>
            </div>
        </div>
    </div>
    <div class="how-visual">
        <div class="simplify-card">
            <div class="sc-title">🗂️ Seu Plano de Quitação</div>
            <div class="sc-steps">
                <div class="sc-step">
                    <div class="sc-step-num">1</div>
                    <div class="sc-step-text"><strong>Cartão de Crédito</strong><span>Prioridade: Alta · R$ 3.200</span></div>
                </div>
                <div class="sc-step">
                    <div class="sc-step-num">2</div>
                    <div class="sc-step-text"><strong>Empréstimo Pessoal</strong><span>Prioridade: Média · R$ 6.800</span></div>
                </div>
                <div class="sc-step">
                    <div class="sc-step-num">3</div>
                    <div class="sc-step-text"><strong>Financiamento Auto</strong><span>Prioridade: Normal · R$ 2.840</span></div>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="testimonials-section">
    <div class="section-center">
        <div class="section-pill">💬 Depoimentos</div>
        <div class="section-title">Ajudamos <span>muitas pessoas</span></div>
    </div>
    <div class="t-grid">
        <div class="t-card">
            <div class="t-stars">★★★★★</div>
            <div class="t-text">"Em 8 meses usando o QuiteJá quitei R$ 28.000 em dívidas. O plano de quitação me mostrou exatamente o que fazer. Incrível!"</div>
            <div class="t-author"><div class="t-av">BC</div><div><div class="t-name">Bessie Cooper</div><div class="t-role">Professora</div></div></div>
        </div>
        <div class="t-card">
            <div class="t-stars">★★★★★</div>
            <div class="t-text">"Os lembretes me salvaram de multas diversas vezes. A interface é linda e muito fácil de usar. Recomendo para todos!"</div>
            <div class="t-author"><div class="t-av">JB</div><div><div class="t-name">Jerome Bell</div><div class="t-role">Empreendedor</div></div></div>
        </div>
        <div class="t-card">
            <div class="t-stars">★★★★★</div>
            <div class="t-text">"Uso para controlar dívidas em dólar e real. Conversão automática perfeita. Finalmente um app que entende quem tem dívidas internacionais."</div>
            <div class="t-author"><div class="t-av">JJ</div><div><div class="t-name">Jacob Jones</div><div class="t-role">Importador</div></div></div>
        </div>
    </div>
</section>

<section class="stats-section">
    <div class="stats-grid">
        <div><div class="stat-num">100K+</div><div class="stat-label">Downloads realizados</div></div>
        <div><div class="stat-num">R$2.4B</div><div class="stat-label">Em dívidas gerenciadas</div></div>
        <div><div class="stat-num">4.9★</div><div class="stat-label">Avaliação nas lojas</div></div>
        <div><div class="stat-num">98%</div><div class="stat-label">Usuários satisfeitos</div></div>
    </div>
</section>

<section class="cta-section">
    <div class="cta-inner">
        <h2>Saia das dívidas<br>do seu jeito!</h2>
        <p>Baixe grátis e comece sua jornada rumo à liberdade financeira hoje.</p>
        <div class="cta-badges">
            <a href="#" class="cta-btn">🍎 Baixar no App Store</a>
            <a href="#" class="cta-btn">🤖 Baixar no Google Play</a>
        </div>
    </div>
</section>

<footer class="footer">
    <div class="nav-logo"><div class="nav-logo-icon">💚</div><div class="nav-logo-text" style="color:white;">Quite<span style="color:#6ee7b7;">Já</span></div></div>
    <div class="footer-links"><a href="#">Privacidade</a><a href="#">Termos</a><a href="#">Suporte</a><a href="#">Blog</a></div>
    <div class="footer-copy">© 2025 QuiteJá. Feito com 💚 no Brasil.</div>
</footer>
""", unsafe_allow_html=True)
