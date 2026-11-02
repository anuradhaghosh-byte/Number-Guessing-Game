
import random
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎮",
    layout="centered"
)

# ---------------- RESET GAME ----------------
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


# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #101426, #191d38, #242044);
    color: #E2E8F0;
}

.block-container {
    max-width: 600px;
    padding-top: 2rem;
}

/* Main Title */
.title {
    text-align: center;
    font-size: 36px;
    font-weight: 900;
    letter-spacing: 2px;
    color: #A78BFA;
}

.subtitle {
    text-align: center;
    color: #C4B5FD;
    font-size: 16px;
    margin-bottom: 20px;
}

/* Game Card */
div[data-testid="stVerticalBlockBorderWrapper"] {
    border: 1px solid #45436B;
    border-radius: 22px;
    background: rgba(35, 39, 70, 0.85);
    padding: 20px;
}

/* Stars */
.stars {
    text-align: center;
    font-size: 32px;
    margin: 15px 0;
    letter-spacing: 8px;
}

/* Number Display */
.number-display {
    background: #171B32;
    border: 2px solid #7770C9;
    border-radius: 20px;
    min-height: 130px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #67E8F9;
    font-size: 65px;
    font-weight: bold;
    margin: 15px 0 25px 0;
}

/* Guess Indicator */
.guess-bar {
    width: 100%;
    height: 10px;
    background: #343451;
    border: 1px solid #555477;
    border-radius: 20px;
    overflow: hidden;
    margin: 10px 0 25px 0;
}

.guess-fill {
    height: 100%;
    border-radius: 20px;
    transition: all 0.4s ease;
}

/* Number Buttons */
div.stButton > button {
    width: 100%;
    border-radius: 12px;
    height: 48px;
    background: #292747 !important;
    color: #E0E7FF !important;
    border: 1.5px solid #7770C9 !important;
    font-weight: bold;
    font-size: 20px;
    transition: 0.2s;
}

div.stButton > button:hover {
    background: #6255A5 !important;
    color: white !important;
    border-color: #A78BFA !important;
}

/* Submit Button */
div.stButton > button[kind="primary"] {
    background: #8B5CF6 !important;
    color: white !important;
    border: 1px solid #A78BFA !important;
    font-weight: bold;
}

div.stButton > button[kind="primary"]:hover {
    background: #A78BFA !important;
    color: #17132C !important;
}

/* Result */
.result {
    font-size: 35px;
    font-weight: bold;
    text-align: center;
    margin: 20px 0;
}

.win {
    color: #4ADE80;
}

.lose {
    color: #FB7185;
}

/* Status Text */
.stAlert {
    border-radius: 12px;
}

/* ---------------- SLOW BALLOON ANIMATION ---------------- */
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
    animation: fly 16s linear infinite;
}

.balloon:after {
    content: "";
    position: absolute;
    width: 1px;
    height: 65px;
    background: rgba(255,255,255,0.6);
    top: 44px;
    left: 17px;
}

.balloon:nth-child(1) {
    left: 10%;
    background: #FF4D6D;
    animation-delay: 0s;
}

.balloon:nth-child(2) {
    left: 30%;
    background: #FFD166;
    animation-delay: 3s;
}

.balloon:nth-child(3) {
    left: 50%;
    background: #06D6A0;
    animation-delay: 6s;
}

.balloon:nth-child(4) {
    left: 70%;
    background: #4CC9F0;
    animation-delay: 2s;
}

.balloon:nth-child(5) {
    left: 90%;
    background: #C77DFF;
    animation-delay: 5s;
}

@keyframes fly {
    0% {
        transform: translateY(0) rotate(0deg);
    }
    100% {
        transform: translateY(-120vh) rotate(20deg);
    }
}

/* ---------------- FALLING CONFETTI ---------------- */
.confetti-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    overflow: hidden;
    z-index: 9997;
}

.confetti {
    position: absolute;
    top: -30px;
    width: 12px;
    height: 18px;
    animation: paperFall 4s linear infinite;
}

.confetti:nth-child(5n+1) {
    background: #FF4D6D;
}

.confetti:nth-child(5n+2) {
    background: #FFD166;
}

.confetti:nth-child(5n+3) {
    background: #06D6A0;
}

.confetti:nth-child(5n+4) {
    background: #4CC9F0;
}

.confetti:nth-child(5n) {
    background: #C77DFF;
}

@keyframes paperFall {
    0% {
        transform: translateY(-20px) rotate(0deg);
    }
    100% {
        transform: translateY(110vh) rotate(720deg);
    }
}

/* ---------------- PAGE TEAR ANIMATION ---------------- */
.tear-overlay {
    position: fixed;
    inset: 0;
    z-index: 9998;
    pointer-events: none;
}

.tear-half {
    position: absolute;
    left: 0;
    width: 100%;
    height: 50%;
    background: #191D38;
}

.tear-top {
    top: 0;
    clip-path: polygon(
        0 0, 100% 0, 100% 100%,
        85% 96%, 70% 100%, 55% 95%,
        40% 100%, 25% 95%, 10% 100%, 0 96%
    );
    animation: tearTop 2s ease-in forwards;
}

