import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #101827, #1e293b);
    color: white;
}
.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 800;
    color: white;
}
.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 30px;
}
.game-card {
    background: #263449;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #3b4b62;
    text-align: center;
}
.stat {
    font-size: 28px;
    font-weight: bold;
    color: #38bdf8;
}
.stat-label {
    color: #cbd5e1;
    font-size: 13px;
}
.stButton > button,
.stFormSubmitButton > button {
    width: 100%;
    border-radius: 10px;
    height: 45px;
    font-weight: bold;
}
.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 35px;
}
</style>
""", unsafe_allow_html=True)


# ---------------- GAME INITIALIZATION ----------------
def new_game():
    st.session_state.python_no = random.randint(1, 10)
    st.session_state.attempts = 3
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.message = "Make your first guess!"


if "python_no" not in st.session_state:
    new_game()


# ---------------- HEADER ----------------
st.markdown(
    '<div class="main-title">🎯 Number Guessing Game</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Test your luck and guess the secret number!</div>',
    unsafe_allow_html=True
)


# ---------------- STATISTICS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="game-card">
        <div class="stat">1–10</div>
        <div class="stat-label">NUMBER RANGE</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="game-card">
        <div class="stat">{st.session_state.attempts}</div>
        <div class="stat-label">CHANCES LEFT</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="game-card">
        <div class="stat">3</div>
        <div class="stat-label">TOTAL CHANCES</div>
    </div>
    """, unsafe_allow_html=True)


# ---------------- INSTRUCTIONS ----------------
st.subheader("🎮 How to Play")
st.write("""
- Guess a secret number between **1 and 10**.
- You have only **3 chances**.
- Guess correctly to win!
- Every wrong guess reduces your chances.
""")

st.divider()


# ---------------- GAME AREA ----------------
st.subheader("🔢 Enter Your Guess")

if not st.session_state.game_over:
    st.info(st.session_state.message)

    with st.form("guess_form"):
        cust_no = st.number_input(
            "Choose a number between 1 and 10",
            min_value=1,
            max_value=10,
            step=1,
            value=5
        )
        submit = st.form_submit_button("🚀 Submit Guess")

    if submit:
        if cust_no == st.session_state.python_no:
            st.session_state.won = True
            st.session_state.game_over = True
            st.session_state.message = "Congratulations! You won!"
        else:
            st.session_state.attempts -= 1

            if st.session_state.attempts == 0:
                st.session_state.game_over = True
                st.session_state.message = "No chances left! Game Over."
            elif cust_no < st.session_state.python_no:
                st.session_state.message = (
                    f"Too low! {st.session_state.attempts} "
                    "chance(s) left. Try again!"
                )
            else:
                st.session_state.message = (
                    f"Too high! {st.session_state.attempts} "
                    "chance(s) left. Try again!"
                )

        st.rerun()


# ---------------- GAME RESULT ----------------
if st.session_state.game_over:
    if st.session_state.won:
        st.success("🏆 YOU WIN! Congratulations!")
        st.balloons()
    else:
        st.error("❌ YOU LOSE! GAME OVER.")

    st.markdown(f"""
    <div class="game-card">
        <h3>Correct Number</h3>
        <div class="stat">{st.session_state.python_no}</div>
        <p>{"Great job!" if st.session_state.won else "Better luck next time!"}</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 Play Again"):
        new_game()
        st.rerun()


# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    Developed with Python & Streamlit ❤️
</div>
""", unsafe_allow_html=True)
