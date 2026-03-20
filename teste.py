import streamlit as st

st.set_page_config(page_title="FORMA Studio - Agência de Design", page_icon="◼", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --white: #ffffff;
    --off-white: #f5f2ee;
    --black: #0a0a0a;
    --dark-gray: #1a1a1a;
    --mid-gray: #6b6b6b;
    --light-gray: #e8e4df;
    --accent: #c9a96e;
    --accent-dark: #a8854a;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html, body, [data-testid="stAppViewContainer"] {
    background: var(--off-white) !important;
    color: var(--black) !important;
    font-family: 'DM Sans', sans-serif;
}
[data-testid="stHeader"] { display: none; }
[data-testid="stSidebar"] { display: none; }
.main .block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stVerticalBlock"] { gap: 0 !important; }

/* NAV */
.nav {
    position: fixed; top: 0; left: 0; right: 0; z-index: 999;
    display: flex; align-items: center; justify-content: space-between;
    padding: 1.5rem 6%;
    background: rgba(245,242,238,0.92);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--light-gray);
}
.nav-logo { font-family: 'Playfair Display', serif; font-size: 1.4rem; color: var(--black); font-weight: 900; letter-spacing: -0.5px; }
.nav-links { display: flex; gap: 2.5rem; }
.nav-links a { color: var(--mid-gray); text-decoration: none; font-size: 0.9rem; font-weight: 500; transition: color 0.3s; letter-spacing: 0.5px; }
.nav-links a:hover { color: var(--black); }
.nav-cta {
    background: var(--black); color: var(--white);
    padding: 0.7rem 1.8rem; border-radius: 50px;
    font-size: 0.875rem; font-weight: 600; text-decoration: none;
    transition: all 0.3s;
}
.nav-cta:hover { background: var(--accent); }

/* HERO */
.hero {
    min-height: 100vh;
    padding: 10rem 6% 6rem;
    display: grid; grid-template-columns: 1fr 1fr;
    gap: 4rem; align-items: center;
    position: relative;
}
.hero-text-block {}
.hero-pretitle {
    display: inline-block;
    background: var(--black); color: var(--white);
    padding: 0.35rem 1rem; border-radius: 4px;
    font-size: 0.75rem; font-weight: 600; letter-spacing: 2px; text-transform: uppercase;
    margin-bottom: 2rem;
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 5.5vw, 5.5rem);
    font-weight: 900;
    line-height: 1.05;
    color: var(--black);
    margin-bottom: 1.5rem;
}
.hero h1 em { font-style: italic; color: var(--accent); }
.hero p { color: var(--mid-gray); font-size: 1.05rem; line-height: 1.75; margin-bottom: 2.5rem; max-width: 460px; }
.hero-btns { display: flex; gap: 1rem; align-items: center; flex-wrap: wrap; }
.btn-black {
    background: var(--black); color: var(--white);
    padding: 0.9rem 2rem; border-radius: 50px; font-weight: 600; font-size: 0.95rem;
    text-decoration: none; transition: all 0.3s;
}
.btn-black:hover { background: var(--accent); transform: translateY(-2px); }
.btn-text { color: var(--black); text-decoration: none; font-size: 0.9rem; font-weight: 500; display: flex; align-items: center; gap: 0.5rem; }

