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
    color: white;
}

.subtitle {
    text-align: center;
    color: #D6D6D6;
    font-size: 16px;
}

.stars {
    text-align: center;
    font-size: 38px;
    margin: 15px 0;
    letter-spacing: 10px;
    color: white;
}

.game-box {
    background: rgba(255,255,255,0.08);
    border: 2px solid rgba(255,255,255,0.5);
    border-radius: 25px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
}

.number-display {
    background: transparent;
    border: 2px solid white;
    border-radius: 20px;
    min-height: 150px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-size: 85px;
    font-weight: bold;
    margin: 15px 0 25px 0;
}

.guess-bar {
    width: 100%;
    height: 12px;
    background: transparent;
    border: 1px solid rgba(255,255,255,0.5);
    border-radius: 20px;
    overflow: hidden;
    margin: 10px 0 25px 0;
}

.guess-fill {
    height: 100%;
    border-radius: 20px;
    transition: all 0.4s ease;
}

div.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 48px;
    background: transparent !important;
    color: white !important;
    border: 1.5px solid white !important;
    font-weight: bold;
    font-size: 20px;
}

div.stButton > button:hover {
    background: rgba(255,255,255,0.15) !important;
    color: white !important;
}

div.stButton > button[kind="primary"] {
    background: white !important;
    color: #141E30 !important;
    border: 1px solid white !important;
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

/* Balloon Animation */
.balloon-container {
    position: fixed;
    bottom: -150px;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 9999;
}

.balloon {
    position: absolute;
    bottom: -120px;
    width: 35px;
    height: 45px;
    border-radius: 50%;
    animation: fly 7s linear infinite;
}

.balloon:after {
    content: "";
    position: absolute;
    width: 1px;
    height: 65px;
    background: white;
    top: 44px;
    left: 17px;
}

.balloon:nth-child(1) {
    left: 10%;
    background: #ff4d6d;
    animation-delay: 0s;
}

.balloon:nth-child(2) {
    left: 30%;
    background: #ffd166;
    animation-delay: 1s;
}

.balloon:nth-child(3) {
    left: 50%;
    background: #06d6a0;
    animation-delay: 2s;
}

.balloon:nth-child(4) {
    left: 70%;
    background: #4cc9f0;
    animation-delay: 0.5s;
}

.balloon:nth-child(5) {
    left: 90%;
    background: #c77dff;
    animation-delay: 1.5s;
}

@keyframes fly {
    0% {
        transform: translateY(0) rotate(0deg);
    }
    100% {
        transform: translateY(-120vh) rotate(20deg);
    }
}

/* Falling Paper Confetti */
.confetti-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    overflow: hidden;
    z-index: 9999;
}

.confetti {
    position: absolute;
    top: -30px;
    width: 12px;
    height: 18px;
    animation: paperFall 4s linear infinite;
}

.confetti:nth-child(5n+1) {
    background: #ff4d6d;
}

.confetti:nth-child(5n+2) {
    background: #ffd166;
}

.confetti:nth-child(5n+3) {
    background: #06d6a0;
}

.confetti:nth-child(5n+4) {
    background: #4cc9f0;
}

.confetti:nth-child(5n) {
    background: #c77dff;
}

@keyframes paperFall {
    0% {
        transform: translateY(-20px) rotate(0deg);
    }
    100% {
        transform: translateY(110vh) rotate(720deg);
    }
}

