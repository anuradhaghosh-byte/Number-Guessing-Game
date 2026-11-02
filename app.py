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
