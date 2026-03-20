import streamlit as st

st.set_page_config(page_title="NexRank - SEO Intelligence", page_icon="⚡", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Bebas+Neue&family=JetBrains+Mono:wght@400;700&display=swap');

:root {
    --black: #050508;
    --dark: #0d0d14;
    --card: #12121c;
    --border: #1e1e2e;
    --accent: #7c3aed;
    --accent2: #06b6d4;
    --green: #10b981;
    --white: #f8f8ff;
    --gray: #9090a8;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html, body, [data-testid="stAppViewContainer"] {
    background: var(--black) !important;
    color: var(--white) !important;
    font-family: 'Space Grotesk', sans-serif;
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
    background: rgba(5,5,8,0.85);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border);
}
.nav-logo { font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem; color: var(--white); letter-spacing: 2px; }
.nav-logo span { color: var(--accent); }
.nav-links { display: flex; gap: 2rem; }
.nav-links a { color: var(--gray); text-decoration: none; font-size: 0.9rem; transition: color 0.3s; }
.nav-links a:hover { color: var(--white); }
.nav-cta {
    background: var(--accent); color: var(--white); border: none;
    padding: 0.6rem 1.5rem; border-radius: 6px; font-size: 0.9rem;
    font-family: 'Space Grotesk', sans-serif; cursor: pointer; font-weight: 600;
    text-decoration: none;
}

/* HERO */
.hero {
    min-height: 100vh;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    padding: 8rem 5% 5rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute; top: 20%; left: 50%; transform: translateX(-50%);
    width: 600px; height: 600px;
    background: radial-gradient(circle, rgba(124,58,237,0.15) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
}
.hero-badge {
    display: inline-flex; align-items: center; gap: 0.5rem;
    background: rgba(124,58,237,0.1); border: 1px solid rgba(124,58,237,0.3);
    color: var(--accent); padding: 0.4rem 1rem; border-radius: 50px;
    font-size: 0.8rem; font-weight: 600; letter-spacing: 1px; text-transform: uppercase;
    margin-bottom: 2rem;
}
.hero h1 {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(3.5rem, 8vw, 7rem);
    line-height: 0.95;
    color: var(--white);
    margin-bottom: 1.5rem;
    letter-spacing: 2px;
}
.hero h1 span { color: var(--accent); }
.hero p {
    max-width: 600px; color: var(--gray); font-size: 1.1rem;
    line-height: 1.7; margin: 0 auto 2.5rem;
}
.hero-btns { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
.btn-primary {
    background: var(--accent); color: var(--white);
    padding: 0.9rem 2.2rem; border-radius: 8px;
    font-weight: 600; font-size: 1rem; text-decoration: none;
    display: inline-flex; align-items: center; gap: 0.5rem;
    transition: all 0.3s; box-shadow: 0 0 30px rgba(124,58,237,0.4);
}
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 0 50px rgba(124,58,237,0.6); }
.btn-secondary {
    background: transparent; color: var(--white);
    padding: 0.9rem 2.2rem; border-radius: 8px;
    border: 1px solid var(--border); font-weight: 600; font-size: 1rem;
    text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem;
    transition: all 0.3s;
}
.btn-secondary:hover { border-color: var(--accent); color: var(--accent); }

/* STATS STRIP */
.stats-strip {
    background: var(--card); border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
    padding: 2rem 5%; display: flex; justify-content: space-around; flex-wrap: wrap; gap: 1rem;
}
.stat-item { text-align: center; }
.stat-num { font-family: 'Bebas Neue', sans-serif; font-size: 2.5rem; color: var(--accent); }
.stat-label { color: var(--gray); font-size: 0.85rem; }

/* LOGOS */
.logos-section { padding: 3rem 5%; text-align: center; }
.logos-title { color: var(--gray); font-size: 0.85rem; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 2rem; }
.logos-row { display: flex; justify-content: center; align-items: center; gap: 3rem; flex-wrap: wrap; }
.logo-pill {
    background: var(--card); border: 1px solid var(--border);
    padding: 0.6rem 1.5rem; border-radius: 8px; color: var(--gray);
    font-weight: 600; font-size: 0.9rem;
}

/* FEATURES */
.features-section { padding: 6rem 5%; }
.section-label {
    display: inline-block; color: var(--accent2);
    font-size: 0.8rem; font-weight: 600; letter-spacing: 2px; text-transform: uppercase;
    margin-bottom: 1rem;
}
.section-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(2.5rem, 5vw, 4rem); color: var(--white);
    margin-bottom: 1rem; letter-spacing: 1px;
}
.section-title span { color: var(--accent); }
.section-sub { color: var(--gray); font-size: 1rem; line-height: 1.7; max-width: 500px; margin-bottom: 3rem; }
.features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; }
.feature-card {
    background: var(--card); border: 1px solid var(--border); border-radius: 16px;
    padding: 2rem; transition: all 0.3s; position: relative; overflow: hidden;
}
.feature-card::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, var(--accent), var(--accent2));
    opacity: 0; transition: opacity 0.3s;
}
.feature-card:hover { border-color: rgba(124,58,237,0.4); transform: translateY(-4px); }
.feature-card:hover::before { opacity: 1; }
.feature-icon { font-size: 2rem; margin-bottom: 1rem; }
.feature-title { font-size: 1.1rem; font-weight: 700; color: var(--white); margin-bottom: 0.5rem; }
.feature-desc { color: var(--gray); font-size: 0.9rem; line-height: 1.6; }

