import streamlit as st

st.set_page_config(page_title="Estrutura Forte - Construção Civil", page_icon="🏗️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');

:root {
    --yellow: #f59e0b;
    --yellow-light: #fef3c7;
    --dark: #111827;
    --darker: #0a0f1a;
    --mid: #1f2937;
    --muted: #9ca3af;
    --white: #f9fafb;
    --border: #374151;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html, body, [data-testid="stAppViewContainer"] {
    background: var(--darker) !important;
    color: var(--white) !important;
    font-family: 'Inter', sans-serif;
}
[data-testid="stHeader"] { display: none; }
[data-testid="stSidebar"] { display: none; }
.main .block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stVerticalBlock"] { gap: 0 !important; }

/* NAV */
.nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 999;
    display: flex; align-items: center; justify-content: space-between;
    padding: 1.2rem 5%;
    background: rgba(10,15,26,0.95); backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--border);
}
.nav-logo { display: flex; align-items: center; gap: 0.75rem; }
.nav-logo-icon { background: var(--yellow); color: var(--dark); width: 36px; height: 36px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1rem; }
.nav-logo-text { font-family: 'Oswald', sans-serif; font-size: 1.1rem; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; }
.nav-links { display: flex; gap: 2rem; }
.nav-links a { color: var(--muted); text-decoration: none; font-size: 0.875rem; font-weight: 500; transition: color 0.3s; }
.nav-links a:hover { color: var(--yellow); }
.nav-cta { background: var(--yellow); color: var(--dark); padding: 0.7rem 1.8rem; border-radius: 6px; font-weight: 600; font-size: 0.875rem; text-decoration: none; font-family: 'Oswald', sans-serif; letter-spacing: 0.5px; text-transform: uppercase; }

