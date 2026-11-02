import random
import streamlit as st

st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎮",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #141E30, #243B55);
    color: white;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #FFD700;
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
    padding: 25px;
    text-align: center;
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
}

.number-display {
    background: rgba(0,0,0,0.25);
    border: 2px solid #FFD700;
    border-radius: 20px;
    min-height: 150px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #FFD700;
    font-size: 85px;
    font-weight: bold;
    margin: 15px 0 25px 0;
}

.result {
    font-size: 35px;
    font-weight: bold;
    text-align: center;
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
    height: 48px;
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


def reset_game():
    st.session_state.secret_number = random.randint(0, 9)
    st.session_state.attempts = 3
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.selected_number = None
    st.session_state.message = "Select a number from 0 to 9"


if "secret_number" not in st.session_state:
    reset_game()


st.markdown(
    '<div class="title">🎮 NUMBER GUESSING GAME</div>',
    unsafe_allow_html=True
)

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
with st.container(border=True):

    st.markdown(
        "<h2 style='text-align:center; color:#FFD700;'>"
        "CHOOSE YOUR NUMBER</h2>",
        unsafe_allow_html=True
    )

    # Number display
    if st.session_state.won:
        st.markdown(
            '<div class="number-display">🎉</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="result win">YOU WIN!</div>',
            unsafe_allow_html=True
        )
        st.success("Congratulations! You guessed the correct number.")

    elif st.session_state.game_over:
        st.markdown(
            '<div class="number-display">GAME OVER</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="result lose">GAME OVER</div>',
            unsafe_allow_html=True
        )
        st.error(
            f"The correct number was {st.session_state.secret_number}"
        )

    else:

        selected = st.session_state.selected_number

        display_number = (
            str(selected) if selected is not None else "?"
        )

        st.markdown(
            f'<div class="number-display">{display_number}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            "<p style='text-align:center; color:white; "
            "font-size:17px;'>Choose a number from 0 to 9</p>",
            unsafe_allow_html=True
        )

        # Number buttons: 0 to 9
        for row in range(2):
            cols = st.columns(5)

            for col in range(5):
                number = row * 5 + col

                with cols[col]:
                    if st.button(
                        str(number),
                        key=f"number_{number}"
                    ):
                        st.session_state.selected_number = number
                        st.rerun()

        st.write("")

        # Submit button
        if st.button("SUBMIT GUESS", use_container_width=True):

            if st.session_state.selected_number is None:
                st.warning("Please choose a number first!")

            elif st.session_state.selected_number == st.session_state.secret_number:
                st.session_state.won = True
                st.rerun()

            else:
                st.session_state.attempts -= 1

                if st.session_state.attempts == 0:
                    st.session_state.game_over = True
                else:
                    if st.session_state.selected_number < st.session_state.secret_number:
                        st.session_state.message = "Too Low! Try Again."
                    else:
                        st.session_state.message = "Too High! Try Again."

                st.session_state.selected_number = None
                st.rerun()

        st.info(st.session_state.message)


# Play Again
if st.session_state.won or st.session_state.game_over:

    if st.button("🔄 PLAY AGAIN", use_container_width=True):
        reset_game()
        st.rerun()


st.markdown(
    "<p style='text-align:center; color:#AAAAAA; margin-top:30px;'>"
    "Made with ❤️ using Python & Streamlit"
    "</p>",
    unsafe_allow_html=True
)