/* RESULTS */
.results-section {
    padding: 6rem 5%;
    background: linear-gradient(135deg, rgba(124,58,237,0.05) 0%, rgba(6,182,212,0.03) 100%);
    border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
}
.results-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }
.results-metrics { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.metric-card {
    background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 1.5rem;
}
.metric-value { font-family: 'Bebas Neue', sans-serif; font-size: 2.5rem; color: var(--green); }
.metric-label { color: var(--gray); font-size: 0.85rem; }

/* PRICING */
.pricing-section { padding: 6rem 5%; text-align: center; }
.pricing-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; max-width: 900px; margin: 3rem auto 0; }
.pricing-card {
    background: var(--card); border: 1px solid var(--border); border-radius: 16px;
    padding: 2.5rem 2rem; position: relative; transition: all 0.3s;
}
.pricing-card.popular {
    border-color: var(--accent);
    background: linear-gradient(135deg, rgba(124,58,237,0.1), var(--card));
}
.popular-badge {
    position: absolute; top: -12px; left: 50%; transform: translateX(-50%);
    background: var(--accent); color: var(--white); padding: 0.25rem 1rem;
    border-radius: 50px; font-size: 0.75rem; font-weight: 700; white-space: nowrap;
}
.pricing-name { font-size: 0.9rem; color: var(--gray); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 1rem; }
.pricing-price { font-family: 'Bebas Neue', sans-serif; font-size: 3.5rem; color: var(--white); }
.pricing-period { color: var(--gray); font-size: 0.85rem; margin-bottom: 1.5rem; }
.pricing-features { list-style: none; text-align: left; margin-bottom: 2rem; }
.pricing-features li { color: var(--gray); font-size: 0.9rem; padding: 0.5rem 0; border-bottom: 1px solid var(--border); }
.pricing-features li::before { content: '✓ '; color: var(--green); font-weight: 700; }
.pricing-btn {
    width: 100%; padding: 0.9rem; border-radius: 8px; font-weight: 700;
    cursor: pointer; font-family: 'Space Grotesk', sans-serif; font-size: 0.95rem;
    transition: all 0.3s;
}
.pricing-btn-outline { background: transparent; border: 1px solid var(--border); color: var(--white); }
.pricing-btn-outline:hover { border-color: var(--accent); color: var(--accent); }
.pricing-btn-filled { background: var(--accent); border: none; color: var(--white); }
.pricing-btn-filled:hover { background: #6d28d9; }

/* TESTIMONIALS */
.testimonials-section { padding: 6rem 5%; background: var(--dark); }
.testimonials-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-top: 3rem; }
.testimonial-card {
    background: var(--card); border: 1px solid var(--border); border-radius: 16px; padding: 2rem;
}
.testimonial-stars { color: #fbbf24; font-size: 1rem; margin-bottom: 1rem; }
.testimonial-text { color: var(--gray); font-size: 0.9rem; line-height: 1.7; margin-bottom: 1.5rem; font-style: italic; }
.testimonial-author { display: flex; align-items: center; gap: 0.75rem; }
.author-avatar {
    width: 40px; height: 40px; border-radius: 50%;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.9rem;
}
.author-name { font-weight: 600; font-size: 0.9rem; }
.author-role { color: var(--gray); font-size: 0.8rem; }

/* FAQ */
.faq-section { padding: 6rem 5%; max-width: 800px; margin: 0 auto; }
.faq-item { border-bottom: 1px solid var(--border); padding: 1.5rem 0; }
.faq-q { font-weight: 600; color: var(--white); margin-bottom: 0.75rem; font-size: 1rem; }
.faq-a { color: var(--gray); font-size: 0.9rem; line-height: 1.7; }

/* CTA FINAL */
.cta-section {
    padding: 6rem 5%; text-align: center;
    background: linear-gradient(135deg, rgba(124,58,237,0.1) 0%, rgba(6,182,212,0.05) 100%);
    border-top: 1px solid var(--border);
}
.cta-section h2 { font-family: 'Bebas Neue', sans-serif; font-size: 4rem; color: var(--white); margin-bottom: 1rem; }
.cta-section p { color: var(--gray); font-size: 1.1rem; margin-bottom: 2.5rem; }

/* FOOTER */
.footer {
    background: var(--dark); border-top: 1px solid var(--border);
    padding: 3rem 5%; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;
}
.footer-links { display: flex; gap: 2rem; flex-wrap: wrap; }
.footer-links a { color: var(--gray); text-decoration: none; font-size: 0.85rem; transition: color 0.3s; }
.footer-links a:hover { color: var(--accent); }
.footer-copy { color: var(--gray); font-size: 0.8rem; }

@media (max-width: 768px) {
    .pricing-grid, .testimonials-grid { grid-template-columns: 1fr; }
    .results-grid { grid-template-columns: 1fr; }
    .results-metrics { grid-template-columns: 1fr 1fr; }
}
</style>

<nav class="nav">
    <div class="nav-logo">NEX<span>RANK</span></div>
    <div class="nav-links">
        <a href="#">Recursos</a>
        <a href="#">Resultados</a>
        <a href="#">Preços</a>
        <a href="#">FAQ</a>
    </div>
    <a href="#" class="nav-cta">Teste Grátis →</a>
</nav>

<section class="hero">
    <div class="hero-badge">⚡ Nova IA de SEO chegou</div>
    <h1>DOMINE O<br><span>GOOGLE</span><br>COM IA</h1>
    <p>A plataforma de SEO mais poderosa do mercado. Análise em tempo real, sugestões de IA e rankings que sobem enquanto você dorme.</p>
    <div class="hero-btns">
        <a href="#" class="btn-primary">Começar Agora — Grátis ⚡</a>
        <a href="#" class="btn-secondary">▶ Ver Demo</a>
    </div>
</section>

<div class="stats-strip">
    <div class="stat-item"><div class="stat-num">50K+</div><div class="stat-label">Palavras Rastreadas</div></div>
    <div class="stat-item"><div class="stat-num">200%</div><div class="stat-label">Aumento Médio de Tráfego</div></div>
    <div class="stat-item"><div class="stat-num">12K+</div><div class="stat-label">Empresas Ativas</div></div>
    <div class="stat-item"><div class="stat-num">98%</div><div class="stat-label">Satisfação dos Clientes</div></div>
</div>

<div class="logos-section">
    <div class="logos-title">Confiado por empresas que crescem de verdade</div>
    <div class="logos-row">
        <div class="logo-pill">Google Partner</div>
        <div class="logo-pill">Shopify</div>
        <div class="logo-pill">HubSpot</div>
        <div class="logo-pill">Semrush</div>
        <div class="logo-pill">Ahrefs</div>
    </div>
</div>

<section class="features-section">
    <div class="section-label">● Recursos</div>
    <div class="section-title">SEO QUE ENTREGA<br><span>RESULTADOS REAIS</span></div>
    <div class="section-sub">Chega de achismo. Nossa IA analisa dados de milhões de páginas e entrega o que você precisa fazer agora.</div>
    <div class="features-grid">
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Análise de Keywords com IA</div>
            <div class="feature-desc">Descubra as palavras-chave com maior potencial de conversão antes da concorrência.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📈</div>
            <div class="feature-title">Rastreamento em Tempo Real</div>
            <div class="feature-desc">Monitore suas posições 24/7 com alertas instantâneos de mudanças de ranking.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🔗</div>
            <div class="feature-title">Análise de Backlinks</div>
            <div class="feature-desc">Mapa completo do seu perfil de links. Encontre oportunidades de link building de alto valor.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">Sugestões de Conteúdo IA</div>
            <div class="feature-desc">Receba briefs completos de conteúdo otimizado para ranquear na primeira página.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">⚙️</div>
            <div class="feature-title">Auditoria Técnica Completa</div>
            <div class="feature-desc">Identifique e corrija problemas técnicos que impedem seu site de ranquear.</div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Relatórios Automáticos</div>
            <div class="feature-desc">Relatórios profissionais gerados automaticamente para seus clientes toda semana.</div>
        </div>
    </div>
</section>

<section class="results-section">
    <div class="results-grid">
        <div>
            <div class="section-label">● Resultados Comprovados</div>
            <div class="section-title">NÚMEROS QUE<br><span>VOCÊ PODE</span><br>CONFIAR</div>
            <div class="section-sub">De startups a grandes empresas, ajudamos negócios a dominarem o Google com resultados mensuráveis.</div>
        </div>
        <div class="results-metrics">
            <div class="metric-card">
                <div class="metric-value">200%</div>
                <div class="metric-label">Tráfego Orgânico</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">50K+</div>
                <div class="metric-label">Keywords Ranqueadas</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">3.2x</div>
                <div class="metric-label">Mais Cliques</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">119%</div>
                <div class="metric-label">ROI Médio</div>
            </div>
        </div>
    </div>
</section>

<section class="pricing-section">
    <div class="section-label">● Preços</div>
    <div class="section-title">PLANO IDEAL<br>PARA <span>CADA NEGÓCIO</span></div>
    <div class="pricing-grid">
        <div class="pricing-card">
            <div class="pricing-name">Starter</div>
            <div class="pricing-price">R$0</div>
            <div class="pricing-period">para sempre grátis</div>
            <ul class="pricing-features">
                <li>100 palavras-chave</li>
                <li>1 projeto</li>
                <li>Relatórios básicos</li>
                <li>Suporte por email</li>
            </ul>
            <button class="pricing-btn pricing-btn-outline">Começar Grátis</button>
        </div>
        <div class="pricing-card popular">
            <div class="popular-badge">⭐ Mais Popular</div>
            <div class="pricing-name">Pro</div>
            <div class="pricing-price">R$197</div>
            <div class="pricing-period">/mês · cancele quando quiser</div>
            <ul class="pricing-features">
                <li>10.000 palavras-chave</li>
                <li>10 projetos</li>
                <li>IA de conteúdo inclusa</li>
                <li>Relatórios automáticos</li>
                <li>Suporte prioritário</li>
            </ul>
            <button class="pricing-btn pricing-btn-filled">Teste 14 dias Grátis</button>
        </div>
        <div class="pricing-card">
            <div class="pricing-name">Enterprise</div>
            <div class="pricing-price">R$497</div>
            <div class="pricing-period">/mês · tudo incluso</div>
            <ul class="pricing-features">
                <li>Projetos ilimitados</li>
                <li>API completa</li>
                <li>White label</li>
                <li>Gerente dedicado</li>
                <li>SLA garantido</li>
            </ul>
            <button class="pricing-btn pricing-btn-outline">Falar com Vendas</button>
        </div>
    </div>
</section>

<section class="testimonials-section">
    <div style="text-align:center">
        <div class="section-label">● Depoimentos</div>
        <div class="section-title">O QUE DIZEM<br><span>NOSSOS CLIENTES</span></div>
    </div>
    <div class="testimonials-grid">
        <div class="testimonial-card">
            <div class="testimonial-stars">★★★★★</div>
            <div class="testimonial-text">"Em 3 meses o tráfego orgânico do nosso e-commerce triplicou. A NexRank é simplesmente incomparável no mercado."</div>
            <div class="testimonial-author">
                <div class="author-avatar">RS</div>
                <div><div class="author-name">Rafael Santos</div><div class="author-role">CEO, E-commerce Moda</div></div>
            </div>
        </div>
        <div class="testimonial-card">
            <div class="testimonial-stars">★★★★★</div>
            <div class="testimonial-text">"A funcionalidade de IA para conteúdo transformou nossa estratégia. Economizamos 40h por mês em produção de conteúdo."</div>
            <div class="testimonial-author">
                <div class="author-avatar">AC</div>
                <div><div class="author-name">Ana Carolina</div><div class="author-role">Diretora de Marketing</div></div>
            </div>
        </div>
        <div class="testimonial-card">
            <div class="testimonial-stars">★★★★★</div>
            <div class="testimonial-text">"Usamos 5 ferramentas de SEO antes. Agora usamos só a NexRank e os resultados são melhores. Valeu cada centavo."</div>
            <div class="testimonial-author">
                <div class="author-avatar">PM</div>
                <div><div class="author-name">Pedro Mendes</div><div class="author-role">Founder, Agência Digital</div></div>
            </div>
        </div>
    </div>
</section>

<section class="faq-section">
    <div style="text-align:center; margin-bottom:3rem">
        <div class="section-label">● FAQ</div>
        <div class="section-title">DÚVIDAS<br><span>FREQUENTES</span></div>
    </div>
    <div class="faq-item">
        <div class="faq-q">⚡ Preciso de conhecimento técnico para usar?</div>
        <div class="faq-a">Não! A NexRank foi criada para ser usada por qualquer pessoa. Interface intuitiva com IA que explica tudo em linguagem simples.</div>
    </div>
    <div class="faq-item">
        <div class="faq-q">⚡ Quanto tempo para ver resultados?</div>
        <div class="faq-a">A maioria dos clientes vê melhorias nas primeiras 4 semanas. Resultados significativos geralmente aparecem em 60-90 dias.</div>
    </div>
    <div class="faq-item">
        <div class="faq-q">⚡ Posso cancelar a qualquer momento?</div>
        <div class="faq-a">Sim, sem multas ou burocracia. Cancele com um clique, a qualquer momento, direto no painel.</div>
    </div>
    <div class="faq-item">
        <div class="faq-q">⚡ Funciona para qualquer nicho?</div>
        <div class="faq-a">Sim! Atendemos desde e-commerces a consultórios médicos, agências digitais, SaaS e muito mais.</div>
    </div>
</section>

<section class="cta-section">
    <h2>PRONTO PARA<br>DOMINAR O GOOGLE?</h2>
    <p>Junte-se a 12.000+ empresas que já escolheram a inteligência.</p>
    <a href="#" class="btn-primary" style="font-size:1.1rem; padding:1rem 3rem;">Começar Gratuitamente ⚡</a>
</section>

<footer class="footer">
    <div class="nav-logo" style="font-family:'Bebas Neue',sans-serif;font-size:1.4rem;color:#f8f8ff;letter-spacing:2px;">NEX<span style="color:#7c3aed;">RANK</span></div>
    <div class="footer-links">
        <a href="#">Privacidade</a>
        <a href="#">Termos</a>
        <a href="#">Contato</a>
        <a href="#">Blog</a>
    </div>
    <div class="footer-copy">© 2025 NexRank. Todos os direitos reservados.</div>
</footer>
""", unsafe_allow_html=True)