/* HERO */
.hero {
    min-height: 100vh;
    padding: 8rem 5% 5rem;
    display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 4rem; align-items: center;
    background: linear-gradient(135deg, var(--darker) 0%, var(--dark) 100%);
    position: relative; overflow: hidden;
}
.hero::before {
    content: ''; position: absolute; bottom: 0; right: 0;
    width: 50%; height: 100%;
    background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23f59e0b' fill-opacity='0.04'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}
.hero-eyebrow { display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1.5rem; }
.hero-line { width: 40px; height: 2px; background: var(--yellow); }
.hero-label { color: var(--yellow); font-size: 0.8rem; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; }
.hero h1 {
    font-family: 'Oswald', sans-serif;
    font-size: clamp(3rem, 5.5vw, 5.5rem);
    font-weight: 700; line-height: 1.05;
    color: var(--white); text-transform: uppercase;
    letter-spacing: 1px; margin-bottom: 1.5rem;
}
.hero h1 span { color: var(--yellow); }
.hero p { color: var(--muted); font-size: 1rem; line-height: 1.8; margin-bottom: 2.5rem; max-width: 480px; }
.hero-btns { display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 3rem; }
.btn-yellow { background: var(--yellow); color: var(--dark); padding: 0.9rem 2rem; border-radius: 6px; font-weight: 700; font-size: 0.95rem; text-decoration: none; font-family: 'Oswald', sans-serif; text-transform: uppercase; letter-spacing: 0.5px; transition: all 0.3s; }
.btn-yellow:hover { background: #d97706; transform: translateY(-2px); }
.btn-outline-y { background: transparent; color: var(--yellow); border: 1px solid var(--yellow); padding: 0.9rem 2rem; border-radius: 6px; font-weight: 700; font-size: 0.95rem; text-decoration: none; font-family: 'Oswald', sans-serif; text-transform: uppercase; letter-spacing: 0.5px; transition: all 0.3s; }
.btn-outline-y:hover { background: rgba(245,158,11,0.1); }
.hero-numbers { display: flex; gap: 2.5rem; flex-wrap: wrap; }
.h-num .num { font-family: 'Oswald', sans-serif; font-size: 2.5rem; font-weight: 700; color: var(--yellow); }
.h-num .label { color: var(--muted); font-size: 0.8rem; }

.hero-right { position: relative; }
.hero-visual-card {
    background: var(--mid); border: 1px solid var(--border); border-radius: 16px;
    overflow: hidden;
}
.hvc-img { height: 280px; background: linear-gradient(135deg, #1f2937, #374151); display: flex; align-items: center; justify-content: center; font-size: 4rem; position: relative; }
.hvc-content { padding: 2rem; }
.hvc-title { font-family: 'Oswald', sans-serif; font-size: 1.3rem; font-weight: 600; text-transform: uppercase; margin-bottom: 0.75rem; }
.hvc-checks { display: flex; flex-direction: column; gap: 0.5rem; }
.hvc-check { display: flex; align-items: center; gap: 0.75rem; font-size: 0.875rem; color: var(--muted); }
.check-dot { width: 18px; height: 18px; border-radius: 50%; background: var(--yellow); display: flex; align-items: center; justify-content: center; font-size: 0.6rem; color: var(--dark); font-weight: 700; flex-shrink: 0; }
.exp-badge { position: absolute; top: -20px; right: -20px; background: var(--yellow); color: var(--dark); border-radius: 50%; width: 90px; height: 90px; display: flex; flex-direction: column; align-items: center; justify-content: center; font-family: 'Oswald', sans-serif; font-weight: 700; text-align: center; }
.exp-badge .num { font-size: 1.8rem; line-height: 1; }
.exp-badge .text { font-size: 0.55rem; text-transform: uppercase; letter-spacing: 1px; }

/* RIBBON */
.ribbon { background: var(--yellow); padding: 1rem 5%; display: flex; align-items: center; justify-content: center; gap: 4rem; flex-wrap: wrap; }
.ribbon-item { display: flex; align-items: center; gap: 0.75rem; }
.ribbon-icon { font-size: 1.2rem; }
.ribbon-text { font-family: 'Oswald', sans-serif; font-size: 0.9rem; font-weight: 600; color: var(--dark); text-transform: uppercase; letter-spacing: 0.5px; }

/* ABOUT */
.about-section { padding: 6rem 5%; display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; align-items: center; }
.about-left .section-eyebrow { display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1.5rem; }
.about-left h2 { font-family: 'Oswald', sans-serif; font-size: clamp(2rem, 3.5vw, 3rem); font-weight: 700; text-transform: uppercase; line-height: 1.1; margin-bottom: 1.5rem; }
.about-left h2 span { color: var(--yellow); }
.about-left p { color: var(--muted); line-height: 1.8; margin-bottom: 1.5rem; }
.about-checks { display: flex; flex-direction: column; gap: 1rem; margin-bottom: 2rem; }
.about-check { display: flex; align-items: flex-start; gap: 0.75rem; }
.about-check-icon { font-size: 1rem; flex-shrink: 0; color: var(--yellow); margin-top: 2px; }
.about-check-text strong { display: block; font-size: 0.9rem; margin-bottom: 0.2rem; }
.about-check-text span { color: var(--muted); font-size: 0.85rem; }
.about-right { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.about-img-main { background: var(--mid); border: 1px solid var(--border); border-radius: 12px; aspect-ratio: 1; display: flex; align-items: center; justify-content: center; font-size: 3rem; grid-column: 1/-1; }
.about-stat { background: var(--mid); border: 1px solid var(--border); border-radius: 12px; padding: 1.5rem; }
.about-stat.yellow { background: var(--yellow); border-color: transparent; }
.about-stat.yellow .num { color: var(--dark); }
.about-stat.yellow .label { color: rgba(0,0,0,0.6); }
.about-stat .num { font-family: 'Oswald', sans-serif; font-size: 2rem; font-weight: 700; color: var(--yellow); }
.about-stat .label { color: var(--muted); font-size: 0.8rem; }

/* SERVICES */
.services-section { padding: 6rem 5%; }
.section-header { text-align: center; margin-bottom: 4rem; }
.section-header h2 { font-family: 'Oswald', sans-serif; font-size: clamp(2rem, 3.5vw, 3rem); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
.section-header h2 span { color: var(--yellow); }
.section-header p { color: var(--muted); margin-top: 1rem; }
.services-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
.service-card { background: var(--mid); border: 1px solid var(--border); border-radius: 12px; padding: 2.5rem; transition: all 0.3s; cursor: pointer; }
.service-card:hover { border-color: var(--yellow); transform: translateY(-4px); }
.service-icon { font-size: 2.5rem; margin-bottom: 1.5rem; }
.service-title { font-family: 'Oswald', sans-serif; font-size: 1.3rem; text-transform: uppercase; margin-bottom: 0.75rem; letter-spacing: 0.5px; }
.service-desc { color: var(--muted); font-size: 0.875rem; line-height: 1.7; margin-bottom: 1.5rem; }
.service-link { color: var(--yellow); font-size: 0.875rem; font-weight: 600; text-decoration: none; display: flex; align-items: center; gap: 0.5rem; }

/* TESTIMONIALS */
.testimonials-section { padding: 6rem 5%; background: var(--dark); }
.testimonials-layout { display: grid; grid-template-columns: 1fr 2fr; gap: 4rem; align-items: start; }
.t-left h2 { font-family: 'Oswald', sans-serif; font-size: clamp(1.8rem, 3vw, 2.5rem); font-weight: 700; text-transform: uppercase; line-height: 1.2; margin-bottom: 1rem; }
.t-left h2 span { color: var(--yellow); }
.t-left p { color: var(--muted); font-size: 0.9rem; line-height: 1.7; margin-bottom: 2rem; }
.t-stats { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.t-stat { background: var(--mid); border: 1px solid var(--border); border-radius: 10px; padding: 1.2rem; }
.t-stat .num { font-family: 'Oswald', sans-serif; font-size: 1.8rem; font-weight: 700; color: var(--yellow); }
.t-stat .label { color: var(--muted); font-size: 0.8rem; }
.t-right { display: flex; flex-direction: column; gap: 1.5rem; }
.t-card { background: var(--mid); border: 1px solid var(--border); border-radius: 12px; padding: 2rem; display: flex; gap: 1.5rem; }
.t-av { width: 48px; height: 48px; border-radius: 50%; background: linear-gradient(135deg, var(--yellow), #d97706); display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1rem; color: var(--dark); flex-shrink: 0; }
.t-body .t-name { font-weight: 600; font-size: 0.95rem; margin-bottom: 0.2rem; }
.t-body .t-role { color: var(--yellow); font-size: 0.8rem; margin-bottom: 0.75rem; }
.t-body .t-text { color: var(--muted); font-size: 0.875rem; line-height: 1.7; }

/* NEWS */
.news-section { padding: 6rem 5%; }
.news-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 3rem; }
.news-header h2 { font-family: 'Oswald', sans-serif; font-size: clamp(1.8rem, 3vw, 2.5rem); font-weight: 700; text-transform: uppercase; }
.news-header a { color: var(--yellow); text-decoration: none; font-size: 0.875rem; font-weight: 600; display: flex; align-items: center; gap: 0.5rem; }
.news-grid { display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 1.5rem; }
.news-card { background: var(--mid); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; }
.news-img { height: 200px; display: flex; align-items: center; justify-content: center; font-size: 3rem; }
.news-img.big { height: 300px; }
.ni-1 { background: linear-gradient(135deg, #1f2937, #374151); }
.ni-2 { background: linear-gradient(135deg, #1c1917, #292524); }
.ni-3 { background: linear-gradient(135deg, #0f172a, #1e293b); }
.news-body { padding: 1.5rem; }
.news-cat { color: var(--yellow); font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.5rem; }
.news-title { font-weight: 600; font-size: 0.95rem; line-height: 1.5; margin-bottom: 0.75rem; }
.news-meta { color: var(--muted); font-size: 0.8rem; }

/* CTA */
.cta-section { padding: 6rem 5%; text-align: center; background: var(--mid); border-top: 1px solid var(--border); }
.cta-section h2 { font-family: 'Oswald', sans-serif; font-size: clamp(2.5rem, 5vw, 4rem); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 1rem; }
.cta-section h2 span { color: var(--yellow); }
.cta-section p { color: var(--muted); margin-bottom: 2.5rem; }

/* FOOTER */
.footer { background: var(--darker); border-top: 1px solid var(--border); padding: 4rem 5%; }
.footer-top { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 3rem; margin-bottom: 3rem; }
.footer-brand p { color: var(--muted); font-size: 0.875rem; line-height: 1.7; margin-top: 1rem; }
.footer-col h4 { font-family: 'Oswald', sans-serif; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; color: var(--yellow); margin-bottom: 1rem; }
.footer-col ul { list-style: none; display: flex; flex-direction: column; gap: 0.5rem; }
.footer-col ul a { color: var(--muted); text-decoration: none; font-size: 0.875rem; transition: color 0.3s; }
.footer-col ul a:hover { color: var(--yellow); }
.footer-bottom { border-top: 1px solid var(--border); padding-top: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; }
.footer-copy { color: var(--muted); font-size: 0.8rem; }

@media (max-width: 900px) {
    .hero, .about-section, .testimonials-layout { grid-template-columns: 1fr; }
    .services-grid, .news-grid { grid-template-columns: 1fr; }
    .footer-top { grid-template-columns: 1fr 1fr; }
}
</style>

<nav class="nav">
    <div class="nav-logo">
        <div class="nav-logo-icon">🏗</div>
        <div class="nav-logo-text">Estrutura<span style="color:var(--yellow);"> Forte</span></div>
    </div>
    <div class="nav-links">
        <a href="#">Início</a><a href="#">Sobre</a><a href="#">Projetos</a><a href="#">Serviços</a><a href="#">Equipe</a>
    </div>
    <a href="#" class="nav-cta">Solicitar Orçamento</a>
</nav>

<section class="hero">
    <div>
        <div class="hero-eyebrow">
            <div class="hero-line"></div>
            <div class="hero-label">Construção de Alta Performance</div>
        </div>
        <h1>Construímos<br><span>Algo Novo</span><br>E Consistente.</h1>
        <p>Suas ideias e sonhos são transformados por nós em edificações duradouras e de alta engenharia. 25 anos construindo o futuro.</p>
        <div class="hero-btns">
            <a href="#" class="btn-yellow">Começar Projeto</a>
            <a href="#" class="btn-outline-y">Nossos Serviços</a>
        </div>
        <div class="hero-numbers">
            <div class="h-num"><div class="num">850+</div><div class="label">Obras entregues</div></div>
            <div class="h-num"><div class="num">25</div><div class="label">Anos de experiência</div></div>
            <div class="h-num"><div class="num">98%</div><div class="label">Clientes satisfeitos</div></div>
        </div>
    </div>
    <div class="hero-right">
        <div class="hero-visual-card">
            <div class="hvc-img">🏢</div>
            <div class="hvc-content">
                <div class="hvc-title">Padrão de Qualidade Máximo</div>
                <div class="hvc-checks">
                    <div class="hvc-check"><div class="check-dot">✓</div> Materiais certificados ABNT</div>
                    <div class="hvc-check"><div class="check-dot">✓</div> Engenheiros altamente qualificados</div>
                    <div class="hvc-check"><div class="check-dot">✓</div> Prazo garantido em contrato</div>
                </div>
            </div>
        </div>
        <div class="exp-badge" style="position:absolute;top:-20px;right:-20px;">
            <div class="num">25</div>
            <div class="text">Anos de<br>Experiência</div>
        </div>
    </div>
</section>

<div class="ribbon">
    <div class="ribbon-item"><div class="ribbon-icon">🏆</div><div class="ribbon-text">Qualidade Certificada</div></div>
    <div class="ribbon-item"><div class="ribbon-icon">⏰</div><div class="ribbon-text">Entrega no Prazo</div></div>
    <div class="ribbon-item"><div class="ribbon-icon">💎</div><div class="ribbon-text">Materiais Premium</div></div>
    <div class="ribbon-item"><div class="ribbon-icon">🛡️</div><div class="ribbon-text">Garantia de Obra</div></div>
</div>

<section class="about-section">
    <div class="about-left">
        <div class="section-eyebrow">
            <div class="hero-line"></div>
            <div class="hero-label">Sobre Nós</div>
        </div>
        <h2>Bem-vindos à <span>Solução Real</span> em Construção</h2>
        <p>Com 25 anos de experiência, a Estrutura Forte é referência em construção civil residencial e comercial. Nossa equipe de engenheiros e arquitetos transforma projetos em realidade com precisão e qualidade incomparável.</p>
        <div class="about-checks">
            <div class="about-check">
                <div class="about-check-icon">◆</div>
                <div class="about-check-text">
                    <strong>Engenharia de Alto Padrão</strong>
                    <span>Projetos executivos com cálculos estruturais rigorosos e supervisão técnica em todas as etapas.</span>
                </div>
            </div>
            <div class="about-check">
                <div class="about-check-icon">◆</div>
                <div class="about-check-text">
                    <strong>Materiais Certificados</strong>
                    <span>Utilizamos apenas materiais com certificação ABNT e fornecedores homologados.</span>
                </div>
            </div>
            <div class="about-check">
                <div class="about-check-icon">◆</div>
                <div class="about-check-text">
                    <strong>Prazo e Orçamento Garantidos</strong>
                    <span>Contratos com cláusulas de garantia de prazo e ausência de surpresas no orçamento.</span>
                </div>
            </div>
        </div>
        <a href="#" class="btn-yellow">Saiba Mais →</a>
    </div>
    <div class="about-right">
        <div class="about-img-main">🏗️</div>
        <div class="about-stat yellow"><div class="num">850+</div><div class="label">Obras concluídas</div></div>
        <div class="about-stat"><div class="num" style="color:var(--yellow)">25</div><div class="label">Anos de mercado</div></div>
    </div>
</section>

<section class="services-section">
    <div class="section-header">
        <div class="hero-label" style="display:inline-block;margin-bottom:1rem;">● Serviços</div>
        <h2>Fornecemos os Melhores <span>Serviços</span></h2>
        <p>Soluções completas em construção civil para todos os tipos de projeto</p>
    </div>
    <div class="services-grid">
        <div class="service-card">
            <div class="service-icon">🏠</div>
            <div class="service-title">Residencial</div>
            <div class="service-desc">Construção de casas e apartamentos personalizados. Do projeto à entrega, com acabamento premium e sustentabilidade.</div>
            <a href="#" class="service-link">Saiba Mais →</a>
        </div>
        <div class="service-card">
            <div class="service-icon">🏛️</div>
            <div class="service-title">Design de Interiores</div>
            <div class="service-desc">Projetos de interiores que combinam funcionalidade e estética. Ambientes únicos para cada cliente.</div>
            <a href="#" class="service-link">Saiba Mais →</a>
        </div>
        <div class="service-card">
            <div class="service-icon">🔧</div>
            <div class="service-title">Reparo Estrutural</div>
            <div class="service-desc">Diagnóstico e recuperação estrutural de edificações. Reforço e modernização com técnicas avançadas.</div>
            <a href="#" class="service-link">Saiba Mais →</a>
        </div>
        <div class="service-card">
            <div class="service-icon">🏢</div>
            <div class="service-title">Comercial</div>
            <div class="service-desc">Galpões, escritórios e empreendimentos comerciais. Projetos otimizados para produtividade e eficiência.</div>
            <a href="#" class="service-link">Saiba Mais →</a>
        </div>
        <div class="service-card">
            <div class="service-icon">🌱</div>
            <div class="service-title">Construção Verde</div>
            <div class="service-desc">Edificações sustentáveis com certificação LEED. Economia de energia e impacto ambiental reduzido.</div>
            <a href="#" class="service-link">Saiba Mais →</a>
        </div>
        <div class="service-card">
            <div class="service-icon">📐</div>
            <div class="service-title">Projetos e Laudos</div>
            <div class="service-desc">Elaboração de projetos executivos, laudos técnicos e consultoria para aprovação em órgãos municipais.</div>
            <a href="#" class="service-link">Saiba Mais →</a>
        </div>
    </div>
</section>

<section class="testimonials-section">
    <div class="testimonials-layout">
        <div class="t-left">
            <div class="hero-eyebrow" style="margin-bottom:1rem;"><div class="hero-line"></div><div class="hero-label">Depoimentos</div></div>
            <h2>O que Dizem Nossos <span>Clientes</span> Satisfeitos</h2>
            <p>Mais de 850 obras entregues e clientes que voltam projeto após projeto. Veja o que dizem sobre nosso trabalho.</p>
            <div class="t-stats">
                <div class="t-stat"><div class="num">850+</div><div class="label">Obras entregues</div></div>
                <div class="t-stat"><div class="num">98%</div><div class="label">Satisfação</div></div>
            </div>
        </div>
        <div class="t-right">
            <div class="t-card">
                <div class="t-av">LJ</div>
                <div class="t-body"><div class="t-name">Larem Jemes</div><div class="t-role">Graphic Design</div><div class="t-stars" style="color:#f59e0b;font-size:0.85rem;">★★★★★</div><div class="t-text">"A Estrutura Forte transformou nosso projeto em realidade com uma qualidade surpreendente. Prazo respeitado e acabamento impecável. Super recomendo!"</div></div>
            </div>
            <div class="t-card">
                <div class="t-av">JM</div>
                <div class="t-body"><div class="t-name">Johan Mickel</div><div class="t-role">Web Development</div><div class="t-stars" style="color:#f59e0b;font-size:0.85rem;">★★★★★</div><div class="t-text">"Equipe extremamente profissional e comprometida. O resultado final superou todas as nossas expectativas. Com certeza voltarei para o próximo projeto."</div></div>
            </div>
        </div>
    </div>
</section>

<section class="news-section">
    <div class="news-header">
        <h2>Últimas Notícias e Histórias</h2>
        <a href="#">Ver Todas →</a>
    </div>
    <div class="news-grid">
        <div class="news-card">
            <div class="news-img big ni-1">🏗️</div>
            <div class="news-body"><div class="news-cat">Projetos</div><div class="news-title">Novo complexo residencial entregue: 200 unidades de alto padrão</div><div class="news-meta">15 Jan 2025 · 5 min leitura</div></div>
        </div>
        <div class="news-card">
            <div class="news-img ni-2">🔧</div>
            <div class="news-body"><div class="news-cat">Tecnologia</div><div class="news-title">Inovações em construção sustentável</div><div class="news-meta">10 Jan 2025</div></div>
        </div>
        <div class="news-card">
            <div class="news-img ni-3">📊</div>
            <div class="news-body"><div class="news-cat">Mercado</div><div class="news-title">Setor de construção cresce 12% em 2024</div><div class="news-meta">5 Jan 2025</div></div>
        </div>
    </div>
</section>

<section class="cta-section">
    <h2>Vamos Construir <span>Juntos</span>?</h2>
    <p>Entre em contato e solicite seu orçamento gratuito. Atendemos em todo o Brasil.</p>
    <a href="#" class="btn-yellow" style="font-size:1rem;padding:1rem 2.5rem;">Solicitar Orçamento Gratuito →</a>
</section>

<footer class="footer">
    <div class="footer-top">
        <div class="footer-brand">
            <div class="nav-logo"><div class="nav-logo-icon">🏗</div><div class="nav-logo-text">Estrutura<span style="color:var(--yellow);"> Forte</span></div></div>
            <p>Construindo sonhos com qualidade, segurança e compromisso desde 2000. Sua obra em boas mãos.</p>
        </div>
        <div class="footer-col"><h4>Empresa</h4><ul><li><a href="#">Início</a></li><li><a href="#">Sobre</a></li><li><a href="#">Projetos</a></li><li><a href="#">Equipe</a></li></ul></div>
        <div class="footer-col"><h4>Serviços</h4><ul><li><a href="#">Residencial</a></li><li><a href="#">Comercial</a></li><li><a href="#">Interiores</a></li><li><a href="#">Estrutural</a></li></ul></div>
        <div class="footer-col"><h4>Contato</h4><ul><li><a href="#">WhatsApp</a></li><li><a href="#">Email</a></li><li><a href="#">Instagram</a></li><li><a href="#">LinkedIn</a></li></ul></div>
    </div>
    <div class="footer-bottom">
        <div class="footer-copy">© 2025 Estrutura Forte. Todos os direitos reservados.</div>
        <div class="footer-copy">CREA-SP 123456</div>
    </div>
</footer>
""", unsafe_allow_html=True)
