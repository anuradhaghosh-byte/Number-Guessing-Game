import random
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎮",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #141E30, #243B55);
    color: white;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #FFD700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #D6D6D6;
    font-size: 16px;
}

.stars {
    text-align: center;
    font-size: 38px;
    margin: 20px 0;
    letter-spacing: 10px;
}

.game-box {
    background: rgba(255,255,255,0.10);
    border: 2px solid rgba(255,255,255,0.2);
    border-radius: 25px;
    padding: 35px 25px;
    text-align: center;
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
}

.result {
    font-size: 35px;
    font-weight: bold;
    margin: 20px 0;
}

.win {
    color: #00FF99;
}

.lose {
    color: #FF5252;
}

div.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 50px;
    background: #FFD700;
    color: #141E30;
    font-weight: bold;
    border: none;
    font-size: 18px;
}

div.stButton > button:hover {
    background: #FFC107;
    color: black;
}
</style>
""", unsafe_allow_html=True)


# Initialize game
def reset_game():
    st.session_state.secret_number = random.randint(1, 10)
    st.session_state.attempts = 3
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.message = "Guess a number between 1 and 10!"


if "secret_number" not in st.session_state:
    reset_game()


# Heading
st.markdown('<div class="title">🎮 NUMBER GUESSING GAME</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Can you guess the secret number?</div>',
    unsafe_allow_html=True
)

# Stars
stars = "⭐" * st.session_state.attempts
empty_stars = "☆" * (3 - st.session_state.attempts)

st.markdown(
    f'<div class="stars">{stars}{empty_stars}</div>',
    unsafe_allow_html=True
)

# Main game box
st.markdown('<div class="game-box">', unsafe_allow_html=True)

if st.session_state.won:
    st.markdown(
        '<div class="result win">🎉 YOU WIN!</div>',
        unsafe_allow_html=True
    )
    st.success("Congratulations! You guessed the correct number.")

elif st.session_state.game_over:
    st.markdown(
        '<div class="result lose">GAME OVER</div>',
        unsafe_allow_html=True
    )
    st.error(
        f"The correct number was {st.session_state.secret_number}."
    )

else:
    st.markdown("### Enter Your Guess")

    guess = st.number_input(
        "Choose a number",
        min_value=1,
        max_value=10,
        step=1,
        key="guess_input"
    )

    if st.button("SUBMIT GUESS"):
        if guess == st.session_state.secret_number:
            st.session_state.won = True
            st.session_state.message = "Correct guess!"
        else:
            st.session_state.attempts -= 1

            if st.session_state.attempts == 0:
                st.session_state.game_over = True
            elif guess < st.session_state.secret_number:
                st.session_state.message = "Too low! Try again."
            else:
                st.session_state.message = "Too high! Try again."

        st.rerun()

    st.info(st.session_state.message)

st.markdown('</div>', unsafe_allow_html=True)

# Play again
if st.session_state.won or st.session_state.game_over:
    if st.button("🔄 PLAY AGAIN"):
        reset_game()
        st.rerun()

st.markdown(
    "<p style='text-align:center; color:#AAAAAA; margin-top:30px;'>"
    "Made with ❤️ using Python & Streamlit"
    "</p>",
    unsafe_allow_html=True
)
