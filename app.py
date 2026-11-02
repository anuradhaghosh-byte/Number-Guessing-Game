
import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(0, 10)

if "attempts" not in st.session_state:
    st.session_state.attempts = 3

if "selected_number" not in st.session_state:
    st.session_state.selected_number = None

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "won" not in st.session_state:
    st.session_state.won = False

if "guess_distance" not in st.session_state:
    st.session_state.guess_distance = None

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #101323, #202743, #111827);
    color: white;
}

.block-container {
    max-width: 600px;
    padding-top: 2rem;
}

h1, h2, h3, p, label {
    color: white !important;
}

.game-title {
    text-align: center;
    font-size: 38px;
    font-weight: 900;
    letter-spacing: 3px;
    color: white;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #b9c3dd;
    font-size: 15px;
    margin-bottom: 25px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 22px;
    background: rgba(255,255,255,0.06);
    padding: 20px;
}

.number-display {
    background: rgba(255,255,255,0.08);
    border: 2px solid rgba(255,255,255,0.35);
    border-radius: 18px;
    text-align: center;
    padding: 22px 10px;
    font-size: 52px;
    font-weight: 900;
    color: white;
    margin: 15px 0 20px 0;
    min-height: 105px;
}

.number-label {
    text-align: center;
    color: #d7def2;
    font-size: 14px;
    letter-spacing: 2px;
    font-weight: bold;
}

div.stButton > button {
    border-radius: 12px;
    height: 48px;
    font-size: 20px;
    font-weight: bold;
    border: 1.5px solid white;
    background: transparent;
    color: white;
    transition: 0.2s;
}

div.stButton > button:hover {
    background: white;
    color: #17203a;
    border-color: white;
}

div.stButton > button:focus {
    color: white;
    border-color: #ffffff;
}

div.stButton > button[kind="primary"] {
    background: white;
    color: #17203a;
    border: none;
    height: 50px;
    font-size: 17px;
}

div.stButton > button[kind="primary"]:hover {
    background: #dce5ff;
    color: #111827;
}

.status-text {
    text-align: center;
    color: #e5eaff;
    font-size: 16px;
    font-weight: 600;
    margin: 12px 0;
}

.result-win {
    text-align: center;
    color: #54ff9b;
    font-size: 30px;
    font-weight: 900;
    padding: 12px;
}

.result-lose {
    text-align: center;
    color: #ff7373;
    font-size: 30px;
    font-weight: 900;
    padding: 12px;
}

.footer {
    text-align: center;
    color: #8e9ab9;
    font-size: 12px;
    margin-top: 25px;
}

.stars {
    text-align: center;
    font-size: 27px;
    letter-spacing: 8px;
    margin: 8px 0;
}

.bar-track {
    height: 9px;
    width: 100%;
    background: rgba(255,255,255,0.12);
    border-radius: 20px;
    overflow: hidden;
    margin: 12px 0 22px 0;
}

.bar-fill {
    height: 100%;
    border-radius: 20px;
    transition: all 0.4s ease;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.04); }
    100% { transform: scale(1); }
}

.st-key-play_again button {
    animation: pulse 1.2s infinite;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    '<div class="game-title">🎯 NUMBER GAME</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Guess the secret number between 0 and 10</div>',
    unsafe_allow_html=True
)

# ---------------- GAME CARD ----------------
with st.container(border=True):

    st.markdown(
        '<div class="number-label">YOUR CHANCES</div>',
        unsafe_allow_html=True
    )

    # Stars
    stars = "⭐" * st.session_state.attempts
    st.markdown(
        f'<div class="stars">{stars}</div>',
        unsafe_allow_html=True
    )

    # Guess indicator bar
    if st.session_state.guess_distance is None:
        bar_color = "transparent"
        bar_width = 0
    else:
        distance = st.session_state.guess_distance
        closeness = max(0, 1 - (distance / 10))
        red = int(255 * (1 - closeness))
        green = int(255 * closeness)
        bar_color = f"rgb({red},{green},0)"
        bar_width = 100

    st.markdown(
        f"""
        <div class="bar-track">
            <div class="bar-fill"
                 style="width:{bar_width}%;background:{bar_color};">
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Main number display
    st.markdown(
        '<div class="number-label">CHOOSE YOUR NUMBER</div>',
        unsafe_allow_html=True
    )

    if st.session_state.selected_number is None:
        display_number = "?"
    else:
        display_number = str(st.session_state.selected_number)

    st.markdown(
        f'<div class="number-display">{display_number}</div>',
        unsafe_allow_html=True
    )

    # ---------------- NUMBER BUTTON LAYOUT ----------------
    number_layout = [
        [None, 0, None],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [None, 10, None]
    ]

    for row in number_layout:
        cols = st.columns(3)

        for col_index, number in enumerate(row):
            with cols[col_index]:

                if number is not None:
                    if st.button(
                        str(number),
                        key=f"number_{number}",
                        use_container_width=True,
                        disabled=st.session_state.game_over
                    ):
                        st.session_state.selected_number = number
                        st.rerun()

    st.write("")

    # ---------------- SUBMIT GUESS ----------------
    if st.button(
        "SUBMIT GUESS",
        type="primary",
        use_container_width=True,
        disabled=(
            st.session_state.game_over
            or st.session_state.selected_number is None
        )
    ):

        guess = st.session_state.selected_number
        secret = st.session_state.secret_number

        st.session_state.guess_distance = abs(guess - secret)

        if guess == secret:
            st.session_state.won = True
            st.session_state.game_over = True

        else:
            st.session_state.attempts -= 1

            if st.session_state.attempts <= 0:
                st.session_state.game_over = True
                st.session_state.won = False

        st.session_state.selected_number = None
        st.rerun()

    # ---------------- GAME RESULT ----------------
    if st.session_state.game_over:

        if st.session_state.won:

            st.markdown(
                '<div class="result-win">🎉 YOU WIN!</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="status-text">Correct number: '
                f'{st.session_state.secret_number}</div>',
                unsafe_allow_html=True
            )

            st.balloons()

        else:

            st.markdown(
                '<div class="result-lose">💔 GAME OVER</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="status-text">The correct number was '
                f'{st.session_state.secret_number}</div>',
                unsafe_allow_html=True
            )

            st.markdown("""
            <div style="text-align:center;font-size:28px;">
                🎊 🎊 🎊
            </div>
            """, unsafe_allow_html=True)

        st.write("")

        if st.button(
            "🔄 PLAY AGAIN",
            key="play_again",
            type="primary",
            use_container_width=True
        ):
            st.session_state.secret_number = random.randint(0, 10)
            st.session_state.attempts = 3
            st.session_state.selected_number = None
            st.session_state.game_over = False
            st.session_state.won = False
            st.session_state.guess_distance = None
            st.rerun()

    else:

        if st.session_state.selected_number is None:
            st.markdown(
                '<div class="status-text">Select a number to play!</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="status-text">Press SUBMIT GUESS to check your answer!</div>',
                unsafe_allow_html=True
            )

# ---------------- FOOTER ----------------
st.markdown(
    '<div class="footer">✨ Made with Python & Streamlit ✨</div>',
    unsafe_allow_html=True
)
