import streamlit as st
import random

# Page setup
st.set_page_config(page_title="Hangman Game", page_icon="🎯", layout="centered")

# Styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #d6f0ff, #eafaff);
        }
        .stButton>button {
            background-color: #007acc;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 10px;
            transition: 0.3s ease-in-out;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .stButton>button:hover {
            background-color: #005f99;
            transform: scale(1.05);
        }
        .hangman-box {
            background-color: #f2faff;
            border-radius: 15px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease-in-out;
        }
        .hanging-header {
            background-color: #007acc;
            padding: 15px 40px;
            border-radius: 20px;
            color: white;
            font-size: 28px;
            text-align: center;
            margin: 30px auto 10px auto;
            width: fit-content;
            position: relative;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease-in-out;
        }
        .hanging-header:hover {
            transform: rotate(3deg);
        }
        .hanging-header::before, .hanging-header::after {
            content: '';
            position: absolute;
            width: 12px;
            height: 12px;
            background: #ff6666;
            border-radius: 50%;
            top: -16px;
        }
        .hanging-header::before {
            left: 15px;
        }
        .hanging-header::after {
            right: 15px;
        }
        .hanging-line-left, .hanging-line-right {
            width: 2px;
            height: 20px;
            background: #999;
            position: absolute;
            top: -20px;
        }
        .hanging-line-left {
            left: 21px;
        }
        .hanging-line-right {
            right: 21px;
        }

        /* Enlarged text input styling */
        label[for^="Enter a letter"] {
            font-size: 20px !important;
            font-weight: bold;
            color: #004466;
            margin-bottom: 10px;
            display: block;
        }

        .stTextInput>div>div>input {
            font-size: 20px;
            padding: 10px;
            border-radius: 8px;
            border: 2px solid #007acc;
        }
    </style>
""", unsafe_allow_html=True)

# Hanging Title
st.markdown("""
<div class="hanging-header">
    🎯 Hangman Game
    <div class="hanging-line-left"></div>
    <div class="hanging-line-right"></div>
</div>
<div class="hangman-box">
    <p style='text-align: center; font-size: 18px; color: #005f99;'>Guess the word one letter at a time before you run out of lives!</p>
</div>
""", unsafe_allow_html=True)

# Words list
word_list = [
    "python", "developer", "hangman", "streamlit", "algorithm",
    "variable", "function", "debugging", "terminal", "keyboard",
    "internet", "database", "software", "hardware", "framework",
    "compiler", "argument", "boolean", "iteration", "exception"
]
chosen_word = st.session_state.get("chosen_word", random.choice(word_list))
display = st.session_state.get("display", ["_"] * len(chosen_word))
guessed_letters = st.session_state.get("guessed_letters", [])
lives = st.session_state.get("lives", 6)
game_over = st.session_state.get("game_over", False)

# Input
if not game_over:
    guess = st.text_input("Enter a letter:", max_chars=1).lower()

    if st.button("Guess Letter"):
        if guess and guess not in guessed_letters:
            guessed_letters.append(guess)
            if guess in chosen_word:
                for index, letter in enumerate(chosen_word):
                    if letter == guess:
                        display[index] = letter
            else:
                lives -= 1
            if "_" not in display or lives <= 0:
                game_over = True
        else:
            st.warning("Letter already guessed or invalid input.")

# Display Current Game State
st.markdown(f"""
<div class="hangman-box">
    <h3 style='color:#004466;'>Word: {' '.join(display)}</h3>
    <p style='color:#004466;'>Guessed Letters: {', '.join(guessed_letters)}</p>
    <p style='color:#004466;'>Lives Remaining: {lives} ❤️</p>
</div>
""", unsafe_allow_html=True)

# Game Over Message (Big Celebratory or Sad Text)
if game_over:
    if "_" not in display:
        st.balloons()
        st.markdown(f"""
            <div style='text-align: center; font-size: 40px; color: green; font-weight: bold; margin-top: 40px;'>
                🎉 YOU WON! 🎉
            </div>
            <p style='text-align: center; font-size: 20px;'>The word was: <strong>{chosen_word}</strong></p>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style='text-align: center; font-size: 40px; color: red; font-weight: bold; margin-top: 40px;'>
                😢 YOU LOST! TRY AGAIN 😢
            </div>
            <p style='text-align: center; font-size: 20px;'>The word was: <strong>{chosen_word}</strong></p>
        """, unsafe_allow_html=True)

    if st.button("🔁 Play Again"):
        for key in ["chosen_word", "display", "guessed_letters", "lives", "game_over"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# Save session state
st.session_state.chosen_word = chosen_word
st.session_state.display = display
st.session_state.guessed_letters = guessed_letters
st.session_state.lives = lives
st.session_state.game_over = game_over

# Footer
st.markdown("""
<hr style='border: 1px solid #b3d9ff;'>
<p style='text-align: center; font-size: 14px;'>Developed by Sabila Aleem ❤</p>
""", unsafe_allow_html=True)
