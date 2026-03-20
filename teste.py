import streamlit as st

st.set_page_config(page_title="FlowPay - Controle Financeiro", page_icon="💜", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

:root {
    --bg: #fafafa;
    --white: #ffffff;
    --purple: #7c3aed;
    --purple-light: #a78bfa;
    --purple-dark: #5b21b6;
    --pink: #ec4899;
    --blue: #3b82f6;
    --dark: #0f0a1e;
    --text: #1e1b4b;
    --muted: #6b7280;
    --border: #e5e7eb;
    --card-bg: #ffffff;
    --green: #10b981;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
}
[data-testid="stHeader"] { display: none; }
[data-testid="stSidebar"] { display: none; }
.main .block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stVerticalBlock"] { gap: 0 !important; }

/* NAV */
.nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 999;
    display: flex; align-items: center; justify-content: space-between;
    padding: 1rem 6%;
    background: rgba(250,250,250,0.85); backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border);
}
.nav-logo { display: flex; align-items: center; gap: 0.5rem; font-weight: 800; font-size: 1.2rem; color: var(--text); }
.nav-logo-icon {
    width: 32px; height: 32px; border-radius: 8px;
    background: linear-gradient(135deg, var(--purple), var(--pink));
    display: flex; align-items: center; justify-content: center; color: white; font-size: 0.9rem;
}
.nav-links { display: flex; gap: 2rem; }
.nav-links a { color: var(--muted); text-decoration: none; font-size: 0.9rem; font-weight: 500; transition: color 0.3s; }
.nav-links a:hover { color: var(--purple); }
.nav-cta {
    background: linear-gradient(135deg, var(--purple), var(--pink));
    color: white; padding: 0.65rem 1.8rem; border-radius: 50px;
    font-size: 0.875rem; font-weight: 700; text-decoration: none;
    box-shadow: 0 4px 20px rgba(124,58,237,0.35);
    transition: all 0.3s;
}
.nav-cta:hover { transform: translateY(-2px); box-shadow: 0 8px 30px rgba(124,58,237,0.5); }

