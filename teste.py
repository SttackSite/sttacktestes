import streamlit as st

st.set_page_config(page_title="EduVibe - Aprenda do Seu Jeito", page_icon="🎓", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Nunito+Sans:wght@400;600;700&display=swap');

:root {
    --purple: #7c3aed;
    --purple-light: #ede9fe;
    --yellow: #fbbf24;
    --yellow-light: #fef9c3;
    --pink: #f472b6;
    --green: #34d399;
    --bg: #f8f7ff;
    --white: #ffffff;
    --text: #1e1b4b;
    --muted: #6b7280;
    --border: #e5e7eb;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Nunito', sans-serif;
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
    background: rgba(248,247,255,0.92); backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--border);
}
.nav-logo { font-weight: 900; font-size: 1.4rem; color: var(--purple); }
.nav-logo span { color: var(--yellow); }
.nav-links { display: flex; gap: 2rem; }
.nav-links a { color: var(--muted); text-decoration: none; font-size: 0.9rem; font-weight: 700; transition: color 0.3s; }
.nav-links a:hover { color: var(--purple); }
.nav-btns { display: flex; gap: 0.75rem; align-items: center; }
.nav-login { color: var(--purple); text-decoration: none; font-weight: 700; font-size: 0.9rem; }
.nav-cta { background: var(--purple); color: white; padding: 0.6rem 1.5rem; border-radius: 50px; font-size: 0.875rem; font-weight: 800; text-decoration: none; }