.hero-visual {
    position: relative;
}
.hero-img-main {
    background: var(--black);
    border-radius: 20px; padding: 3rem;
    aspect-ratio: 4/5;
    display: flex; align-items: flex-end;
    position: relative; overflow: hidden;
}
.hero-img-overlay {
    position: absolute; inset: 0;
    background: linear-gradient(135deg, #1a1a1a 0%, #3d3d3d 50%, #1a1a1a 100%);
    display: flex; align-items: center; justify-content: center;
    font-family: 'Playfair Display', serif; font-size: 5rem; font-weight: 900;
    color: rgba(255,255,255,0.05);
    letter-spacing: -3px;
}
.hero-img-text {
    position: relative; z-index: 2;
    background: var(--accent); color: var(--white);
    padding: 1.5rem 2rem; border-radius: 12px; width: 100%;
}
.hero-img-text .stat-big { font-size: 2.5rem; font-weight: 700; font-family: 'Playfair Display', serif; }
.hero-img-text .stat-desc { font-size: 0.85rem; opacity: 0.8; }

.hero-badge-float {
    position: absolute; top: 20%; right: -30px;
    background: var(--white); border-radius: 12px; padding: 1.2rem 1.5rem;
    box-shadow: 0 20px 60px rgba(0,0,0,0.1);
    font-size: 0.85rem; font-weight: 600; color: var(--black);
    border: 1px solid var(--light-gray);
}
.hero-badge-num { font-family: 'Playfair Display', serif; font-size: 2rem; font-weight: 900; color: var(--accent); }

/* LOGOS */
.logos-section { padding: 2.5rem 6%; border-top: 1px solid var(--light-gray); background: var(--white); }
.logos-inner { display: flex; align-items: center; gap: 4rem; flex-wrap: wrap; }
.logos-label { color: var(--mid-gray); font-size: 0.8rem; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; white-space: nowrap; }
.logos-brands { display: flex; gap: 3rem; flex-wrap: wrap; align-items: center; }
.brand-name { font-weight: 700; font-size: 0.95rem; color: var(--light-gray); }

/* ABOUT */
.about-section { padding: 8rem 6%; display: grid; grid-template-columns: 1fr 1fr; gap: 6rem; align-items: center; }
.about-img {
    background: var(--black); border-radius: 20px; aspect-ratio: 3/4;
    display: flex; align-items: center; justify-content: center; overflow: hidden; position: relative;
}
.about-img-pattern {
    position: absolute; inset: 0;
    background: repeating-linear-gradient(45deg, transparent, transparent 10px, rgba(201,169,110,0.05) 10px, rgba(201,169,110,0.05) 20px);
}
.about-img-content { position: relative; z-index: 2; text-align: center; }
.about-img-content .big-num { font-family: 'Playfair Display', serif; font-size: 5rem; font-weight: 900; color: var(--accent); line-height: 1; }
.about-img-content .big-label { color: rgba(255,255,255,0.6); font-size: 0.85rem; letter-spacing: 2px; text-transform: uppercase; }

.about-label { font-size: 0.75rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--accent); margin-bottom: 1rem; }
.about h2 { font-family: 'Playfair Display', serif; font-size: clamp(2rem, 3.5vw, 3rem); font-weight: 900; line-height: 1.2; margin-bottom: 1.5rem; }
.about p { color: var(--mid-gray); line-height: 1.8; margin-bottom: 1.5rem; }
.about-stat-row { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-top: 2rem; }
.about-stat { background: var(--off-white); border-radius: 12px; padding: 1.5rem; }
.about-stat .num { font-family: 'Playfair Display', serif; font-size: 2.5rem; font-weight: 900; color: var(--black); }
.about-stat .label { color: var(--mid-gray); font-size: 0.85rem; }

