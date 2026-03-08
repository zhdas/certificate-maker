import base64
from pathlib import Path
import html
import streamlit as st


def _logo_data_uri() -> str:
    logo_path = Path(__file__).with_name('logo.png')
    if not logo_path.exists():
        return ''
    encoded = base64.b64encode(logo_path.read_bytes()).decode('utf-8')
    return f'data:image/png;base64,{encoded}'


def set_page_style():
    st.markdown(
        """
        <style>
        :root {
            --bg: #07111f;
            --bg-2: #0b1832;
            --panel: rgba(10, 21, 40, 0.80);
            --stroke: rgba(255, 255, 255, 0.10);
            --text: #eef6ff;
            --muted: rgba(238, 246, 255, 0.72);
            --cyan: #86eeff;
            --blue: #8cb7ff;
        }

        .stApp {
            background:
                radial-gradient(circle at 12% 12%, rgba(0, 217, 255, 0.16), transparent 26%),
                radial-gradient(circle at 88% 18%, rgba(96, 165, 250, 0.16), transparent 28%),
                linear-gradient(135deg, var(--bg) 0%, var(--bg-2) 100%);
            color: var(--text);
        }

        .block-container {
            max-width: 840px;
            padding-top: 1.2rem;
            padding-bottom: 3rem;
        }

        .stApp [data-testid='stHeader'] { background: transparent; }
        h1, h2, h3, p, span, div, label { color: var(--text); }

        .hero-card, .info-card, .file-card {
            border: 1px solid var(--stroke);
            background: var(--panel);
            border-radius: 30px;
            backdrop-filter: blur(18px);
            box-shadow: 0 24px 60px rgba(0, 0, 0, 0.26);
        }

        .hero-card { padding: 28px; margin-bottom: 16px; }
        .info-card, .file-card { padding: 22px; margin-top: 16px; }

        .brand-row {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 22px;
        }

        .brand-logo {
            width: 64px;
            height: 64px;
            object-fit: contain;
            border-radius: 18px;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.08);
            padding: 10px;
        }

        .brand-kicker {
            text-transform: uppercase;
            letter-spacing: .24em;
            font-size: 12px;
            color: rgba(134, 238, 255, 0.82);
            margin-bottom: 5px;
        }

        .brand-title {
            font-size: clamp(2rem, 5vw, 3.4rem);
            font-weight: 800;
            line-height: 1.05;
            margin: 0;
        }

        .brand-subtitle {
            color: var(--muted);
            font-size: 1.06rem;
            line-height: 1.8;
            margin-top: 12px;
            max-width: 640px;
        }

        .section-kicker {
            text-transform: uppercase;
            letter-spacing: .22em;
            color: rgba(134, 238, 255, 0.76);
            font-size: 12px;
            margin-bottom: 10px;
        }

        .instruction-list {
            margin: 0;
            padding-left: 1.25rem;
            color: var(--text);
        }

        .instruction-list li {
            margin: 0 0 12px 0;
            line-height: 1.8;
            color: var(--muted);
            font-size: 1rem;
        }

        [data-testid='stFileUploader'] {
            margin-top: 14px;
            margin-bottom: 12px;
        }

        [data-testid='stFileUploaderDropzone'] {
            border: 1px dashed rgba(134, 238, 255, 0.34);
            border-radius: 26px;
            background: linear-gradient(180deg, rgba(134,238,255,0.08), rgba(255,255,255,0.03));
            padding: 1.2rem 1.1rem;
        }

        [data-testid='stFileUploaderDropzoneInstructions'] > div,
        [data-testid='stFileUploaderDropzoneInstructions'] small,
        [data-testid='stFileUploaderDropzone'] small {
            visibility: hidden;
        }

        [data-testid='stFileUploaderDropzoneInstructions']::before {
            content: 'Перетащите файл сюда';
            display: block;
            visibility: visible;
            color: var(--text);
            font-size: 1.15rem;
            font-weight: 700;
            margin-bottom: 6px;
        }

        [data-testid='stFileUploaderDropzoneInstructions']::after {
            content: 'или нажмите кнопку для выбора Excel-файла (.xlsx)';
            display: block;
            visibility: visible;
            color: var(--muted);
            font-size: 0.95rem;
        }

        [data-testid='stFileUploader'] button,
        .stButton > button,
        .stDownloadButton > button {
            border-radius: 20px;
            border: 0;
            min-height: 3.5rem;
            font-weight: 800;
        }

        [data-testid='stFileUploader'] button,
        .stButton > button {
            background: linear-gradient(90deg, var(--cyan) 0%, var(--blue) 100%);
            color: #07111f;
            box-shadow: 0 18px 44px rgba(117, 185, 255, 0.22);
        }

        .stDownloadButton > button {
            background: rgba(255,255,255,0.96);
            color: #07111f;
        }

        .file-name {
            font-size: 1.12rem;
            font-weight: 700;
            margin-bottom: 14px;
        }

        .summary-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 12px;
            margin-top: 10px;
        }

        .summary-card {
            border-radius: 22px;
            border: 1px solid var(--stroke);
            background: rgba(255,255,255,0.05);
            padding: 16px;
        }

        .summary-label {
            color: var(--muted);
            font-size: 13px;
            margin-bottom: 6px;
        }

        .summary-value {
            color: var(--text);
            font-size: 1.02rem;
            font-weight: 700;
            word-break: break-word;
        }

        .hint {
            color: var(--muted);
            line-height: 1.75;
        }

        @media (max-width: 760px) {
            .summary-grid { grid-template-columns: 1fr; }
            .brand-row { align-items: flex-start; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_header():
    logo_uri = _logo_data_uri()
    logo_html = f'<img class="brand-logo" src="{logo_uri}" alt="ADN SHORING logo">' if logo_uri else ''
    st.markdown(
        f'''
        <section class="hero-card">
            <div class="brand-row">
                {logo_html}
                <div>
                    <div class="brand-kicker">Workspace</div>
                    <h1 class="brand-title">ADN SHORING</h1>
                </div>
            </div>
            <p class="brand-subtitle">
                Загрузите PACKING LIST, нажмите кнопку генерации, и система создаст единый PDF из всех страниц файла.
            </p>
        </section>
        ''',
        unsafe_allow_html=True,
    )


def render_instruction():
    st.markdown(
        '''
        <section class="info-card">
            <div class="section-kicker">Инструкция</div>
            <ol class="instruction-list">
                <li>Загрузите файл.</li>
                <li>Нажмите кнопку генерации.</li>
                <li>Система создаст PDF из всех страниц.</li>
            </ol>
        </section>
        ''',
        unsafe_allow_html=True,
    )


def render_upload_hint():
    st.markdown(
        '''
        <section class="file-card">
            <div class="section-kicker">Файл ещё не загружен</div>
            <div class="hint">После загрузки появится кнопка генерации PDF. Когда генерация завершится, ниже появится кнопка для скачивания готового PDF.</div>
        </section>
        ''',
        unsafe_allow_html=True,
    )


def render_file_ready(file_name: str, summary: dict):
    items = [
        ('Файл', html.escape(file_name)),
        ('Количество листов', str(summary.get('sheets', '—'))),
        ('Компания', html.escape(str(summary.get('company') or '—'))),
    ]
    cards = ''.join(
        f'<div class="summary-card"><div class="summary-label">{label}</div><div class="summary-value">{value}</div></div>'
        for label, value in items
    )
    st.markdown(
        f'''
        <section class="file-card">
            <div class="section-kicker">Файл загружен</div>
            <div class="file-name">{html.escape(file_name)}</div>
            <div class="summary-grid">{cards}</div>
        </section>
        ''',
        unsafe_allow_html=True,
    )