/* Play Again Highlight */
.st-key-play_again button {
    background: linear-gradient(90deg, #ffffff, #d6e4ff) !important;
    color: #141E30 !important;
    border: 2px solid white !important;
    font-size: 21px !important;
    font-weight: 900 !important;
    height: 58px !important;
    box-shadow: 0 0 15px rgba(255,255,255,0.6);
    animation: pulse 1.2s infinite;
}

@keyframes pulse {
    0%, 100% {
        box-shadow: 0 0 8px rgba(255,255,255,0.4);
        transform: scale(1);
    }
    50% {
        box-shadow: 0 0 25px rgba(255,255,255,0.9);
        transform: scale(1.03);
    }
}
</style>
""", unsafe_allow_html=True)


# Reset Game
def reset_game():
    st.session_state.secret_number = random.randint(0, 10)
    st.session_state.attempts = 3
    st.session_state.game_over = False
    st.session_state.won = False
    st.session_state.selected_number = None
    st.session_state.guess_distance = None
    st.session_state.message = "Select a number from 0 to 10"


if "secret_number" not in st.session_state:
    reset_game()


# Heading
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


# Guess Indicator Bar
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
    <div class="guess-bar">
        <div class="guess-fill"
             style="width:{bar_width}%; background:{bar_color};">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# Main Game Box
with st.container(border=True):

    st.markdown(
        "<h2 style='text-align:center; color:white;'>"
        "CHOOSE YOUR NUMBER</h2>",
        unsafe_allow_html=True
    )

    if st.session_state.won:

        # Balloon Animation
        st.markdown("""
        <div class="balloon-container">
            <div class="balloon"></div>
            <div class="balloon"></div>
            <div class="balloon"></div>
            <div class="balloon"></div>
            <div class="balloon"></div>
        </div>
        """, unsafe_allow_html=True)

        st.balloons()

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

        # Falling Paper Animation
        st.markdown("""
        <div class="confetti-container">
            <div class="confetti" style="left:5%;animation-delay:0s"></div>
            <div class="confetti" style="left:15%;animation-delay:1s"></div>
            <div class="confetti" style="left:25%;animation-delay:0.5s"></div>
            <div class="confetti" style="left:35%;animation-delay:2s"></div>
            <div class="confetti" style="left:45%;animation-delay:0.2s"></div>
            <div class="confetti" style="left:55%;animation-delay:1.5s"></div>
            <div class="confetti" style="left:65%;animation-delay:0.7s"></div>
            <div class="confetti" style="left:75%;animation-delay:2.5s"></div>
            <div class="confetti" style="left:85%;animation-delay:1s"></div>
            <div class="confetti" style="left:95%;animation-delay:0.3s"></div>
        </div>
        """, unsafe_allow_html=True)

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

        # Selected Number Display
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
            "font-size:17px;'>Choose a number from 0 to 10</p>",
            unsafe_allow_html=True
        )

        # Number Buttons 0 to 10
        for row in range(3):
            cols = st.columns(5)

            for col in range(5):
                number = row * 5 + col

                if number <= 10:
                    with cols[col]:
                        if st.button(
                            str(number),
                            key=f"number_{number}"
                        ):
                            st.session_state.selected_number = number
                            st.rerun()

        st.write("")

        # Submit Guess
        if st.button(
            "SUBMIT GUESS",
            use_container_width=True,
            type="primary"
        ):

            if st.session_state.selected_number is None:

                st.warning("Please choose a number first!")

            elif st.session_state.selected_number == st.session_state.secret_number:

                st.session_state.won = True
                st.session_state.guess_distance = 0
                st.rerun()

            else:

                distance = abs(
                    st.session_state.selected_number
                    - st.session_state.secret_number
                )

                st.session_state.guess_distance = distance
                st.session_state.attempts -= 1

                if st.session_state.attempts == 0:
                    st.session_state.game_over = True

                elif st.session_state.selected_number < st.session_state.secret_number:
                    st.session_state.message = "Too Low! Try Again."

                else:
                    st.session_state.message = "Too High! Try Again."

                st.session_state.selected_number = None
                st.rerun()

        st.info(st.session_state.message)


# Play Again
if st.session_state.won or st.session_state.game_over:

    with st.container(key="play_again"):
        if st.button(
            "🔄 PLAY AGAIN",
            use_container_width=True
        ):
            reset_game()
            st.rerun()


# Footer
st.markdown(
    "<p style='text-align:center; color:#AAAAAA; margin-top:30px;'>"
    "Made with ❤️ using Python & Streamlit"
    "</p>",
    unsafe_allow_html=True
)