.tear-bottom {
    bottom: 0;
    clip-path: polygon(
        0 0, 10% 5%, 25% 0, 40% 5%,
        55% 0, 70% 5%, 85% 0, 100% 4%,
        100% 100%, 0 100%
    );
    animation: tearBottom 2s ease-in forwards;
}

@keyframes tearTop {
    0% {
        transform: translateY(0);
    }
    100% {
        transform: translateY(-110%);
    }
}

@keyframes tearBottom {
    0% {
        transform: translateY(0);
    }
    100% {
        transform: translateY(110%);
    }
}

/* ---------------- PLAY AGAIN HIGHLIGHT ---------------- */
.st-key-play_again button {
    background: linear-gradient(90deg, #8B5CF6, #A78BFA) !important;
    color: white !important;
    border: 2px solid #C4B5FD !important;
    font-size: 21px !important;
    font-weight: 900 !important;
    height: 58px !important;
    box-shadow: 0 0 15px rgba(167,139,250,0.7);
    animation: pulse 1.2s infinite;
}

@keyframes pulse {
    0%, 100% {
        box-shadow: 0 0 8px rgba(167,139,250,0.5);
        transform: scale(1);
    }
    50% {
        box-shadow: 0 0 25px rgba(167,139,250,1);
        transform: scale(1.03);
    }
}

/* Footer */
.footer {
    text-align: center;
    color: #9299BB;
    margin-top: 30px;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADING ----------------
st.markdown(
    '<div class="title">🎮 NUMBER GUESSING GAME</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Can you guess the secret number?</div>',
    unsafe_allow_html=True
)


# ---------------- STARS ----------------
stars = "⭐" * st.session_state.attempts
empty_stars = "☆" * (3 - st.session_state.attempts)

st.markdown(
    f'<div class="stars">{stars}{empty_stars}</div>',
    unsafe_allow_html=True
)


# ---------------- GUESS INDICATOR BAR ----------------
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


# ---------------- MAIN GAME BOX ----------------
with st.container(border=True):

    st.markdown(
        "<h2 style='text-align:center; color:#A5B4FC;'>"
        "CHOOSE YOUR NUMBER</h2>",
        unsafe_allow_html=True
    )

    # ---------------- WIN SCREEN ----------------
    if st.session_state.won:

        # Slow Balloon Animation
        st.markdown("""
        <div class="balloon-container">
            <div class="balloon"></div>
            <div class="balloon"></div>
            <div class="balloon"></div>
            <div class="balloon"></div>
            <div class="balloon"></div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            '<div class="number-display">🎉</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="result win">YOU WIN!</div>',
            unsafe_allow_html=True
        )

        st.success("Congratulations! You guessed the correct number.")

    # ---------------- LOSS SCREEN ----------------
    elif st.session_state.game_over:

        # Page Tear Animation
        st.markdown("""
        <div class="tear-overlay">
            <div class="tear-half tear-top"></div>
            <div class="tear-half tear-bottom"></div>
        </div>
        """, unsafe_allow_html=True)

        # Falling Confetti Animation
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
            '<div class="number-display">💔</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="result lose">GAME OVER</div>',
            unsafe_allow_html=True
        )

        st.error(
            f"The correct number was {st.session_state.secret_number}"
        )

    # ---------------- PLAYING SCREEN ----------------
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
            "<p style='text-align:center; color:#C4B5FD; "
            "font-size:16px;'>Choose a number from 0 to 10</p>",
            unsafe_allow_html=True
        )

        # ---------------- CALCULATOR STYLE NUMBER BUTTONS ----------------
        number_layout = [
            [None, 0, None],
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [None, 10, None]
        ]

        for row_index, row in enumerate(number_layout):
            cols = st.columns(3)

            for col_index, number in enumerate(row):
                with cols[col_index]:

                    if number is not None:
                        if st.button(
                            str(number),
                            key=f"number_{number}",
                            use_container_width=True
                        ):
                            st.session_state.selected_number = number
                            st.rerun()

        st.write("")

        # ---------------- SUBMIT GUESS ----------------
        if st.button(
            "SUBMIT GUESS",
            use_container_width=True,
            type="primary"
        ):

            if st.session_state.selected_number is None:

                st.warning("Please choose a number first!")

            elif (
                st.session_state.selected_number
                == st.session_state.secret_number
            ):

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

                elif (
                    st.session_state.selected_number
                    < st.session_state.secret_number
                ):
                    st.session_state.message = "Too Low! Try Again."

                else:
                    st.session_state.message = "Too High! Try Again."

                st.session_state.selected_number = None
                st.rerun()

        st.info(st.session_state.message)


# ---------------- PLAY AGAIN ----------------
if st.session_state.won or st.session_state.game_over:

    with st.container(key="play_again"):

        if st.button(
            "🔄 PLAY AGAIN",
            use_container_width=True
        ):
            reset_game()
            st.rerun()


# ---------------- FOOTER ----------------
st.markdown(
    '<div class="footer">'
    'Made with ❤️ using Python & Streamlit'
    '</div>',
    unsafe_allow_html=True
)