/* SERVICES */
.services-section { padding: 8rem 6%; background: var(--black); color: var(--white); }
.services-header { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 4rem; flex-wrap: wrap; gap: 2rem; }
.services-header h2 { font-family: 'Playfair Display', serif; font-size: clamp(2.5rem, 4vw, 3.5rem); font-weight: 900; line-height: 1.1; }
.services-header h2 em { font-style: italic; color: var(--accent); }
.services-header p { color: rgba(255,255,255,0.5); max-width: 340px; line-height: 1.7; }
.services-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; background: rgba(255,255,255,0.08); border-radius: 16px; overflow: hidden; }
.service-item { background: var(--dark-gray); padding: 2.5rem; transition: all 0.3s; }
.service-item:hover { background: rgba(201,169,110,0.1); }
.service-num { font-family: 'Playfair Display', serif; font-size: 3rem; font-weight: 900; color: rgba(255,255,255,0.07); margin-bottom: 1.5rem; }
.service-icon { font-size: 1.5rem; margin-bottom: 1rem; }
.service-title { font-size: 1.1rem; font-weight: 700; margin-bottom: 0.75rem; }
.service-desc { color: rgba(255,255,255,0.5); font-size: 0.9rem; line-height: 1.7; margin-bottom: 1.5rem; }
.service-tags { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.service-tag { background: rgba(255,255,255,0.06); color: rgba(255,255,255,0.5); padding: 0.25rem 0.75rem; border-radius: 50px; font-size: 0.75rem; }

/* PROCESS */
.process-section { padding: 8rem 6%; }
.process-header { text-align: center; margin-bottom: 5rem; }
.process-header h2 { font-family: 'Playfair Display', serif; font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 900; margin-bottom: 1rem; }
.process-header p { color: var(--mid-gray); max-width: 500px; margin: 0 auto; line-height: 1.7; }
.process-steps { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; position: relative; }
.process-steps::before {
    content: ''; position: absolute; top: 2rem; left: 10%; right: 10%;
    height: 1px; background: var(--light-gray);
}
.process-step { text-align: center; }
.step-num {
    width: 4rem; height: 4rem; border-radius: 50%;
    background: var(--black); color: var(--white);
    display: flex; align-items: center; justify-content: center;
    font-family: 'Playfair Display', serif; font-size: 1.2rem; font-weight: 900;
    margin: 0 auto 1.5rem; position: relative; z-index: 2;
}
.step-num.accent { background: var(--accent); }
.step-title { font-weight: 700; margin-bottom: 0.75rem; font-size: 1rem; }
.step-desc { color: var(--mid-gray); font-size: 0.875rem; line-height: 1.7; }

/* PORTFOLIO */
.portfolio-section { padding: 8rem 6%; background: var(--black); }
.portfolio-header { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 3rem; }
.portfolio-header h2 { font-family: 'Playfair Display', serif; font-size: clamp(2rem, 4vw, 3rem); font-weight: 900; color: var(--white); }
.portfolio-header a { color: var(--accent); text-decoration: none; font-size: 0.9rem; font-weight: 600; }
.portfolio-grid { display: grid; grid-template-columns: 2fr 1fr; gap: 1.5rem; }
.portfolio-item { border-radius: 16px; overflow: hidden; position: relative; }
.portfolio-img { aspect-ratio: 16/9; display: flex; align-items: center; justify-content: center; font-size: 3rem; }
.portfolio-img-tall { aspect-ratio: 3/4; display: flex; align-items: center; justify-content: center; font-size: 3rem; }
.p1 { background: linear-gradient(135deg, #2d2d2d, #4a4a4a); }
.p2 { background: linear-gradient(135deg, #1a2744, #2d4a8a); }
.portfolio-overlay {
    position: absolute; inset: 0; background: rgba(0,0,0,0.7);
    display: flex; flex-direction: column; justify-content: flex-end; padding: 2rem;
    opacity: 0; transition: opacity 0.3s;
}
.portfolio-item:hover .portfolio-overlay { opacity: 1; }
.portfolio-cat { color: var(--accent); font-size: 0.75rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 0.5rem; }
.portfolio-name { color: var(--white); font-weight: 700; font-size: 1.1rem; }

/* TESTIMONIALS */
.testimonials-section { padding: 8rem 6%; }
.testimonial-big {
    background: var(--black); color: var(--white); border-radius: 24px; padding: 4rem;
    display: grid; grid-template-columns: 1fr auto; gap: 3rem; align-items: center;
    margin-bottom: 2rem;
}
.testimonial-big-text { font-family: 'Playfair Display', serif; font-size: clamp(1.3rem, 2.5vw, 2rem); font-weight: 400; line-height: 1.5; font-style: italic; }
.testimonial-big-text em { color: var(--accent); font-style: normal; font-weight: 700; }
.testimonial-author-big { text-align: right; white-space: nowrap; }
.author-name-big { font-weight: 700; font-size: 1rem; }
.author-role-big { color: rgba(255,255,255,0.5); font-size: 0.85rem; margin-top: 0.25rem; }
.testimonials-small { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
.testimonial-small { background: var(--off-white); border-radius: 16px; padding: 2rem; }
.t-quote { font-size: 2rem; color: var(--accent); line-height: 1; margin-bottom: 1rem; font-family: Georgia; }
.t-text { color: var(--mid-gray); font-size: 0.9rem; line-height: 1.7; margin-bottom: 1.5rem; font-style: italic; }
.t-author { font-weight: 700; font-size: 0.875rem; }
.t-role { color: var(--mid-gray); font-size: 0.8rem; }

/* FAQ */
.faq-section { padding: 8rem 6%; background: var(--black); color: var(--white); }
.faq-grid { display: grid; grid-template-columns: 1fr 2fr; gap: 6rem; }
.faq-left h2 { font-family: 'Playfair Display', serif; font-size: clamp(2.5rem, 4vw, 3.5rem); font-weight: 900; line-height: 1.1; }
.faq-left h2 em { font-style: italic; color: var(--accent); }
.faq-left p { color: rgba(255,255,255,0.5); margin-top: 1.5rem; line-height: 1.7; }
.faq-items { display: flex; flex-direction: column; gap: 0; }
.faq-item { border-bottom: 1px solid rgba(255,255,255,0.1); padding: 1.5rem 0; }
.faq-q { font-weight: 600; color: var(--white); margin-bottom: 0.75rem; display: flex; justify-content: space-between; align-items: center; }
.faq-q::after { content: '↓'; color: var(--accent); }
.faq-a { color: rgba(255,255,255,0.5); font-size: 0.9rem; line-height: 1.8; }

/* CTA */
.cta-section {
    padding: 8rem 6%; text-align: center;
    background: var(--off-white);
}
.cta-section h2 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 6vw, 5rem); font-weight: 900; line-height: 1.05;
    margin-bottom: 1.5rem;
}
.cta-section h2 em { font-style: italic; color: var(--accent); }
.cta-section p { color: var(--mid-gray); font-size: 1.05rem; margin-bottom: 2.5rem; }

/* FOOTER */
.footer { padding: 3rem 6%; background: var(--black); color: var(--white); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; }
.footer-logo { font-family: 'Playfair Display', serif; font-size: 1.4rem; font-weight: 900; }
.footer-links { display: flex; gap: 2rem; }
.footer-links a { color: rgba(255,255,255,0.4); text-decoration: none; font-size: 0.85rem; transition: color 0.3s; }
.footer-links a:hover { color: var(--accent); }
.footer-copy { color: rgba(255,255,255,0.3); font-size: 0.8rem; }

@media (max-width: 900px) {
    .hero, .about-section { grid-template-columns: 1fr; }
    .services-grid, .process-steps, .portfolio-grid { grid-template-columns: 1fr; }
    .testimonials-small { grid-template-columns: 1fr; }
    .faq-grid { grid-template-columns: 1fr; }
    .testimonial-big { grid-template-columns: 1fr; }
}
</style>

<nav class="nav">
    <div class="nav-logo">FORMA<span style="color:var(--accent);">.</span></div>
    <div class="nav-links">
        <a href="#">Sobre</a>
        <a href="#">Serviços</a>
        <a href="#">Portfólio</a>
        <a href="#">Contato</a>
    </div>
    <a href="#" class="nav-cta">Iniciar Projeto</a>
</nav>

<section class="hero">
    <div class="hero-text-block">
        <div class="hero-pretitle">✦ Agência de Design Premium</div>
        <h1>Criamos Marcas<br>que <em>Imprimem</em><br>na Memória</h1>
        <p>Somos parceiros de criação para empresas que entendem que design excepcional não é custo — é vantagem competitiva.</p>
        <div class="hero-btns">
            <a href="#" class="btn-black">Iniciar Projeto →</a>
            <a href="#" class="btn-text">Ver Portfólio ↗</a>
        </div>
    </div>
    <div class="hero-visual">
        <div class="hero-img-main">
            <div class="hero-img-overlay">FORMA</div>
            <div class="hero-img-text">
                <div class="stat-big">250+</div>
                <div class="stat-desc">Projetos entregues com sucesso</div>
            </div>
        </div>
        <div class="hero-badge-float">
            <div class="hero-badge-num">40%</div>
            <div style="font-size:0.8rem;color:var(--mid-gray);">Crescimento médio<br>de receita dos clientes</div>
        </div>
    </div>
</section>

<div class="logos-section">
    <div class="logos-inner">
        <div class="logos-label">Parceiros que confiam</div>
        <div class="logos-brands">
            <div class="brand-name">Natura</div>
            <div class="brand-name">XP Inc.</div>
            <div class="brand-name">Magazine Luiza</div>
            <div class="brand-name">Nubank</div>
            <div class="brand-name">iFood</div>
        </div>
    </div>
</div>

<section class="about-section">
    <div class="about-img">
        <div class="about-img-pattern"></div>
        <div class="about-img-content">
            <div class="big-num">8</div>
            <div class="big-label">anos de mercado</div>
        </div>
    </div>
    <div class="about">
        <div class="about-label">● Sobre a FORMA</div>
        <h2>Seus Parceiros de<br>Design Estratégico</h2>
        <p>Não somos apenas designers — somos estrategistas visuais. Na FORMA, vivemos e respiramos design, da identidade visual à experiência digital.</p>
        <p>Pensamos em cada pixel como uma decisão de negócio. Cada projeto começa com entendimento profundo do seu público e termina com resultados mensuráveis.</p>
        <div class="about-stat-row">
            <div class="about-stat">
                <div class="num">250+</div>
                <div class="label">Projetos entregues</div>
            </div>
            <div class="about-stat">
                <div class="num">98%</div>
                <div class="label">Taxa de satisfação</div>
            </div>
        </div>
    </div>
</section>

<section class="services-section">
    <div class="services-header">
        <h2>O que<br>fazemos <em>muito</em><br>bem</h2>
        <p>Cada serviço é entregue com precisão cirúrgica e atenção obsessiva aos detalhes.</p>
    </div>
    <div class="services-grid">
        <div class="service-item">
            <div class="service-num">01</div>
            <div class="service-icon">◼</div>
            <div class="service-title">Identidade de Marca</div>
            <div class="service-desc">Criamos marcas que comunicam valores, constroem autoridade e ficam na memória do consumidor.</div>
            <div class="service-tags"><span class="service-tag">Logo</span><span class="service-tag">Brandbook</span><span class="service-tag">Naming</span></div>
        </div>
        <div class="service-item">
            <div class="service-num">02</div>
            <div class="service-icon">◻</div>
            <div class="service-title">Web Design</div>
            <div class="service-desc">Sites que convertem visitantes em clientes. Design pensado para performance e experiência.</div>
            <div class="service-tags"><span class="service-tag">UX/UI</span><span class="service-tag">Landing Page</span><span class="service-tag">E-commerce</span></div>
        </div>
        <div class="service-item">
            <div class="service-num">03</div>
            <div class="service-icon">▲</div>
            <div class="service-title">Design de Produto</div>
            <div class="service-desc">Interfaces de apps e plataformas digitais que encantam usuários e geram retenção.</div>
            <div class="service-tags"><span class="service-tag">App Design</span><span class="service-tag">Prototipagem</span></div>
        </div>
        <div class="service-item">
            <div class="service-num">04</div>
            <div class="service-icon">●</div>
            <div class="service-title">Motion Design</div>
            <div class="service-desc">Animações e vídeos que comunicam sua mensagem com impacto e elegância.</div>
            <div class="service-tags"><span class="service-tag">Animação</span><span class="service-tag">Vídeo</span></div>
        </div>
        <div class="service-item">
            <div class="service-num">05</div>
            <div class="service-icon">◈</div>
            <div class="service-title">Estratégia de Marca</div>
            <div class="service-desc">Posicionamento, arquitetura de marca e identidade verbal para crescimento sustentável.</div>
            <div class="service-tags"><span class="service-tag">Posicionamento</span><span class="service-tag">Tom de voz</span></div>
        </div>
        <div class="service-item">
            <div class="service-num">06</div>
            <div class="service-icon">◉</div>
            <div class="service-title">Design Social</div>
            <div class="service-desc">Templates e sistemas visuais para redes sociais que mantêm sua marca coerente e profissional.</div>
            <div class="service-tags"><span class="service-tag">Instagram</span><span class="service-tag">LinkedIn</span></div>
        </div>
    </div>
</section>

<section class="process-section">
    <div class="process-header">
        <div class="about-label">● Como Trabalhamos</div>
        <h2>Da Ideia ao Lançamento</h2>
        <p>Nosso processo foi refinado ao longo de 8 anos para garantir resultados excepcionais com eficiência máxima.</p>
    </div>
    <div class="process-steps">
        <div class="process-step">
            <div class="step-num">01</div>
            <div class="step-title">Descoberta</div>
            <div class="step-desc">Imersão profunda no seu negócio, público e objetivos estratégicos.</div>
        </div>
        <div class="process-step">
            <div class="step-num">02</div>
            <div class="step-title">Estratégia</div>
            <div class="step-desc">Definição do posicionamento visual e conceito criativo central.</div>
        </div>
        <div class="process-step">
            <div class="step-num accent">03</div>
            <div class="step-title">Criação</div>
            <div class="step-desc">Design executado com precisão e revisões colaborativas.</div>
        </div>
        <div class="process-step">
            <div class="step-num">04</div>
            <div class="step-title">Entrega</div>
            <div class="step-desc">Arquivos finais + guia de uso + suporte pós-projeto.</div>
        </div>
    </div>
</section>

<section class="portfolio-section">
    <div class="portfolio-header">
        <h2>Projetos<br>em Destaque</h2>
        <a href="#">Ver todos os projetos ↗</a>
    </div>
    <div class="portfolio-grid">
        <div>
            <div class="portfolio-item">
                <div class="portfolio-img p1">🎨</div>
                <div class="portfolio-overlay">
                    <div class="portfolio-cat">Identidade Visual</div>
                    <div class="portfolio-name">Redesign Marca Nacional</div>
                </div>
            </div>
        </div>
        <div>
            <div class="portfolio-item">
                <div class="portfolio-img-tall p2">💻</div>
                <div class="portfolio-overlay">
                    <div class="portfolio-cat">Web Design</div>
                    <div class="portfolio-name">Plataforma Fintech</div>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="testimonials-section">
    <div class="about-label">● Depoimentos</div>
    <div class="testimonial-big">
        <div class="testimonial-big-text">"A FORMA não entregou apenas um design bonito. Entregou uma <em>estratégia visual completa</em> que transformou como o mercado nos enxerga."</div>
        <div class="testimonial-author-big">
            <div class="author-name-big">Carla Drummond</div>
            <div class="author-role-big">CEO, Startup de Saúde</div>
        </div>
    </div>
    <div class="testimonials-small">
        <div class="testimonial-small">
            <div class="t-quote">"</div>
            <div class="t-text">Triplicamos as conversões após o redesign do site. Investimento que pagou em semanas.</div>
            <div class="t-author">Marcos Oliveira</div><div class="t-role">E-commerce de Moda</div>
        </div>
        <div class="testimonial-small">
            <div class="t-quote">"</div>
            <div class="t-text">A atenção ao detalhe é incomparável. Cada elemento tem propósito e intenção claros.</div>
            <div class="t-author">Julia Fernandes</div><div class="t-role">Diretora de Marketing</div>
        </div>
        <div class="testimonial-small">
            <div class="t-quote">"</div>
            <div class="t-text">Parceiros de verdade. Estão na 4ª entrega conosco. Indispensáveis para o crescimento.</div>
            <div class="t-author">Ricardo Neves</div><div class="t-role">Founder SaaS B2B</div>
        </div>
    </div>
</section>

<section class="faq-section">
    <div class="faq-grid">
        <div class="faq-left">
            <h2>Suas<br>Dúvidas<br><em>Respondidas</em></h2>
            <p>Não encontrou o que procura? Fale diretamente com nossa equipe.</p>
        </div>
        <div class="faq-items">
            <div class="faq-item"><div class="faq-q">Qual o prazo médio de entrega?</div><div class="faq-a">Projetos de identidade visual: 3-4 semanas. Web design: 4-6 semanas. Projetos completos: 8-12 semanas.</div></div>
            <div class="faq-item"><div class="faq-q">Como funciona o processo de revisão?</div><div class="faq-a">Cada projeto inclui 3 rodadas de revisão. Trabalhamos até você estar 100% satisfeito com o resultado.</div></div>
            <div class="faq-item"><div class="faq-q">Vocês trabalham com startups ou só grandes empresas?</div><div class="faq-a">Atendemos empresas de todos os tamanhos. Temos pacotes específicos para startups em crescimento.</div></div>
            <div class="faq-item"><div class="faq-q">Qual o investimento mínimo?</div><div class="faq-a">Projetos a partir de R$3.500. O valor final depende do escopo e complexidade do projeto.</div></div>
        </div>
    </div>
</section>

<section class="cta-section">
    <div class="about-label" style="justify-content:center; display:flex;">● Vamos começar</div>
    <h2>Pronto para<br><em>transformar</em><br>sua marca?</h2>
    <p>Vamos conversar sobre o seu próximo projeto.</p>
    <a href="#" class="btn-black" style="font-size:1.1rem; padding:1.1rem 2.5rem;">Iniciar Projeto Agora →</a>
</section>

<footer class="footer">
    <div class="footer-logo">FORMA<span style="color:var(--accent);">.</span></div>
    <div class="footer-links"><a href="#">Privacidade</a><a href="#">Termos</a><a href="#">Blog</a><a href="#">Contato</a></div>
    <div class="footer-copy">© 2025 FORMA Studio. Todos os direitos reservados.</div>
</footer>
""", unsafe_allow_html=True)
