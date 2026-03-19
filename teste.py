import streamlit as st

def render():
    """Renderiza o template Sprint - Evento/Mentoria Style (Joel Jota)"""

    st.set_page_config(
        page_title="Sprint | Seja o Profissional Mais Desejado",
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,400;0,600;0,700;0,800;0,900;1,700;1,800&family=Barlow:wght@400;500;600;700&display=swap');

        * { margin: 0; padding: 0; box-sizing: border-box; }

        :root {
            --verde:   #8AFF00;
            --escuro:  #0a0a0a;
            --cinza:   #141414;
            --cinza2:  #1e1e1e;
            --texto:   #e0e0e0;
        }

        html, body, [data-testid="stAppViewContainer"] {
            background: var(--escuro);
            color: var(--texto);
            font-family: 'Barlow', sans-serif;
        }

        [data-testid="stHeader"],
        [data-testid="stToolbarActions"],
        [data-testid="stDecoration"],
        footer { display: none !important; }

        .block-container { padding: 0 !important; max-width: 100% !important; }

        /* ── HERO ── */
        .hero {
            background: var(--escuro);
            position: relative;
            overflow: hidden;
            padding: 70px 8% 60px;
            display: flex;
            align-items: center;
            gap: 40px;
            min-height: 520px;
        }
        .hero::before {
            content: '';
            position: absolute;
            inset: 0;
            background:
                radial-gradient(ellipse 60% 80% at 70% 50%, rgba(138,255,0,0.12) 0%, transparent 70%),
                radial-gradient(ellipse 40% 60% at 80% 20%, rgba(138,255,0,0.08) 0%, transparent 60%);
        }
        .hero-text { flex: 1; position: relative; z-index: 2; }
        .hero-logo {
            font-family: 'Barlow Condensed', sans-serif;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 3px;
            color: var(--verde);
            text-transform: uppercase;
            margin-bottom: 6px;
        }
        .hero-logo span {
            font-size: 28px;
            font-weight: 900;
            letter-spacing: 4px;
            display: block;
            color: var(--verde);
            text-shadow: 0 0 30px rgba(138,255,0,0.5);
        }
        .hero-h1 {
            font-family: 'Barlow Condensed', sans-serif;
            font-size: clamp(36px, 5.5vw, 62px);
            font-weight: 900;
            line-height: 1.0;
            color: #ffffff;
            margin: 20px 0 16px;
            text-transform: uppercase;
        }
        .hero-h1 em {
            font-style: normal;
            color: var(--verde);
        }
        .hero-desc {
            font-size: 15px;
            line-height: 1.7;
            color: #aaa;
            max-width: 480px;
            margin-bottom: 32px;
        }
        .hero-desc strong { color: #fff; }
        .btn-verde {
            display: inline-block;
            background: var(--verde);
            color: #0a0a0a !important;
            font-family: 'Barlow Condensed', sans-serif;
            font-weight: 800;
            font-size: 16px;
            letter-spacing: 1px;
            text-transform: uppercase;
            padding: 16px 44px;
            border-radius: 6px;
            text-decoration: none !important;
            transition: all 0.3s;
            box-shadow: 0 0 30px rgba(138,255,0,0.3);
        }
        .btn-verde:hover {
            background: #a0ff20;
            box-shadow: 0 0 50px rgba(138,255,0,0.5);
            transform: translateY(-2px);
        }
        .hero-img {
            flex: 0 0 420px;
            position: relative;
            z-index: 2;
        }
        .hero-img img {
            width: 100%;
            border-radius: 12px;
            filter: brightness(1.05) contrast(1.05);
        }
        .hero-badge {
            position: absolute;
            bottom: 20px;
            right: 10px;
            width: 90px;
            height: 90px;
            background: var(--verde);
            border-radius: 50%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-family: 'Barlow Condensed', sans-serif;
            font-weight: 900;
            font-size: 11px;
            color: #000;
            text-align: center;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            box-shadow: 0 0 25px rgba(138,255,0,0.5);
        }
        .hero-badge span { font-size: 16px; font-weight: 900; }

        /* ── BANNER VERDE ── */
        .banner-verde {
            background: var(--verde);
            padding: 14px 8%;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .banner-verde p {
            font-family: 'Barlow Condensed', sans-serif;
            font-size: 18px;
            font-weight: 700;
            color: #000;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .banner-check {
            width: 28px;
            height: 28px;
            background: #000;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--verde);
            font-size: 14px;
            font-weight: 900;
            flex-shrink: 0;
        }

        /* ── PARA QUEM ── */
        .para-quem {
            padding: 80px 8%;
            background: var(--cinza);
            display: flex;
            gap: 60px;
            align-items: flex-start;
        }
        .para-quem-left { flex: 1.2; }
        .para-quem-right { flex: 1; }
        .section-label {
            font-family: 'Barlow Condensed', sans-serif;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 3px;
            color: var(--verde);
            text-transform: uppercase;
            margin-bottom: 12px;
        }
        .section-h2 {
            font-family: 'Barlow Condensed', sans-serif;
            font-size: clamp(30px, 4vw, 48px);
            font-weight: 900;
            color: #fff;
            text-transform: uppercase;
            line-height: 1.05;
            margin-bottom: 20px;
        }
        .section-h2 em { font-style: normal; color: var(--verde); }
        .para-quem-desc {
            font-size: 15px;
            line-height: 1.8;
            color: #888;
        }
        .check-item {
            display: flex;
            align-items: flex-start;
            gap: 12px;
            margin-bottom: 16px;
        }
        .check-icon {
            width: 22px;
            height: 22px;
            background: var(--verde);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #000;
            font-size: 12px;
            font-weight: 900;
            flex-shrink: 0;
            margin-top: 2px;
        }
        .check-text {
            font-size: 15px;
            color: #ccc;
            line-height: 1.5;
        }
        .check-text strong { color: #fff; }

        /* ── PILARES ── */
        .pilares {
            padding: 80px 8%;
            background: var(--escuro);
            text-align: center;
        }
        .pilares-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
            margin-top: 50px;
        }
        .pilar-card {
            background: var(--cinza2);
            border: 1px solid rgba(138,255,0,0.15);
            border-radius: 10px;
            padding: 36px 28px;
            text-align: center;
            transition: all 0.3s;
        }
        .pilar-card:hover {
            border-color: var(--verde);
            box-shadow: 0 0 30px rgba(138,255,0,0.1);
            transform: translateY(-4px);
        }
        .pilar-icon {
            font-size: 36px;
            margin-bottom: 16px;
        }
        .pilar-titulo {
            font-family: 'Barlow Condensed', sans-serif;
            font-size: 22px;
            font-weight: 800;
            color: var(--verde);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 12px;
        }
        .pilar-desc {
            font-size: 14px;
            color: #888;
            line-height: 1.7;
            margin-bottom: 16px;
        }
        .pilar-link {
            font-size: 13px;
            font-weight: 700;
            color: var(--verde);
            text-decoration: none;
            letter-spacing: 0.5px;
        }
        .pilares-cta { margin-top: 50px; }

        /* ── CTA INTERMEDIÁRIO ── */
        .cta-mid {
            background: var(--cinza);
            padding: 70px 8%;
            text-align: center;
        }
        .cta-mid-h2 {
            font-family: 'Barlow Condensed', sans-serif;
            font-size: clamp(28px, 4vw, 46px);
            font-weight: 900;
            color: #fff;
            text-transform: uppercase;
            margin-bottom: 10px;
        }
        .cta-mid-h2 em { font-style: normal; color: var(--verde); }

        /* ── OFERTA / PREÇO ── */
        .oferta {
            padding: 80px 8%;
            background: var(--escuro);
            text-align: center;
        }
        .oferta-box {
            max-width: 520px;
            margin: 40px auto 0;
            background: var(--cinza2);
            border: 2px solid rgba(138,255,0,0.25);
            border-radius: 14px;
            padding: 44px 40px;
        }
        .oferta-logo {
            font-family: 'Barlow Condensed', sans-serif;
            font-size: 20px;
            font-weight: 900;
            letter-spacing: 4px;
            color: var(--verde);
            text-transform: uppercase;
            margin-bottom: 6px;
        }
        .oferta-sub {
            font-size: 12px;
            color: #666;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 24px;
        }
        .oferta-item {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 12px;
            text-align: left;
        }
        .oferta-item-check {
            color: var(--verde);
            font-size: 16px;
            font-weight: 900;
            flex-shrink: 0;
        }
        .oferta-item-text {
            font-size: 14px;
            color: #ccc;
        }
        .oferta-item-text.destaque { color: var(--verde); font-weight: 700; }
        .oferta-divider {
            border: none;
            border-top: 1px solid rgba(255,255,255,0.08);
            margin: 24px 0;
        }
        .oferta-de {
            font-size: 14px;
            color: #666;
            text-decoration: line-through;
            margin-bottom: 4px;
        }
        .oferta-por {
            font-family: 'Barlow Condensed', sans-serif;
            font-size: 56px;
            font-weight: 900;
            color: var(--verde);
            line-height: 1;
            margin-bottom: 4px;
        }
        .oferta-por span { font-size: 28px; vertical-align: top; margin-top: 8px; display: inline-block; }
        .oferta-parcel {
            font-size: 13px;
            color: #666;
            margin-bottom: 28px;
        }
        .garantia-row {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
            flex-wrap: wrap;
        }
        .garantia-item {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 12px;
            color: #666;
        }
        .garantia-item span { font-size: 18px; }

        /* ── MENTOR ── */
        .mentor {
            padding: 80px 8%;
            background: var(--cinza);
            display: flex;
            gap: 60px;
            align-items: center;
        }
        .mentor-img {
            flex: 0 0 280px;
            position: relative;
        }
        .mentor-img img {
            width: 100%;
            border-radius: 12px;
            filter: grayscale(20%);
        }
        .mentor-img::before {
            content: '';
            position: absolute;
            inset: -3px;
            border-radius: 14px;
            background: linear-gradient(135deg, var(--verde), transparent 60%);
            z-index: -1;
        }
        .mentor-text { flex: 1; }
        .mentor-tag {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(138,255,0,0.1);
            border: 1px solid rgba(138,255,0,0.3);
            border-radius: 20px;
            padding: 6px 14px;
            font-size: 12px;
            color: var(--verde);
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            margin-bottom: 20px;
        }
        .mentor-h2 {
            font-family: 'Barlow Condensed', sans-serif;
            font-size: clamp(28px, 3.5vw, 44px);
            font-weight: 900;
            color: #fff;
            text-transform: uppercase;
            line-height: 1.1;
            margin-bottom: 20px;
        }
        .mentor-h2 em { font-style: normal; color: var(--verde); }
        .mentor-bio {
            font-size: 14px;
            color: #888;
            line-height: 1.8;
            margin-bottom: 28px;
        }

        /* ── FOOTER ── */
        .footer-sprint {
            padding: 30px 8%;
            background: #050505;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid rgba(138,255,0,0.1);
        }
        .footer-sprint p {
            font-size: 12px;
            color: #444;
            letter-spacing: 1px;
        }
        .footer-sprint a {
            font-size: 12px;
            color: #444;
            text-decoration: none;
        }
        .footer-sprint a:hover { color: var(--verde); }
    </style>
    """, unsafe_allow_html=True)

    # ── HERO ──
    st.markdown("""
    <div class="hero">
        <div class="hero-text">
            <div class="hero-logo">
                ⚡ Programa de Formação
                <span>SPRINT</span>
            </div>
            <h1 class="hero-h1">
                Seja o profissional<br>
                mais desejado e <em>bem<br>
                pago do mercado!</em>
            </h1>
            <p class="hero-desc">
                Desenvolva sua <strong>COMUNICAÇÃO</strong>, <strong>LIDERANÇA</strong> e aprenda a utilizar a
                <strong>INTELIGÊNCIA ARTIFICIAL</strong> para aumentar sua produtividade
                e ganhar mais dinheiro.
            </p>
            <a href="https://www.google.com/" target="_blank" class="btn-verde">Garantir minha vaga!</a>
        </div>
        <div class="hero-img">
            <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?w=600" alt="Mentor">
            <div class="hero-badge">
                <span>JOEL</span>
                JOTA
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── BANNER VERDE ──
    st.markdown("""
    <div class="banner-verde">
        <div class="banner-check">✓</div>
        <p>Todo nosso conhecimento reunido em um único lugar!</p>
    </div>
    """, unsafe_allow_html=True)

    # ── PARA QUEM ──
    st.markdown("""
    <div class="para-quem">
        <div class="para-quem-left">
            <p class="section-label">⚡ Sprint</p>
            <h2 class="section-h2">O evento <em>SPRINT</em><br>é ideal para:</h2>
            <p class="para-quem-desc">
                Profissionais em busca de aperfeiçoamento das habilidades interpessoais no mercado atual,
                como comunicação, liderança e a utilização de Inteligência Artificial para aumentar sua
                produtividade e ganhar mais dinheiro, se destacar e encantar a excelência.
            </p>
        </div>
        <div class="para-quem-right">
            <div class="check-item">
                <div class="check-icon">✓</div>
                <div class="check-text">Ter uma <strong>comunicação assertiva.</strong></div>
            </div>
            <div class="check-item">
                <div class="check-icon">✓</div>
                <div class="check-text">Ser um <strong>líder inteligente e estratégico.</strong></div>
            </div>
            <div class="check-item">
                <div class="check-icon">✓</div>
                <div class="check-text">Maximizar sua produtividade ao usar as ferramentas de <strong>INTELIGÊNCIA ARTIFICIAL.</strong></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── PILARES ──
    st.markdown("""
    <div class="pilares">
        <p class="section-label">Os 3 pilares</p>
        <h2 class="section-h2">Domine os <em>3 pilares</em><br>do profissional do futuro.</h2>
        <div class="pilares-grid">
            <div class="pilar-card">
                <div class="pilar-icon">🗣️</div>
                <div class="pilar-titulo">Comunicação</div>
                <p class="pilar-desc">
                    Domine as técnicas de comunicação que constroem autoridade, confiança e conexão real
                    com qualquer audiência.
                    <br><br>
                    Aprenda a sua habilidade de comunicar para vender, liderar e inspirar as pessoas.
                </p>
                <a href="#" class="pilar-link">SAIBA MAIS →</a>
            </div>
            <div class="pilar-card">
                <div class="pilar-icon">⚙️</div>
                <div class="pilar-titulo">Produtividade</div>
                <p class="pilar-desc">
                    Ferramentas de IA e sistemas inteligentes de organização para você alcançar mais
                    resultados em menos tempo.
                    <br><br>
                    Ferramentas para você otimizar e elevar sua produtividade.
                </p>
                <a href="#" class="pilar-link">SAIBA MAIS →</a>
            </div>
            <div class="pilar-card">
                <div class="pilar-icon">👑</div>
                <div class="pilar-titulo">Liderança</div>
                <p class="pilar-desc">
                    Desenvolva a capacidade de influenciar, motivar e gerar impacto com as pessoas ao seu
                    redor, na carreira e nos negócios.
                    <br><br>
                    Construção a capacidade de influenciar e gerar impacto de forma positiva.
                </p>
                <a href="#" class="pilar-link">SAIBA MAIS →</a>
            </div>
        </div>
        <div class="pilares-cta">
            <a href="https://www.google.com/" target="_blank" class="btn-verde">Quero fazer parte do Sprint!</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── CTA INTERMEDIÁRIO ──
    st.markdown("""
    <div class="cta-mid">
        <h2 class="cta-mid-h2">Não perca essa chance,<br>garanta hoje a <em>sua participação!</em></h2>
    </div>
    """, unsafe_allow_html=True)

    # ── OFERTA / PREÇO ──
    st.markdown("""
    <div class="oferta">
        <div class="oferta-box">
            <div class="oferta-logo">SPRINT</div>
            <div class="oferta-sub">Programa de Formação</div>

            <div class="oferta-item">
                <span class="oferta-item-check">✓</span>
                <span class="oferta-item-text">Evento online Sprint.</span>
            </div>
            <div class="oferta-item">
                <span class="oferta-item-check">✓</span>
                <span class="oferta-item-text">Interação com a comunidade no chat ao vivo.</span>
            </div>
            <div class="oferta-item">
                <span class="oferta-item-check">✓</span>
                <span class="oferta-item-text">Certificado de conclusão.</span>
            </div>
            <div class="oferta-item">
                <span class="oferta-item-check">✓</span>
                <span class="oferta-item-text">Conteúdos de aquecimento na plataforma.</span>
            </div>
            <div class="oferta-item">
                <span class="oferta-item-check">✓</span>
                <span class="oferta-item-text destaque">Bônus e surpresas exclusivas.</span>
            </div>

            <hr class="oferta-divider">

            <div class="oferta-de">De: R$697</div>
            <div class="oferta-por"><span>12x</span> 28,85</div>
            <div class="oferta-parcel">Ou R$297,00 à vista</div>

            <a href="https://www.google.com/" target="_blank" class="btn-verde" style="display:block;text-align:center;">
                Quero aproveitar a promoção!
            </a>

            <div class="garantia-row">
                <div class="garantia-item"><span>🔒</span> Compra Segura</div>
                <div class="garantia-item"><span>✅</span> Garantia 7 dias</div>
                <div class="garantia-item"><span>💳</span> Parcelamento</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── MENTOR ──
    st.markdown("""
    <div class="mentor">
        <div class="mentor-img">
            <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400" alt="Mentor">
        </div>
        <div class="mentor-text">
            <div class="mentor-tag">⚡ JOEL JOTA</div>
            <h2 class="mentor-h2">Quem vai ser o<br><em>meu mentor?</em></h2>
            <p class="mentor-bio">
                Criado com James Diniz e pai de três menores crianças, Joel Jota é palestrante, escritor
                e autor best-seller. Mestre em Ciências do Esporte e Bacharelando em Psicologia pela
                Universidade Norte do Paraná. Ex-atleta e fundador do Instituto Vaynerchuk.
            </p>
            <a href="https://www.google.com/" target="_blank" class="btn-verde">Garantir minha vaga!</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── FOOTER ──
    st.markdown("""
    <div class="footer-sprint">
        <p>© 2026 SPRINT · Todos os direitos reservados.</p>
        <div style="display:flex;gap:24px;">
            <a href="#">Política de Privacidade</a>
            <a href="#">Termos de Uso</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    render()
