import streamlit as st

st.set_page_config(page_title="IMPULSO - Evento Online", page_icon="🚀", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=Montserrat+Alternates:wght@700;800;900&display=swap');

:root {
    --neon: #22c55e;
    --neon-dark: #16a34a;
    --neon-light: #4ade80;
    --bg: #080c08;
    --dark: #0d140d;
    --card: #111811;
    --border: #1a2e1a;
    --white: #f0fdf4;
    --yellow: #facc15;
    --muted: rgba(240,253,244,0.5);
    --orange: #fb923c;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--white) !important;
    font-family: 'Montserrat', sans-serif;
}
[data-testid="stHeader"] { display: none; }
[data-testid="stSidebar"] { display: none; }
.main .block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stVerticalBlock"] { gap: 0 !important; }

/* HEADER BRAND */
.top-bar { background: var(--neon); padding: 0.6rem 6%; display: flex; align-items: center; justify-content: center; }
.top-bar-text { font-size: 0.85rem; font-weight: 700; color: #0a0f0a; text-transform: uppercase; letter-spacing: 1px; }
.top-bar-text span { font-weight: 900; }

/* HERO */
.hero {
    padding: 4rem 6% 5rem; min-height: 100vh;
    display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 4rem; align-items: center;
    background: radial-gradient(ellipse at top left, rgba(34,197,94,0.1) 0%, transparent 60%),
                radial-gradient(ellipse at bottom right, rgba(34,197,94,0.05) 0%, transparent 60%);
    position: relative;
}
.hero-left { position: relative; z-index: 2; }
.brand-tag { display: inline-flex; align-items: center; gap: 0.75rem; margin-bottom: 2rem; }
.brand-icon { color: var(--neon); font-size: 1rem; }
.brand-name { font-size: 1rem; font-weight: 800; color: var(--neon); letter-spacing: 2px; text-transform: uppercase; }
.brand-sub { font-size: 0.75rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; }
.hero h1 { font-family: 'Montserrat Alternates', sans-serif; font-size: clamp(2.5rem, 4.5vw, 4rem); font-weight: 900; line-height: 1.1; margin-bottom: 1.5rem; }
.hero h1 .highlight { color: var(--neon); }
.hero h1 .highlight-y { color: var(--yellow); }
.hero p { color: var(--muted); font-size: 1rem; line-height: 1.75; margin-bottom: 2rem; }
.hero-cta { display: flex; flex-direction: column; gap: 1rem; align-items: flex-start; }
.btn-neon { background: var(--neon); color: #0a0f0a; padding: 1.1rem 2.5rem; border-radius: 12px; font-weight: 900; font-size: 1.1rem; text-decoration: none; transition: all 0.3s; display: inline-block; font-family: 'Montserrat', sans-serif; }
.btn-neon:hover { background: var(--neon-light); transform: translateY(-3px); box-shadow: 0 16px 40px rgba(34,197,94,0.4); }
.btn-sub-text { color: var(--muted); font-size: 0.8rem; display: flex; align-items: center; gap: 0.5rem; }
.trust-badges { display: flex; gap: 1.5rem; flex-wrap: wrap; margin-top: 1rem; }
.trust-b { display: flex; align-items: center; gap: 0.5rem; font-size: 0.8rem; color: var(--muted); }
.trust-icon { color: var(--neon); }

.hero-right { position: relative; z-index: 2; }
.host-card { background: var(--card); border: 1px solid var(--border); border-radius: 20px; overflow: hidden; }
.host-img { height: 280px; background: linear-gradient(180deg, rgba(34,197,94,0.1), var(--card)); display: flex; align-items: flex-end; justify-content: center; font-size: 6rem; padding-bottom: 0; }
.host-info { padding: 1.5rem; border-top: 1px solid var(--border); }
.host-name { font-weight: 900; font-size: 1.2rem; margin-bottom: 0.25rem; }
.host-title { color: var(--neon); font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 1rem; }
.host-creds { display: flex; flex-direction: column; gap: 0.5rem; }
.host-cred { display: flex; align-items: center; gap: 0.5rem; font-size: 0.8rem; color: var(--muted); }
.host-cred::before { content: '→'; color: var(--neon); }

/* COUNTER */
.counter-section { background: var(--neon); padding: 2rem 6%; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; }
.counter-left { font-size: 0.9rem; font-weight: 800; color: #0a0f0a; text-transform: uppercase; letter-spacing: 1px; }
.counter-timer { display: flex; gap: 1rem; align-items: center; }
.timer-block { background: #0a0f0a; color: var(--neon); border-radius: 10px; padding: 0.75rem 1rem; text-align: center; }
.timer-num { font-size: 2rem; font-weight: 900; line-height: 1; }
.timer-label { font-size: 0.65rem; text-transform: uppercase; letter-spacing: 1px; margin-top: 0.25rem; }
.timer-sep { font-size: 1.5rem; font-weight: 900; color: #0a0f0a; }

/* IDEAL */
.ideal-section { padding: 6rem 6%; }
.section-eyebrow { color: var(--neon); font-size: 0.8rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem; }
.section-eyebrow::before { content: ''; width: 30px; height: 2px; background: var(--neon); }
.section-h2 { font-family: 'Montserrat Alternates', sans-serif; font-size: clamp(2rem, 3.5vw, 3rem); font-weight: 900; line-height: 1.2; margin-bottom: 1.5rem; }
.section-h2 span { color: var(--neon); }
.ideal-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: start; }
.ideal-desc { color: var(--muted); line-height: 1.8; margin-bottom: 2rem; }
.ideal-checks { display: flex; flex-direction: column; gap: 0.75rem; }
.ideal-check { background: var(--card); border: 1px solid var(--border); border-radius: 10px; padding: 0.9rem 1.2rem; display: flex; align-items: center; gap: 0.75rem; font-size: 0.875rem; }
.ideal-check::before { content: '✓'; background: var(--neon); color: #0a0f0a; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 0.7rem; flex-shrink: 0; }

/* PILLARS */
.pillars-section { padding: 6rem 6%; background: var(--dark); }
.pillars-header { text-align: center; margin-bottom: 4rem; }
.pillars-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
.pillar-card { background: var(--card); border: 1px solid var(--border); border-radius: 20px; padding: 2.5rem; text-align: center; transition: all 0.3s; }
.pillar-card:hover { border-color: var(--neon); transform: translateY(-4px); box-shadow: 0 16px 40px rgba(34,197,94,0.1); }
.pillar-icon { font-size: 2.5rem; margin-bottom: 1.5rem; display: block; }
.pillar-num { color: var(--neon); font-size: 0.8rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin-bottom: 0.5rem; }
.pillar-title { font-weight: 800; font-size: 1.2rem; margin-bottom: 1rem; }
.pillar-items { display: flex; flex-direction: column; gap: 0.5rem; }
.pillar-item { color: var(--muted); font-size: 0.85rem; display: flex; align-items: center; gap: 0.5rem; justify-content: center; }
.pillar-item::before { content: '→'; color: var(--neon); font-size: 0.7rem; }
.pillar-cta { margin-top: 1.5rem; }
.pillar-btn { display: inline-block; background: transparent; border: 1px solid var(--neon); color: var(--neon); padding: 0.6rem 1.4rem; border-radius: 8px; font-size: 0.8rem; font-weight: 700; text-decoration: none; transition: all 0.3s; }
.pillar-btn:hover { background: var(--neon); color: #0a0f0a; }

/* OFFER */
.offer-section { padding: 6rem 6%; }
.offer-card { background: var(--card); border: 2px solid var(--border); border-radius: 24px; padding: 3rem; max-width: 700px; margin: 3rem auto 0; }
.offer-logo { text-align: center; margin-bottom: 2rem; }
.offer-logo img { max-height: 60px; }
.offer-title { text-align: center; font-weight: 800; font-size: 1rem; margin-bottom: 2rem; color: var(--muted); }
.offer-includes { display: flex; flex-direction: column; gap: 0.75rem; margin-bottom: 2rem; }
.offer-item { display: flex; align-items: center; gap: 0.75rem; font-size: 0.9rem; }
.offer-check { color: var(--neon); font-weight: 700; }
.offer-price-block { text-align: center; background: rgba(34,197,94,0.06); border: 1px solid var(--border); border-radius: 16px; padding: 2rem; margin-bottom: 2rem; }
.offer-de { color: var(--muted); text-decoration: line-through; font-size: 0.9rem; }
.offer-price-main { font-family: 'Montserrat Alternates', sans-serif; font-size: 3.5rem; font-weight: 900; color: var(--neon); line-height: 1; }
.offer-price-label { font-size: 0.8rem; color: var(--muted); margin-top: 0.25rem; }
.offer-or { color: var(--muted); font-size: 0.85rem; margin: 0.75rem 0; }
.offer-price-alt { font-size: 1rem; font-weight: 700; color: var(--yellow); }
.offer-cta { text-align: center; }
.trust-seals { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-top: 1.5rem; }
.trust-seal { background: rgba(255,255,255,0.04); border: 1px solid var(--border); border-radius: 8px; padding: 0.4rem 0.8rem; font-size: 0.75rem; color: var(--muted); }

/* MENTOR */
.mentor-section { padding: 6rem 6%; display: grid; grid-template-columns: 1fr 1.5fr; gap: 5rem; align-items: center; background: var(--dark); }
.mentor-img { background: var(--card); border: 1px solid var(--border); border-radius: 20px; aspect-ratio: 3/4; display: flex; align-items: center; justify-content: center; font-size: 6rem; }
.mentor-tag { color: var(--neon); font-size: 0.8rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem; }
.mentor-tag::before { content: ''; width: 24px; height: 2px; background: var(--neon); }
.mentor h2 { font-family: 'Montserrat Alternates', sans-serif; font-size: clamp(1.8rem, 3vw, 2.5rem); font-weight: 900; margin-bottom: 1.5rem; line-height: 1.2; }
.mentor p { color: var(--muted); line-height: 1.8; margin-bottom: 1rem; font-size: 0.9rem; }

/* FAQ */
.faq-section { padding: 6rem 6%; max-width: 750px; margin: 0 auto; }
.faq-item { background: var(--card); border: 1px solid var(--border); border-radius: 14px; padding: 1.5rem; margin-bottom: 1rem; }
.faq-q { font-weight: 700; margin-bottom: 0.75rem; font-size: 0.95rem; display: flex; align-items: center; gap: 0.75rem; }
.faq-q::before { content: '?'; background: var(--neon); color: #0a0f0a; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 800; flex-shrink: 0; }
.faq-a { color: var(--muted); font-size: 0.875rem; line-height: 1.7; }

/* FINAL CTA */
.final-cta { padding: 6rem 6%; text-align: center; border-top: 1px solid var(--border); }
.final-cta h2 { font-family: 'Montserrat Alternates', sans-serif; font-size: clamp(2rem, 4vw, 3.5rem); font-weight: 900; margin-bottom: 1rem; line-height: 1.2; }
.final-cta h2 span { color: var(--neon); }
.final-cta p { color: var(--muted); margin-bottom: 2.5rem; }

/* FOOTER */
.footer { padding: 2rem 6%; border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; }
.footer-brand { color: var(--neon); font-weight: 800; font-size: 1rem; }
.footer-links { display: flex; gap: 2rem; }
.footer-links a { color: var(--muted); text-decoration: none; font-size: 0.8rem; }
.footer-copy { color: var(--muted); font-size: 0.75rem; }

@media (max-width: 900px) {
    .hero, .ideal-grid, .mentor-section { grid-template-columns: 1fr; }
    .pillars-grid { grid-template-columns: 1fr; }
    .counter-section { flex-direction: column; text-align: center; }
}
</style>

<div class="top-bar">
    <div class="top-bar-text">⚡ Todo nosso conhecimento reunido em um único lugar! <span>IMPULSO 2025</span></div>
</div>

<section class="hero">
    <div class="hero-left">
        <div class="brand-tag">
            <div class="brand-icon">⚡</div>
            <div>
                <div class="brand-name">IMPULSO</div>
                <div class="brand-sub">Seu Programa de Evolução</div>
            </div>
        </div>
        <h1>Seja o profissional<br>mais desejado e<br><span class="highlight-y">bem pago</span><br>do mercado!</h1>
        <p>Desenvolva sua COMUNICAÇÃO, LIDERANÇA e saiba utilizar a INTELIGÊNCIA ARTIFICIAL para aumentar sua produtividade e ganhar mais dinheiro.</p>
        <div class="hero-cta">
            <a href="#" class="btn-neon">🚀 Garantir Minha Vaga</a>
            <div class="btn-sub-text">⏰ Vagas limitadas · Oferta por tempo limitado</div>
            <div class="trust-badges">
                <div class="trust-b"><span class="trust-icon">✓</span> Certificado de Conclusão</div>
                <div class="trust-b"><span class="trust-icon">✓</span> Acesso Vitalício</div>
                <div class="trust-b"><span class="trust-icon">✓</span> 7 dias de Garantia</div>
            </div>
        </div>
    </div>
    <div class="hero-right">
        <div class="host-card">
            <div class="host-img">👨‍💼</div>
            <div class="host-info">
                <div class="host-name">Joel Jota</div>
                <div class="host-title">⚡ IMPULSO · Seu Mentor</div>
                <div class="host-creds">
                    <div class="host-cred">Parceiro da John C. Maxwell</div>
                    <div class="host-cred">Pós em Psicologia do Esporte</div>
                    <div class="host-cred">+500K seguidores nas redes</div>
                </div>
            </div>
        </div>
    </div>
</section>

<div class="counter-section">
    <div class="counter-left">⏰ Oferta encerra em:</div>
    <div class="counter-timer">
        <div class="timer-block"><div class="timer-num">02</div><div class="timer-label">Dias</div></div>
        <div class="timer-sep">:</div>
        <div class="timer-block"><div class="timer-num">14</div><div class="timer-label">Horas</div></div>
        <div class="timer-sep">:</div>
        <div class="timer-block"><div class="timer-num">38</div><div class="timer-label">Min</div></div>
        <div class="timer-sep">:</div>
        <div class="timer-block"><div class="timer-num">22</div><div class="timer-label">Seg</div></div>
    </div>
</div>

<section class="ideal-section">
    <div class="ideal-grid">
        <div>
            <div class="section-eyebrow">O evento IMPULSO é ideal para:</div>
            <div class="section-h2">Para quem é<br>este <span>evento</span>?</div>
            <div class="ideal-desc">Profissionais em busca de crescimento acelerado no mercado. Se você quer comunicar melhor, liderar equipes e usar IA para ser mais produtivo, este evento é para você.</div>
        </div>
        <div class="ideal-checks">
            <div class="ideal-check">Ter uma comunicação assertiva e estratégica</div>
            <div class="ideal-check">Ser um líder inteligente e estratégico</div>
            <div class="ideal-check">Maximizar sua produtividade com Inteligência Artificial</div>
            <div class="ideal-check">Receber mais e trabalhar com o que ama</div>
            <div class="ideal-check">Construir uma carreira sólida e respeitada</div>
            <div class="ideal-check">Liderar equipes de alta performance</div>
        </div>
    </div>
</section>

<section class="pillars-section">
    <div class="pillars-header">
        <div class="section-eyebrow" style="justify-content:center;">● 3 Pilares</div>
        <div class="section-h2" style="text-align:center;">Domine os <span>3 pilares</span><br>do profissional do futuro</div>
    </div>
    <div class="pillars-grid">
        <div class="pillar-card">
            <span class="pillar-icon">🗣️</span>
            <div class="pillar-num">Pilar 01</div>
            <div class="pillar-title">Comunicação</div>
            <div class="pillar-items">
                <div class="pillar-item">Comunicação de alto impacto</div>
                <div class="pillar-item">Técnicas de persuasão</div>
                <div class="pillar-item">Apresentações que vendem</div>
                <div class="pillar-item">Storytelling profissional</div>
            </div>
            <div class="pillar-cta"><a href="#" class="pillar-btn">Saiba mais →</a></div>
        </div>
        <div class="pillar-card">
            <span class="pillar-icon">⚡</span>
            <div class="pillar-num">Pilar 02</div>
            <div class="pillar-title">Produtividade</div>
            <div class="pillar-items">
                <div class="pillar-item">Ferramentas de IA no trabalho</div>
                <div class="pillar-item">Gestão do tempo avançada</div>
                <div class="pillar-item">Automação de tarefas</div>
                <div class="pillar-item">Foco e gestão de energia</div>
            </div>
            <div class="pillar-cta"><a href="#" class="pillar-btn">Saiba mais →</a></div>
        </div>
        <div class="pillar-card">
            <span class="pillar-icon">👑</span>
            <div class="pillar-num">Pilar 03</div>
            <div class="pillar-title">Liderança</div>
            <div class="pillar-items">
                <div class="pillar-item">Liderar a si mesmo primeiro</div>
                <div class="pillar-item">Gestão de equipes</div>
                <div class="pillar-item">Inteligência emocional</div>
                <div class="pillar-item">Cultura de alta performance</div>
            </div>
            <div class="pillar-cta"><a href="#" class="pillar-btn">Saiba mais →</a></div>
        </div>
    </div>
</section>

<section class="offer-section">
    <div style="text-align:center; margin-bottom:1rem;">
        <div class="section-eyebrow" style="justify-content:center;">💰 Não Perca essa Chance</div>
        <div class="section-h2" style="text-align:center;">Garanta hoje a <span>sua participação</span>!</div>
    </div>
    <div class="offer-card">
        <div class="offer-title">⚡ IMPULSO · Seu Programa de Evolução</div>
        <div class="offer-includes">
            <div class="offer-item"><span class="offer-check">✓</span> Evento online ao vivo com Joel Jota</div>
            <div class="offer-item"><span class="offer-check">✓</span> Interação com a comunidade no chat ao vivo</div>
            <div class="offer-item"><span class="offer-check">✓</span> Certificado de conclusão</div>
            <div class="offer-item"><span class="offer-check">✓</span> Conteúdos de aquecimento na plataforma</div>
            <div class="offer-item"><span class="offer-check">✓</span> Bônus e surpresas exclusivas</div>
        </div>
        <div class="offer-price-block">
            <div class="offer-de">De: R$697</div>
            <div style="font-size:0.8rem;color:var(--neon);margin-bottom:0.5rem;">Por apenas:</div>
            <div class="offer-price-main">12x de R$28,85</div>
            <div class="offer-or">ou</div>
            <div class="offer-price-alt">R$297,00 à vista</div>
        </div>
        <div class="offer-cta">
            <a href="#" class="btn-neon" style="width:100%;text-align:center;display:block;">🚀 Quero aproveitar a promoção!</a>
        </div>
        <div class="trust-seals">
            <div class="trust-seal">🔒 Pagamento Seguro</div>
            <div class="trust-seal">✅ 7 dias de Garantia</div>
            <div class="trust-seal">📜 Certificado Incluso</div>
        </div>
    </div>
</section>

<section class="mentor-section">
    <div class="mentor-img">👨‍💼</div>
    <div>
        <div class="mentor-tag">Quem vai ser o seu mentor?</div>
        <h2>Joel Jota — <span style="color:var(--neon);">Referência</span> em Alta Performance</h2>
        <p>Criado com James Cooke e pai de três menores e atualmente mora na cidade de Campinas. Graduado e autor Best-Seller. Mestre em Ciências do Esporte e Bacharel em Psicologia pela Universidade Anhembi Morumbi. Diretor geral do Instituto Waymark (2015 a 2018).</p>
        <p>Instrutor de PNL e trabalhou com mais de 500 times. Metáfora do modelo global e lider do mundo de jornada.</p>
        <a href="#" class="btn-neon" style="display:inline-block;margin-top:1.5rem;">🚀 Garantir Minha Vaga</a>
    </div>
</section>

<section class="faq-section">
    <div style="text-align:center; margin-bottom:2.5rem;">
        <div class="section-eyebrow" style="justify-content:center;">● FAQ</div>
        <div class="section-h2" style="text-align:center;">Perguntas <span>Frequentes</span></div>
    </div>
    <div class="faq-item"><div class="faq-q">Quais recursos estão incluídos?</div><div class="faq-a">Evento online ao vivo, certificado de conclusão, conteúdos de aquecimento na plataforma, interação na comunidade e bônus exclusivos.</div></div>
    <div class="faq-item"><div class="faq-q">Vou precisar de suporte adicional?</div><div class="faq-a">Toda a estrutura necessária está incluída. Caso precise de ajuda, nossa equipe de suporte está disponível 24/7 durante o evento.</div></div>
    <div class="faq-item"><div class="faq-q">Posso cancelar minha inscrição?</div><div class="faq-a">Sim! Você tem 7 dias de garantia total. Se não gostar, devolvemos 100% do seu investimento sem perguntas.</div></div>
    <div class="faq-item"><div class="faq-q">Tem como entrar em contato?</div><div class="faq-a">Sim! Nossa equipe está disponível via WhatsApp e email. Clique no botão de suporte no rodapé da página.</div></div>
</section>

<section class="final-cta">
    <h2>Não perca essa chance,<br>garanta hoje a <span>sua participação</span>!</h2>
    <p style="color:var(--muted);margin-bottom:2.5rem;">Vagas limitadas. Oferta encerra em breve.</p>
    <a href="#" class="btn-neon" style="font-size:1.1rem;padding:1.1rem 3rem;">🚀 Garantir Minha Vaga Agora</a>
</section>

<footer class="footer">
    <div class="footer-brand">⚡ IMPULSO</div>
    <div class="footer-links"><a href="#">Privacidade</a><a href="#">Termos</a><a href="#">Contato</a></div>
    <div class="footer-copy">© 2025 IMPULSO. Todos os direitos reservados.</div>
</footer>
""", unsafe_allow_html=True)