/* HERO */
.hero {
    padding: 9rem 6% 5rem; text-align: center;
    background: var(--bg);
    position: relative; overflow: hidden;
}
.hero-blob {
    position: absolute; top: -10%; left: 50%; transform: translateX(-50%);
    width: 800px; height: 600px;
    background: radial-gradient(ellipse at center, rgba(124,58,237,0.12) 0%, rgba(236,72,153,0.06) 50%, transparent 70%);
    pointer-events: none;
}
.hero-chip {
    display: inline-flex; align-items: center; gap: 0.5rem;
    background: var(--white); border: 1px solid var(--border);
    padding: 0.4rem 1rem 0.4rem 0.4rem; border-radius: 50px;
    font-size: 0.8rem; font-weight: 600; color: var(--text);
    margin-bottom: 2rem;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.hero-chip-badge {
    background: linear-gradient(135deg, var(--purple), var(--pink));
    color: white; padding: 0.2rem 0.6rem; border-radius: 50px; font-size: 0.7rem; font-weight: 700;
}
.hero h1 {
    font-size: clamp(2.5rem, 5.5vw, 5rem);
    font-weight: 800; line-height: 1.1;
    color: var(--text);
    margin-bottom: 1.5rem;
}
.hero h1 .gradient-text {
    background: linear-gradient(135deg, var(--purple), var(--pink));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero p { color: var(--muted); font-size: 1.1rem; line-height: 1.7; max-width: 550px; margin: 0 auto 2.5rem; }
.hero-btns { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-bottom: 3rem; }
.btn-grad {
    background: linear-gradient(135deg, var(--purple), var(--pink));
    color: white; padding: 0.9rem 2.5rem; border-radius: 50px;
    font-weight: 700; font-size: 1rem; text-decoration: none;
    box-shadow: 0 8px 30px rgba(124,58,237,0.4); transition: all 0.3s;
}
.btn-grad:hover { transform: translateY(-3px); box-shadow: 0 14px 40px rgba(124,58,237,0.5); }
.btn-outline {
    background: white; color: var(--text); border: 1px solid var(--border);
    padding: 0.9rem 2rem; border-radius: 50px;
    font-weight: 600; font-size: 0.95rem; text-decoration: none; transition: all 0.3s;
}
.btn-outline:hover { border-color: var(--purple); color: var(--purple); }

/* HERO MOCKUP */
.hero-mockup {
    max-width: 900px; margin: 0 auto;
    background: var(--white); border-radius: 24px;
    border: 1px solid var(--border);
    box-shadow: 0 40px 100px rgba(0,0,0,0.1), 0 0 0 1px rgba(0,0,0,0.04);
    padding: 2rem; position: relative;
}
.mockup-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 2rem; }
.mockup-title { font-weight: 800; font-size: 1.2rem; }
.mockup-badge { background: rgba(16,185,129,0.1); color: var(--green); padding: 0.3rem 0.75rem; border-radius: 50px; font-size: 0.75rem; font-weight: 700; }
.mockup-balance { text-align: center; margin-bottom: 2rem; }
.balance-label { color: var(--muted); font-size: 0.85rem; margin-bottom: 0.25rem; }
.balance-amount { font-size: 3rem; font-weight: 800; color: var(--text); }
.balance-change { color: var(--green); font-size: 0.9rem; font-weight: 600; }
.mockup-cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
.mockup-card { background: var(--bg); border-radius: 16px; padding: 1.2rem; border: 1px solid var(--border); }
.mc-icon { width: 36px; height: 36px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1rem; margin-bottom: 0.75rem; }
.mc-icon.purple { background: rgba(124,58,237,0.1); }
.mc-icon.pink { background: rgba(236,72,153,0.1); }
.mc-icon.blue { background: rgba(59,130,246,0.1); }
.mc-label { color: var(--muted); font-size: 0.75rem; margin-bottom: 0.25rem; }
.mc-value { font-weight: 700; font-size: 1rem; }

/* LOGOS */
.logos-section { padding: 2.5rem 6%; background: white; border-top: 1px solid var(--border); }
.logos-inner { display: flex; align-items: center; justify-content: center; gap: 4rem; flex-wrap: wrap; }
.logos-label { color: var(--muted); font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }
.logo-item { color: #c0c0cc; font-weight: 800; font-size: 0.95rem; letter-spacing: -0.3px; }

/* FEATURES */
.features-section { padding: 6rem 6%; }
.section-center { text-align: center; margin-bottom: 3.5rem; }
.chip {
    display: inline-flex; align-items: center; gap: 0.4rem;
    background: rgba(124,58,237,0.08); color: var(--purple);
    padding: 0.35rem 1rem; border-radius: 50px;
    font-size: 0.78rem; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase;
    margin-bottom: 1rem;
}
.section-title { font-size: clamp(2rem, 4vw, 3rem); font-weight: 800; color: var(--text); line-height: 1.2; margin-bottom: 1rem; }
.section-sub { color: var(--muted); font-size: 1rem; line-height: 1.7; max-width: 500px; margin: 0 auto; }
.features-bento { display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: auto auto; gap: 1.5rem; }
.bento-card { background: var(--white); border: 1px solid var(--border); border-radius: 20px; padding: 2rem; transition: all 0.3s; }
.bento-card:hover { transform: translateY(-4px); box-shadow: 0 20px 60px rgba(0,0,0,0.08); border-color: rgba(124,58,237,0.2); }
.bento-card.span2 { grid-column: span 2; }
.bento-icon { width: 48px; height: 48px; border-radius: 14px; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; margin-bottom: 1.2rem; }
.bento-icon.p { background: linear-gradient(135deg, rgba(124,58,237,0.15), rgba(124,58,237,0.05)); }
.bento-icon.g { background: linear-gradient(135deg, rgba(16,185,129,0.15), rgba(16,185,129,0.05)); }
.bento-icon.b { background: linear-gradient(135deg, rgba(59,130,246,0.15), rgba(59,130,246,0.05)); }
.bento-icon.pk { background: linear-gradient(135deg, rgba(236,72,153,0.15), rgba(236,72,153,0.05)); }
.bento-title { font-weight: 700; font-size: 1.05rem; color: var(--text); margin-bottom: 0.5rem; }
.bento-desc { color: var(--muted); font-size: 0.875rem; line-height: 1.7; }
.bento-stat { font-size: 2.5rem; font-weight: 800; margin-top: 1rem; }
.bento-stat.purple { background: linear-gradient(135deg, var(--purple), var(--pink)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }

/* HOW IT WORKS */
.how-section { padding: 6rem 6%; background: var(--dark); color: white; }
.how-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; align-items: center; }
.how-steps { display: flex; flex-direction: column; gap: 2rem; }
.how-step { display: flex; gap: 1.5rem; align-items: flex-start; }
.how-num {
    width: 44px; height: 44px; border-radius: 12px; flex-shrink: 0;
    background: linear-gradient(135deg, var(--purple), var(--pink));
    display: flex; align-items: center; justify-content: center;
    font-weight: 800; font-size: 0.875rem; color: white;
}
.how-title { font-weight: 700; margin-bottom: 0.4rem; font-size: 1rem; }
.how-desc { color: rgba(255,255,255,0.5); font-size: 0.875rem; line-height: 1.7; }
.how-visual {
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px; padding: 2rem;
}
.hv-title { font-weight: 700; margin-bottom: 1.5rem; font-size: 0.95rem; color: rgba(255,255,255,0.7); }
.hv-bar { margin-bottom: 1.2rem; }
.hv-bar-label { display: flex; justify-content: space-between; font-size: 0.8rem; color: rgba(255,255,255,0.5); margin-bottom: 0.4rem; }
.hv-bar-track { height: 8px; background: rgba(255,255,255,0.06); border-radius: 50px; overflow: hidden; }
.hv-bar-fill { height: 100%; border-radius: 50px; background: linear-gradient(90deg, var(--purple), var(--pink)); }
.hv-users { display: flex; gap: 1rem; margin-top: 1.5rem; }
.hv-user { display: flex; align-items: center; gap: 0.5rem; font-size: 0.8rem; color: rgba(255,255,255,0.5); }
.hv-avatar { width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700; color: white; }

/* PRICING */
.pricing-section { padding: 6rem 6%; }
.pricing-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; max-width: 950px; margin: 3rem auto 0; }
.price-card { background: white; border: 1px solid var(--border); border-radius: 20px; padding: 2.5rem; position: relative; }
.price-card.featured {
    background: linear-gradient(135deg, var(--purple), var(--purple-dark));
    border-color: transparent; color: white;
    transform: scale(1.03);
    box-shadow: 0 30px 80px rgba(124,58,237,0.4);
}
.price-chip { display: inline-block; background: rgba(255,255,255,0.15); color: white; padding: 0.25rem 0.75rem; border-radius: 50px; font-size: 0.7rem; font-weight: 700; margin-bottom: 1.5rem; }
.price-name { font-size: 0.85rem; font-weight: 600; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.75rem; }
.price-card.featured .price-name { color: rgba(255,255,255,0.7); }
.price-amount { font-size: 3rem; font-weight: 800; color: var(--text); margin-bottom: 0.25rem; }
.price-card.featured .price-amount { color: white; }
.price-period { color: var(--muted); font-size: 0.85rem; margin-bottom: 2rem; }
.price-card.featured .price-period { color: rgba(255,255,255,0.6); }
.price-features { list-style: none; margin-bottom: 2rem; }
.price-features li { padding: 0.6rem 0; border-bottom: 1px solid var(--border); font-size: 0.875rem; display: flex; align-items: center; gap: 0.5rem; }
.price-card.featured .price-features li { border-bottom-color: rgba(255,255,255,0.1); color: rgba(255,255,255,0.85); }
.check { color: var(--green); font-weight: 700; }
.price-card.featured .check { color: rgba(255,255,255,0.9); }
.price-btn { display: block; width: 100%; padding: 0.9rem; border-radius: 50px; text-align: center; font-weight: 700; font-size: 0.9rem; text-decoration: none; transition: all 0.3s; }
.price-btn-outline { background: transparent; border: 1px solid var(--border); color: var(--text); }
.price-btn-outline:hover { border-color: var(--purple); color: var(--purple); }
.price-btn-white { background: white; color: var(--purple); }

/* TESTIMONIALS */
.testimonials-section { padding: 6rem 6%; background: var(--bg); }
.t-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-top: 3rem; }
.t-card { background: white; border: 1px solid var(--border); border-radius: 20px; padding: 2rem; }
.t-stars { color: #f59e0b; font-size: 0.9rem; margin-bottom: 1rem; }
.t-text { color: var(--muted); font-size: 0.9rem; line-height: 1.7; margin-bottom: 1.5rem; }
.t-author { display: flex; align-items: center; gap: 0.75rem; }
.t-avatar { width: 40px; height: 40px; border-radius: 50%; background: linear-gradient(135deg, var(--purple), var(--pink)); display: flex; align-items: center; justify-content: center; color: white; font-weight: 700; font-size: 0.85rem; flex-shrink: 0; }
.t-name { font-weight: 700; font-size: 0.875rem; }
.t-role { color: var(--muted); font-size: 0.8rem; }

/* FAQ */
.faq-section { padding: 6rem 6%; max-width: 750px; margin: 0 auto; }
.faq-item { background: white; border: 1px solid var(--border); border-radius: 16px; padding: 1.5rem; margin-bottom: 1rem; }
.faq-q { font-weight: 700; color: var(--text); margin-bottom: 0.75rem; font-size: 0.95rem; }
.faq-a { color: var(--muted); font-size: 0.875rem; line-height: 1.7; }

/* CTA */
.cta-section {
    margin: 0 4% 4rem;
    border-radius: 28px; padding: 5rem; text-align: center;
    background: linear-gradient(135deg, var(--purple) 0%, var(--purple-dark) 60%, #1e1b4b 100%);
    color: white; position: relative; overflow: hidden;
}
.cta-section::before {
    content: ''; position: absolute; top: -50%; right: -20%;
    width: 400px; height: 400px; border-radius: 50%;
    background: radial-gradient(circle, rgba(236,72,153,0.3) 0%, transparent 70%);
}
.cta-section h2 { font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 800; margin-bottom: 1rem; position: relative; }
.cta-section p { color: rgba(255,255,255,0.7); font-size: 1.1rem; margin-bottom: 2.5rem; position: relative; }
.btn-white { background: white; color: var(--purple); padding: 1rem 2.5rem; border-radius: 50px; font-weight: 700; font-size: 1rem; text-decoration: none; transition: all 0.3s; display: inline-block; }
.btn-white:hover { transform: translateY(-3px); box-shadow: 0 14px 40px rgba(0,0,0,0.25); }

/* FOOTER */
.footer { padding: 3rem 6%; background: var(--dark); color: white; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; }
.footer-logo { display: flex; align-items: center; gap: 0.5rem; font-weight: 800; font-size: 1.1rem; }
.footer-logo-icon { width: 28px; height: 28px; border-radius: 7px; background: linear-gradient(135deg, var(--purple), var(--pink)); display: flex; align-items: center; justify-content: center; font-size: 0.8rem; }
.footer-links { display: flex; gap: 2rem; }
.footer-links a { color: rgba(255,255,255,0.4); text-decoration: none; font-size: 0.85rem; transition: color 0.3s; }
.footer-links a:hover { color: white; }
.footer-copy { color: rgba(255,255,255,0.3); font-size: 0.8rem; }

@media (max-width: 900px) {
    .mockup-cards, .features-bento, .pricing-grid, .t-grid { grid-template-columns: 1fr; }
    .bento-card.span2 { grid-column: span 1; }
    .how-grid { grid-template-columns: 1fr; }
}
</style>

<nav class="nav">
    <div class="nav-logo">
        <div class="nav-logo-icon">💜</div>
        FlowPay
    </div>
    <div class="nav-links">
        <a href="#">Início</a>
        <a href="#">Recursos</a>
        <a href="#">Preços</a>
        <a href="#">Contato</a>
    </div>
    <a href="#" class="nav-cta">Teste Grátis</a>
</nav>

<section class="hero">
    <div class="hero-blob"></div>
    <div class="hero-chip"><span class="hero-chip-badge">NOVO</span> Gestão Financeira com IA</div>
    <h1>Potencialize seu<br><span class="gradient-text">controle financeiro</span><br>com FlowPay</h1>
    <p>Simplifique a gestão financeira da sua empresa com nossa plataforma intuitiva e escalável. Projetada para empresas que crescem.</p>
    <div class="hero-btns">
        <a href="#" class="btn-grad">Começar Grátis — 14 dias</a>
        <a href="#" class="btn-outline">▶ Assistir Demo</a>
    </div>
    <div class="hero-mockup">
        <div class="mockup-header">
            <div class="mockup-title">Painel Financeiro</div>
            <div class="mockup-badge">● Ao Vivo</div>
        </div>
        <div class="mockup-balance">
            <div class="balance-label">Saldo Total da Empresa</div>
            <div class="balance-amount">R$ 847.392</div>
            <div class="balance-change">↑ +12.4% este mês</div>
        </div>
        <div class="mockup-cards">
            <div class="mockup-card"><div class="mc-icon purple">📊</div><div class="mc-label">Receita</div><div class="mc-value">R$ 124K</div></div>
            <div class="mockup-card"><div class="mc-icon pink">💳</div><div class="mc-label">Despesas</div><div class="mc-value">R$ 38K</div></div>
            <div class="mockup-card"><div class="mc-icon blue">📈</div><div class="mc-label">Lucro</div><div class="mc-value">R$ 86K</div></div>
        </div>
    </div>
</section>

<div class="logos-section">
    <div class="logos-inner">
        <div class="logos-label">Confiado por +2.000 empresas</div>
        <div class="logo-item">Mercado Pago</div>
        <div class="logo-item">PagSeguro</div>
        <div class="logo-item">Cielo</div>
        <div class="logo-item">Itaú</div>
        <div class="logo-item">Bradesco</div>
    </div>
</div>

<section class="features-section">
    <div class="section-center">
        <div class="chip">● Nosso Fluxo</div>
        <div class="section-title">Como nossa plataforma<br>torna seu fluxo <span style="background:linear-gradient(135deg,var(--purple),var(--pink));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">mais fácil</span></div>
        <div class="section-sub">Ferramentas poderosas que simplificam cada etapa da sua gestão financeira.</div>
    </div>
    <div class="features-bento">
        <div class="bento-card span2">
            <div class="bento-icon p">📊</div>
            <div class="bento-title">Dashboard Completo em Tempo Real</div>
            <div class="bento-desc">Visualize todas as suas métricas financeiras em um único painel. Receitas, despesas, fluxo de caixa e projeções — tudo atualizado em tempo real.</div>
            <div class="bento-stat purple">+87%</div>
            <div style="color:var(--muted);font-size:0.8rem;">de aumento em eficiência operacional</div>
        </div>
        <div class="bento-card">
            <div class="bento-icon g">🔗</div>
            <div class="bento-title">Integração Bancária Total</div>
            <div class="bento-desc">Conecte todas as suas contas bancárias, cartões de crédito e investimentos em minutos.</div>
        </div>
        <div class="bento-card">
            <div class="bento-icon b">🤖</div>
            <div class="bento-title">IA Preditiva</div>
            <div class="bento-desc">Nossa IA analisa seus dados e prevê seu fluxo de caixa para os próximos meses.</div>
        </div>
        <div class="bento-card">
            <div class="bento-icon pk">📱</div>
            <div class="bento-title">App Mobile</div>
            <div class="bento-desc">Gerencie suas finanças de qualquer lugar com nosso app iOS e Android.</div>
        </div>
        <div class="bento-card">
            <div class="bento-icon p">🔒</div>
            <div class="bento-title">Segurança Bancária</div>
            <div class="bento-desc">Criptografia de nível bancário e conformidade com regulamentações do Banco Central.</div>
        </div>
        <div class="bento-card">
            <div class="bento-icon g">📋</div>
            <div class="bento-title">Relatórios Automáticos</div>
            <div class="bento-desc">Relatórios contábeis e gerenciais gerados automaticamente toda semana.</div>
        </div>
    </div>
</section>

<section class="how-section">
    <div class="section-center" style="margin-bottom:3.5rem;">
        <div class="chip" style="background:rgba(255,255,255,0.1);color:rgba(255,255,255,0.7);">● Como Funciona</div>
        <div class="section-title" style="color:white;">Comece em 3 passos simples</div>
        <div class="section-sub" style="color:rgba(255,255,255,0.5);">Setup rápido. Sem burocracia. Começe a gerenciar em minutos.</div>
    </div>
    <div class="how-grid">
        <div class="how-steps">
            <div class="how-step">
                <div class="how-num">01</div>
                <div><div class="how-title">Crie sua conta</div><div class="how-desc">Cadastro em menos de 2 minutos. Sem cartão de crédito para começar.</div></div>
            </div>
            <div class="how-step">
                <div class="how-num">02</div>
                <div><div class="how-title">Conecte suas contas</div><div class="how-desc">Vincule seus bancos e cartões de forma segura com autenticação bancária.</div></div>
            </div>
            <div class="how-step">
                <div class="how-num">03</div>
                <div><div class="how-title">Gerencie e cresça</div><div class="how-desc">Acesse insights poderosos e tome decisões financeiras com confiança.</div></div>
            </div>
        </div>
        <div class="how-visual">
            <div class="hv-title">Distribuição Financeira — Agosto 2025</div>
            <div class="hv-bar"><div class="hv-bar-label"><span>Receita Recorrente</span><span>68%</span></div><div class="hv-bar-track"><div class="hv-bar-fill" style="width:68%"></div></div></div>
            <div class="hv-bar"><div class="hv-bar-label"><span>Novas Vendas</span><span>45%</span></div><div class="hv-bar-track"><div class="hv-bar-fill" style="width:45%"></div></div></div>
            <div class="hv-bar"><div class="hv-bar-label"><span>Custos Operacionais</span><span>22%</span></div><div class="hv-bar-track"><div class="hv-bar-fill" style="width:22%;background:linear-gradient(90deg,#10b981,#34d399)"></div></div></div>
            <div class="hv-users">
                <div class="hv-user"><div class="hv-avatar" style="background:linear-gradient(135deg,#7c3aed,#ec4899)">A</div>Analítico</div>
                <div class="hv-user"><div class="hv-avatar" style="background:linear-gradient(135deg,#3b82f6,#06b6d4)">E</div>Executivo</div>
                <div class="hv-user"><div class="hv-avatar" style="background:linear-gradient(135deg,#10b981,#34d399)">C</div>Contábil</div>
            </div>
        </div>
    </div>
</section>

<section class="pricing-section">
    <div class="section-center">
        <div class="chip">● Preços</div>
        <div class="section-title">Plano ideal para<br>cada tamanho de empresa</div>
    </div>
    <div class="pricing-grid">
        <div class="price-card">
            <div class="price-name">Starter</div>
            <div class="price-amount">R$0</div>
            <div class="price-period">para sempre grátis</div>
            <ul class="price-features">
                <li><span class="check">✓</span> Até 3 contas bancárias</li>
                <li><span class="check">✓</span> Dashboard básico</li>
                <li><span class="check">✓</span> Relatórios mensais</li>
                <li><span class="check">✓</span> Suporte por email</li>
            </ul>
            <a href="#" class="price-btn price-btn-outline">Começar Grátis</a>
        </div>
        <div class="price-card featured">
            <div class="price-chip">⭐ MAIS POPULAR</div>
            <div class="price-name">Business</div>
            <div class="price-amount">R$249</div>
            <div class="price-period">/mês · cancele quando quiser</div>
            <ul class="price-features">
                <li><span class="check">✓</span> Contas ilimitadas</li>
                <li><span class="check">✓</span> IA preditiva inclusa</li>
                <li><span class="check">✓</span> Relatórios automáticos</li>
                <li><span class="check">✓</span> App mobile completo</li>
                <li><span class="check">✓</span> Suporte prioritário 24/7</li>
            </ul>
            <a href="#" class="price-btn price-btn-white">Teste 14 dias Grátis</a>
        </div>
        <div class="price-card">
            <div class="price-name">Enterprise</div>
            <div class="price-amount">R$799</div>
            <div class="price-period">/mês · tudo incluso</div>
            <ul class="price-features">
                <li><span class="check">✓</span> Multi-empresas</li>
                <li><span class="check">✓</span> API completa</li>
                <li><span class="check">✓</span> White label</li>
                <li><span class="check">✓</span> Gerente dedicado</li>
            </ul>
            <a href="#" class="price-btn price-btn-outline">Falar com Vendas</a>
        </div>
    </div>
</section>

<section class="testimonials-section">
    <div class="section-center">
        <div class="chip">● Depoimentos</div>
        <div class="section-title">Amado por empresas<br>ao redor do Brasil</div>
    </div>
    <div class="t-grid">
        <div class="t-card">
            <div class="t-stars">★★★★★</div>
            <div class="t-text">"O FlowPay transformou como gerenciamos o financeiro. Em 2 meses economizamos 30h mensais de trabalho manual."</div>
            <div class="t-author"><div class="t-avatar">JS</div><div><div class="t-name">João Silva</div><div class="t-role">CFO, Construtora Regional</div></div></div>
        </div>
        <div class="t-card">
            <div class="t-stars">★★★★★</div>
            <div class="t-text">"A previsão de fluxo de caixa com IA nos salvou de uma crise. Detectou o problema 3 meses antes de acontecer."</div>
            <div class="t-author"><div class="t-avatar">MC</div><div><div class="t-name">Maria Costa</div><div class="t-role">CEO, Rede de Franquias</div></div></div>
        </div>
        <div class="t-card">
            <div class="t-stars">★★★★★</div>
            <div class="t-text">"Integração impecável. Conectou todos os nossos bancos em minutos. Interface linda e fácil de usar para toda equipe."</div>
            <div class="t-author"><div class="t-avatar">PR</div><div><div class="t-name">Paulo Rocha</div><div class="t-role">Diretor Financeiro, Tech Startup</div></div></div>
        </div>
    </div>
</section>

<section class="faq-section">
    <div class="section-center">
        <div class="chip">● FAQ</div>
        <div class="section-title">Perguntas Frequentes</div>
    </div>
    <div class="faq-item"><div class="faq-q">💜 Os meus dados financeiros estão seguros?</div><div class="faq-a">Sim! Usamos criptografia AES-256, autenticação de dois fatores e somos certificados pelo Banco Central do Brasil. Seus dados nunca são compartilhados com terceiros.</div></div>
    <div class="faq-item"><div class="faq-q">💜 Quais bancos são suportados?</div><div class="faq-a">Integramos com mais de 40 bancos brasileiros, incluindo Itaú, Bradesco, Santander, Nubank, Inter, C6 e todos os bancos do Open Finance.</div></div>
    <div class="faq-item"><div class="faq-q">💜 Posso cancelar a qualquer momento?</div><div class="faq-a">Sim, sem multas ou contratos longos. Cancele com um clique. Você mantém acesso até o final do período pago.</div></div>
    <div class="faq-item"><div class="faq-q">💜 O plano Business tem limite de usuários?</div><div class="faq-a">O Business inclui até 10 usuários. Para equipes maiores, o plano Enterprise oferece usuários ilimitados.</div></div>
</section>

<div class="cta-section">
    <h2>Pronto para dominar<br>suas finanças?</h2>
    <p>Junte-se a mais de 2.000 empresas que já escolheram o FlowPay.</p>
    <a href="#" class="btn-white">Começar Gratuitamente →</a>
</div>

<footer class="footer">
    <div class="footer-logo"><div class="footer-logo-icon">💜</div> FlowPay</div>
    <div class="footer-links"><a href="#">Privacidade</a><a href="#">Termos</a><a href="#">Blog</a><a href="#">Contato</a></div>
    <div class="footer-copy">© 2025 FlowPay. Todos os direitos reservados.</div>
</footer>
""", unsafe_allow_html=True)