/* HERO */
.hero { padding: 8rem 6% 4rem; display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 4rem; align-items: center; }
.hero-tag { display: inline-flex; align-items: center; gap: 0.5rem; background: var(--yellow-light); color: #92400e; border-radius: 50px; padding: 0.4rem 1rem; font-size: 0.8rem; font-weight: 800; margin-bottom: 1.5rem; }
.hero h1 { font-size: clamp(2.5rem, 4.5vw, 4rem); font-weight: 900; line-height: 1.15; color: var(--text); margin-bottom: 1.5rem; }
.hero h1 span { color: var(--purple); }
.hero h1 em { font-style: normal; background: linear-gradient(135deg, var(--purple), var(--pink)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.hero p { color: var(--muted); font-size: 1rem; line-height: 1.75; margin-bottom: 2rem; font-family: 'Nunito Sans', sans-serif; }
.hero-btns { display: flex; gap: 1rem; flex-wrap: wrap; margin-bottom: 2rem; }
.btn-purple { background: var(--purple); color: white; padding: 0.9rem 2rem; border-radius: 14px; font-weight: 800; text-decoration: none; font-size: 1rem; transition: all 0.3s; box-shadow: 0 8px 24px rgba(124,58,237,0.3); }
.btn-purple:hover { transform: translateY(-2px); box-shadow: 0 14px 30px rgba(124,58,237,0.4); }
.btn-ghost { background: white; color: var(--text); border: 2px solid var(--border); padding: 0.9rem 1.5rem; border-radius: 14px; font-weight: 800; text-decoration: none; font-size: 0.95rem; transition: all 0.3s; }
.btn-ghost:hover { border-color: var(--purple); color: var(--purple); }
.hero-stats { display: flex; gap: 2rem; flex-wrap: wrap; }
.h-stat .num { font-size: 1.4rem; font-weight: 900; color: var(--text); }
.h-stat .label { font-size: 0.8rem; color: var(--muted); font-family: 'Nunito Sans', sans-serif; }

.hero-visual { position: relative; }
.hero-card-main {
    background: var(--purple); border-radius: 24px; padding: 2rem;
    color: white; position: relative; overflow: hidden;
}
.hero-card-main::before { content: ''; position: absolute; top: -20%; right: -20%; width: 200px; height: 200px; border-radius: 50%; background: rgba(255,255,255,0.07); }
.hcm-label { font-size: 0.8rem; opacity: 0.7; margin-bottom: 0.5rem; }
.hcm-title { font-size: 1.1rem; font-weight: 900; margin-bottom: 1.5rem; }
.hcm-students { display: flex; gap: 0.5rem; align-items: center; margin-bottom: 1rem; }
.student-avatars { display: flex; }
.s-av { width: 32px; height: 32px; border-radius: 50%; border: 2px solid var(--purple); background: linear-gradient(135deg, #f472b6, #fb923c); display: flex; align-items: center; justify-content: center; font-size: 0.7rem; font-weight: 800; color: white; margin-left: -8px; }
.s-av:first-child { margin-left: 0; }
.hcm-progress { background: rgba(255,255,255,0.2); border-radius: 50px; height: 8px; margin-bottom: 0.5rem; }
.hcm-progress-fill { height: 100%; border-radius: 50px; background: var(--yellow); width: 67%; }
.hcm-perc { font-size: 0.8rem; opacity: 0.8; }

.float-card { position: absolute; background: white; border-radius: 16px; padding: 1rem 1.2rem; box-shadow: 0 12px 40px rgba(0,0,0,0.1); border: 1px solid var(--border); }
.float-card.top { top: -20px; right: -20px; }
.float-card.bottom { bottom: -20px; left: -20px; }
.fc-icon { font-size: 1.2rem; margin-bottom: 0.25rem; }
.fc-text { font-weight: 800; font-size: 0.85rem; color: var(--text); }
.fc-sub { font-size: 0.75rem; color: var(--muted); }

/* BRANDS */
.brands-section { padding: 2rem 6%; background: white; border-top: 1px solid var(--border); display: flex; align-items: center; justify-content: center; gap: 4rem; flex-wrap: wrap; }
.brand-item { color: #c0c0d0; font-weight: 900; font-size: 1rem; }

/* SEARCH */
.search-section { padding: 4rem 6%; }
.search-wrap { background: white; border-radius: 20px; padding: 2rem; border: 1px solid var(--border); display: flex; gap: 1rem; align-items: center; max-width: 700px; margin: 0 auto; box-shadow: 0 8px 40px rgba(0,0,0,0.06); }
.search-input { flex: 1; border: none; outline: none; font-size: 1rem; font-family: 'Nunito', sans-serif; color: var(--text); }
.search-btn { background: var(--purple); color: white; border: none; padding: 0.8rem 1.8rem; border-radius: 12px; font-weight: 800; font-size: 0.9rem; cursor: pointer; font-family: 'Nunito', sans-serif; }

/* BENEFITS */
.benefits-section { padding: 5rem 6%; }
.section-tag { display: inline-block; background: var(--purple-light); color: var(--purple); padding: 0.3rem 1rem; border-radius: 50px; font-size: 0.8rem; font-weight: 800; margin-bottom: 1rem; }
.section-title-left { font-size: clamp(1.8rem, 3.5vw, 2.8rem); font-weight: 900; color: var(--text); margin-bottom: 1rem; line-height: 1.2; }
.section-title-left span { color: var(--purple); }
.benefits-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-top: 2.5rem; }
.benefit-card { background: white; border: 1px solid var(--border); border-radius: 20px; padding: 1.8rem; transition: all 0.3s; }
.benefit-card:hover { transform: translateY(-4px); box-shadow: 0 16px 40px rgba(0,0,0,0.08); border-color: var(--purple-light); }
.benefit-icon { width: 48px; height: 48px; border-radius: 14px; background: var(--purple-light); display: flex; align-items: center; justify-content: center; font-size: 1.3rem; margin-bottom: 1rem; }
.benefit-title { font-weight: 800; font-size: 1rem; color: var(--text); margin-bottom: 0.5rem; }
.benefit-desc { color: var(--muted); font-size: 0.875rem; line-height: 1.7; font-family: 'Nunito Sans', sans-serif; }
.benefit-num { font-size: 1.5rem; font-weight: 900; color: var(--purple); margin-top: 1rem; }

/* COURSES */
.courses-section { padding: 5rem 6%; background: var(--text); }
.courses-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 2.5rem; }
.courses-header h2 { font-size: clamp(1.8rem, 3vw, 2.5rem); font-weight: 900; color: white; }
.courses-header a { color: var(--yellow); text-decoration: none; font-weight: 800; font-size: 0.9rem; }
.courses-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; }
.course-card { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08); border-radius: 20px; overflow: hidden; transition: all 0.3s; }
.course-card:hover { transform: translateY(-4px); background: rgba(255,255,255,0.08); }
.course-thumb { height: 160px; display: flex; align-items: center; justify-content: center; font-size: 3rem; position: relative; }
.thumb-1 { background: linear-gradient(135deg, #1e1b4b, #4c1d95); }
.thumb-2 { background: linear-gradient(135deg, #14532d, #166534); }
.thumb-3 { background: linear-gradient(135deg, #7c2d12, #9a3412); }
.course-level { position: absolute; top: 12px; left: 12px; background: rgba(0,0,0,0.5); color: white; padding: 0.2rem 0.6rem; border-radius: 6px; font-size: 0.7rem; font-weight: 700; backdrop-filter: blur(4px); }
.course-price-tag { position: absolute; top: 12px; right: 12px; background: var(--yellow); color: #92400e; padding: 0.2rem 0.6rem; border-radius: 6px; font-size: 0.8rem; font-weight: 800; }
.course-body { padding: 1.5rem; }
.course-cat { color: var(--yellow); font-size: 0.75rem; font-weight: 800; letter-spacing: 0.5px; text-transform: uppercase; margin-bottom: 0.5rem; }
.course-title { font-weight: 800; color: white; font-size: 1rem; margin-bottom: 0.5rem; line-height: 1.4; }
.course-meta { display: flex; justify-content: space-between; color: rgba(255,255,255,0.4); font-size: 0.8rem; font-family: 'Nunito Sans', sans-serif; }

/* TEACHER */
.teacher-section { padding: 5rem 6%; display: grid; grid-template-columns: 1fr 1fr; gap: 5rem; align-items: center; }
.teacher-visual { background: linear-gradient(135deg, var(--purple), #4c1d95); border-radius: 24px; padding: 3rem; text-align: center; color: white; }
.teacher-avatar { width: 100px; height: 100px; border-radius: 50%; background: rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; font-size: 3rem; margin: 0 auto 1.5rem; }
.teacher-name { font-size: 1.3rem; font-weight: 900; margin-bottom: 0.25rem; }
.teacher-role { opacity: 0.7; font-size: 0.85rem; margin-bottom: 2rem; }
.teacher-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
.ts-item .ts-num { font-size: 1.5rem; font-weight: 900; color: var(--yellow); }
.ts-item .ts-label { font-size: 0.75rem; opacity: 0.7; }
.teacher-text h2 { font-size: clamp(1.8rem, 3vw, 2.5rem); font-weight: 900; color: var(--text); margin-bottom: 1.5rem; line-height: 1.2; }
.teacher-text h2 span { color: var(--purple); }
.teacher-text p { color: var(--muted); line-height: 1.7; margin-bottom: 1rem; font-family: 'Nunito Sans', sans-serif; }
.teacher-benefits { list-style: none; margin-top: 1.5rem; display: flex; flex-direction: column; gap: 0.75rem; }
.teacher-benefits li { display: flex; align-items: center; gap: 0.75rem; font-weight: 700; font-size: 0.9rem; }
.tb-check { width: 24px; height: 24px; border-radius: 50%; background: var(--purple); display: flex; align-items: center; justify-content: center; color: white; font-size: 0.7rem; flex-shrink: 0; }

/* TESTIMONIALS */
.testimonials-section { padding: 5rem 6%; background: var(--purple-light); }
.t-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-top: 2.5rem; }
.t-card { background: white; border-radius: 20px; padding: 2rem; border: 1px solid rgba(124,58,237,0.1); }
.t-stars { color: var(--yellow); font-size: 1rem; margin-bottom: 1rem; }
.t-text { color: var(--muted); font-size: 0.875rem; line-height: 1.7; margin-bottom: 1.5rem; font-family: 'Nunito Sans', sans-serif; }
.t-author { display: flex; align-items: center; gap: 0.75rem; }
.t-av { width: 40px; height: 40px; border-radius: 50%; background: linear-gradient(135deg, var(--purple), var(--pink)); display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; font-size: 0.85rem; flex-shrink: 0; }
.t-name { font-weight: 800; font-size: 0.875rem; }
.t-role { color: var(--muted); font-size: 0.8rem; }

/* FAQ */
.faq-section { padding: 5rem 6%; max-width: 800px; margin: 0 auto; }
.faq-item { background: white; border: 1px solid var(--border); border-radius: 16px; padding: 1.5rem; margin-bottom: 1rem; }
.faq-q { font-weight: 800; margin-bottom: 0.75rem; color: var(--text); display: flex; align-items: center; gap: 0.5rem; }
.faq-q::before { content: '?'; background: var(--purple); color: white; width: 22px; height: 22px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; flex-shrink: 0; }
.faq-a { color: var(--muted); font-size: 0.875rem; line-height: 1.7; font-family: 'Nunito Sans', sans-serif; }

/* CTA */
.cta-section { margin: 0 4% 4rem; border-radius: 28px; padding: 5rem 3rem; background: var(--purple); text-align: center; color: white; position: relative; overflow: hidden; }
.cta-section::before { content: '🎓'; position: absolute; top: -20px; right: 5%; font-size: 8rem; opacity: 0.08; }
.cta-section::after { content: '📚'; position: absolute; bottom: -20px; left: 5%; font-size: 8rem; opacity: 0.08; }
.cta-section h2 { font-size: clamp(2rem, 4vw, 3rem); font-weight: 900; margin-bottom: 1rem; }
.cta-section p { font-size: 1rem; opacity: 0.8; margin-bottom: 2rem; }
.btn-yellow { background: var(--yellow); color: #92400e; padding: 1rem 2.5rem; border-radius: 14px; font-weight: 900; font-size: 1rem; text-decoration: none; transition: all 0.3s; display: inline-block; }
.btn-yellow:hover { transform: translateY(-3px); box-shadow: 0 12px 30px rgba(0,0,0,0.2); }

/* FOOTER */
.footer { padding: 3rem 6%; background: var(--text); color: white; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; }
.footer-logo { font-weight: 900; font-size: 1.2rem; }
.footer-logo span { color: var(--yellow); }
.footer-links { display: flex; gap: 2rem; }
.footer-links a { color: rgba(255,255,255,0.4); text-decoration: none; font-size: 0.85rem; font-weight: 700; }
.footer-copy { color: rgba(255,255,255,0.3); font-size: 0.8rem; }

@media (max-width: 900px) {
    .hero, .teacher-section { grid-template-columns: 1fr; }
    .benefits-grid, .courses-grid, .t-grid { grid-template-columns: 1fr; }
}
</style>

<nav class="nav">
    <div class="nav-logo">Edu<span>Vibe</span></div>
    <div class="nav-links">
        <a href="#">Cursos</a><a href="#">Professores</a><a href="#">Ofertas</a><a href="#">Contato</a>
    </div>
    <div class="nav-btns">
        <a href="#" class="nav-login">Entrar</a>
        <a href="#" class="nav-cta">Free Trial</a>
    </div>
</nav>

<section class="hero">
    <div>
        <div class="hero-tag">🏆 Plataforma #1 de Aprendizado Online</div>
        <h1>Desenvolva suas<br>habilidades de um<br>jeito <em>novo e único</em></h1>
        <p>Acesse mais de 1.500 cursos com os melhores professores do Brasil. Aprenda no seu ritmo, certificado reconhecido pelo mercado.</p>
        <div class="hero-btns">
            <a href="#" class="btn-purple">Explorar Cursos →</a>
            <a href="#" class="btn-ghost">🎓 Seja Professor</a>
        </div>
        <div class="hero-stats">
            <div class="h-stat"><div class="num">1.5K+</div><div class="label">Cursos disponíveis</div></div>
            <div class="h-stat"><div class="num">50K+</div><div class="label">Alunos ativos</div></div>
            <div class="h-stat"><div class="num">98%</div><div class="label">Satisfação</div></div>
        </div>
    </div>
    <div class="hero-visual">
        <div class="hero-card-main">
            <div class="hcm-label">🎯 Continuando seu aprendizado</div>
            <div class="hcm-title">UX/UI Design Avançado</div>
            <div class="hcm-students">
                <div class="student-avatars">
                    <div class="s-av">A</div><div class="s-av">B</div><div class="s-av">C</div>
                </div>
                <span style="font-size:0.8rem;opacity:0.8;">+1.2K estudando agora</span>
            </div>
            <div class="hcm-progress"><div class="hcm-progress-fill"></div></div>
            <div class="hcm-perc">67% concluído — Continue de onde parou!</div>
        </div>
        <div class="float-card top">
            <div class="fc-icon">⭐</div>
            <div class="fc-text">4.9/5.0</div>
            <div class="fc-sub">Avaliação dos alunos</div>
        </div>
        <div class="float-card bottom">
            <div class="fc-icon">📜</div>
            <div class="fc-text">Certificado Incluso</div>
            <div class="fc-sub">Reconhecido pelo mercado</div>
        </div>
    </div>
</section>

<div class="brands-section">
    <span style="color:var(--muted);font-size:0.8rem;font-weight:800;text-transform:uppercase;letter-spacing:1px;">Parceiros</span>
    <div class="brand-item">Duolingo</div>
    <div class="brand-item">Microsoft</div>
    <div class="brand-item">Magic Leap</div>
    <div class="brand-item">CodeAcademy</div>
    <div class="brand-item">LinkedIn</div>
</div>

<section class="search-section">
    <div style="text-align:center;margin-bottom:2rem;">
        <div class="section-tag">🔍 Encontre seu Curso</div>
        <div class="section-title-left" style="text-align:center;">Pesquisar em mais de <span>1.500 cursos</span></div>
    </div>
    <div class="search-wrap">
        <span style="font-size:1.2rem;">🔍</span>
        <input class="search-input" placeholder="Pesquisar por curso, habilidade ou professor..." />
        <button class="search-btn">Buscar</button>
    </div>
</section>

<section class="benefits-section">
    <div class="section-tag">✨ Vantagens</div>
    <div class="section-title-left">Os benefícios da<br>nossa <span>plataforma</span></div>
    <div class="benefits-grid">
        <div class="benefit-card">
            <div class="benefit-icon">🎓</div>
            <div class="benefit-title">Formação Certificada</div>
            <div class="benefit-desc">Certificados reconhecidos pelas maiores empresas do mercado. Adicione ao seu LinkedIn imediatamente.</div>
            <div class="benefit-num">500+</div>
            <div style="font-size:0.8rem;color:var(--muted);">certificações disponíveis</div>
        </div>
        <div class="benefit-card">
            <div class="benefit-icon">⏰</div>
            <div class="benefit-title">Aprenda no Seu Ritmo</div>
            <div class="benefit-desc">Cursos disponíveis 24/7. Assista offline, pause e continue quando quiser. Sem prazo de validade.</div>
            <div class="benefit-num">24/7</div>
            <div style="font-size:0.8rem;color:var(--muted);">acesso ilimitado</div>
        </div>
        <div class="benefit-card">
            <div class="benefit-icon">🌍</div>
            <div class="benefit-title">Múltiplos Idiomas</div>
            <div class="benefit-desc">Cursos em português, inglês e espanhol com legendas automáticas em mais de 20 idiomas.</div>
            <div class="benefit-num">20+</div>
            <div style="font-size:0.8rem;color:var(--muted);">idiomas disponíveis</div>
        </div>
    </div>
</section>

<section class="courses-section">
    <div class="courses-header">
        <h2>Nossos Cursos Populares</h2>
        <a href="#">Ver todos os cursos →</a>
    </div>
    <div class="courses-grid">
        <div class="course-card">
            <div class="course-thumb thumb-1">🎨<span class="course-level">Iniciante</span><span class="course-price-tag">R$297</span></div>
            <div class="course-body">
                <div class="course-cat">UX/UI Design</div>
                <div class="course-title">Web Design & Desenvolvimento</div>
                <div class="course-meta"><span>⭐ 4.9 (2.3K)</span><span>42 horas</span></div>
            </div>
        </div>
        <div class="course-card">
            <div class="course-thumb thumb-2">📊<span class="course-level">Avançado</span><span class="course-price-tag">R$497</span></div>
            <div class="course-body">
                <div class="course-cat">Data Science</div>
                <div class="course-title">Workbench & Business Intelligence</div>
                <div class="course-meta"><span>⭐ 4.8 (1.8K)</span><span>38 horas</span></div>
            </div>
        </div>
        <div class="course-card">
            <div class="course-thumb thumb-3">🐍<span class="course-level">Intermediário</span><span class="course-price-tag">R$397</span></div>
            <div class="course-body">
                <div class="course-cat">Programação</div>
                <div class="course-title">Python para Data Analysis</div>
                <div class="course-meta"><span>⭐ 4.9 (3.1K)</span><span>55 horas</span></div>
            </div>
        </div>
    </div>
</section>

<section class="teacher-section">
    <div class="teacher-visual">
        <div class="teacher-avatar">👨‍🏫</div>
        <div class="teacher-name">Prof. Marcus Oliveira</div>
        <div class="teacher-role">Especialista em UX Design & Tecnologia</div>
        <div class="teacher-stats">
            <div class="ts-item"><div class="ts-num">12K+</div><div class="ts-label">Alunos</div></div>
            <div class="ts-item"><div class="ts-num">4.9</div><div class="ts-label">Avaliação</div></div>
            <div class="ts-item"><div class="ts-num">18</div><div class="ts-label">Cursos</div></div>
        </div>
    </div>
    <div class="teacher-text">
        <h2>Quer <span>ensinar</span> e ganhar dinheiro com o que sabe?</h2>
        <p>Na EduVibe, você tem toda a estrutura para criar e vender seus cursos. Sem precisar se preocupar com tecnologia, pagamentos ou marketing.</p>
        <ul class="teacher-benefits">
            <li><div class="tb-check">✓</div>Plataforma completa para criar cursos</li>
            <li><div class="tb-check">✓</div>Pagamentos automáticos todo mês</li>
            <li><div class="tb-check">✓</div>Suporte de marketing e vendas</li>
            <li><div class="tb-check">✓</div>Comunidade de professores exclusiva</li>
        </ul>
        <a href="#" class="btn-purple" style="display:inline-block;margin-top:1.5rem;">Tornar-me Professor →</a>
    </div>
</section>

<section class="testimonials-section">
    <div style="text-align:center;">
        <div class="section-tag">💬 Depoimentos</div>
        <div class="section-title-left" style="text-align:center;">O que nossos <span>alunos</span> dizem</div>
    </div>
    <div class="t-grid">
        <div class="t-card"><div class="t-stars">★★★★★</div><div class="t-text">"Consegui meu primeiro emprego como UX Designer em 4 meses de estudo na EduVibe. Os cursos são incrivelmente práticos!"</div><div class="t-author"><div class="t-av">LM</div><div><div class="t-name">Laura Mendes</div><div class="t-role">UX Designer Jr.</div></div></div></div>
        <div class="t-card"><div class="t-stars">★★★★★</div><div class="t-text">"Saí de analista financeiro para Cientista de Dados. O curso de Python foi decisivo. Meu salário dobrou em 8 meses."</div><div class="t-author"><div class="t-av">FG</div><div><div class="t-name">Felipe Gomes</div><div class="t-role">Data Scientist</div></div></div></div>
        <div class="t-card"><div class="t-stars">★★★★★</div><div class="t-text">"Qualidade dos professores é excepcional. Aprendes na teoria e na prática com projetos reais. Vale cada centavo!"</div><div class="t-author"><div class="t-av">CA</div><div><div class="t-name">Camila Alves</div><div class="t-role">Desenvolvedora Front-end</div></div></div></div>
    </div>
</section>

<section class="faq-section">
    <div style="text-align:center;margin-bottom:2.5rem;">
        <div class="section-tag">❓ FAQ</div>
        <div class="section-title-left" style="text-align:center;">Tire suas <span>dúvidas</span></div>
    </div>
    <div class="faq-item"><div class="faq-q">Os certificados são reconhecidos pelo mercado?</div><div class="faq-a">Sim! Nossos certificados são parceiros oficiais da Microsoft, Google e LinkedIn. Amplamente reconhecidos por empresas de tecnologia no Brasil e exterior.</div></div>
    <div class="faq-item"><div class="faq-q">Posso assistir offline?</div><div class="faq-a">Sim! No app mobile você pode baixar as aulas para assistir sem internet. Perfeito para estudar no transporte ou sem conexão.</div></div>
    <div class="faq-item"><div class="faq-q">Tem garantia de satisfação?</div><div class="faq-a">7 dias de garantia total. Se não gostar, devolvemos 100% do seu dinheiro, sem perguntas.</div></div>
    <div class="faq-item"><div class="faq-q">Posso parcelar o pagamento?</div><div class="faq-a">Sim! Em até 12x sem juros no cartão de crédito. Ou à vista com 20% de desconto.</div></div>
</section>

<div class="cta-section">
    <h2>Comece sua jornada de<br>aprendizado hoje!</h2>
    <p>Mais de 50.000 alunos já transformaram suas carreiras. Junte-se a eles!</p>
    <a href="#" class="btn-yellow">🚀 Começar Agora — 7 dias grátis</a>
</div>

<footer class="footer">
    <div class="footer-logo">Edu<span>Vibe</span></div>
    <div class="footer-links"><a href="#">Privacidade</a><a href="#">Termos</a><a href="#">Blog</a><a href="#">Suporte</a></div>
    <div class="footer-copy">© 2025 EduVibe. Todos os direitos reservados.</div>
</footer>
""", unsafe_allow_html=True)
