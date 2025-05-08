import streamlit as st
import time

st.set_page_config(page_title="Happy Birthday, My Love", layout="wide")

# 🎶 Background Music (autoplay, no controls)
# Playing background music automatically
audio_file = open("background_music.mp3", "rb")
st.audio(audio_file, format="audio/mp3", start_time=0)



# 💅 Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Parisienne&family=Great+Vibes&family=Quicksand:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Quicksand', sans-serif;
    background: linear-gradient(-45deg, #2a003f, #3a003f, #4b004f, #2a003f);
    background-size: 400% 400%;
    animation: gradientBG 30s ease infinite;
    color: #f3cce3;
    overflow-x: hidden;
}

h1, h2, h3 {
    font-family: 'Parisienne', cursive;
    color: #ff99cc !important;
    text-shadow: 0 0 5px #ffccf9;
    text-align: center;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.star-button {
    background: none;
    border: none;
    cursor: pointer;
    color: #fff;
    font-size: 24px;
    transition: transform 0.3s;
}

.star-button:hover {
    transform: scale(1.4);
    color: #ff74a4;
}

.shooting-star {
    position: fixed;
    top: 20%;
    left: 100%;
    width: 4px;
    height: 2px;
    background: white;
    box-shadow: 0 0 10px white, 0 0 20px white;
    animation: shooting 5s linear infinite;
    z-index: 1000;
}

@keyframes shooting {
    0% { left: 100%; top: 20%; opacity: 1; }
    100% { left: -20%; top: 80%; opacity: 0; }
}

.stButton>button {
    background-color: #e87bb9;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.5em 1.2em;
    font-size: 16px;
}

.stButton>button:hover {
    background-color: #ff74a4;
}

.streamlit-expanderHeader {
    color: #ffaad4 !important;
    font-size: 18px;
    font-weight: bold;
}

@import url('https://fonts.googleapis.com/css2?family=Dancing+Script&family=Quicksand:wght@400;600&display=swap');

/* Love letter box */
.love-letter {
    background-color: #fff0f5;
    border: 2px solid #ffb6c1;
    border-radius: 12px;
    padding: 30px;
    margin: 20px auto;
    max-width: 700px;
    box-shadow: 0 0 20px rgba(255, 182, 193, 0.4);
    color: #6b0033;
    font-family: 'Dancing Script', cursive;
    font-size: 24px;
    line-height: 2;
    text-align: center;
}

    /* Responsive design for mobile */
    @media (max-width: 600px) {
        html, body, [class*="css"] {
            font-size: 16px; /* Adjust font size for smaller screens */
        }

        .love-letter {
            padding: 15px;  /* Reduce padding on mobile */
            font-size: 18px; /* Adjust font size */
        }

        .stButton>button {
            padding: 0.5em 1em; /* Make buttons slightly smaller */
            font-size: 14px; /* Adjust button text size */
        }

        h1, h2, h3 {
            font-size: 26px; /* Adjust headers for smaller screens */
        }
    }
    </style>
    """, unsafe_allow_html=True)

# 💖 Header
st.markdown("<h1>Happy Birthday, My Universe</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size:18px;'>"
    "You are the poem my heart recites with every beat. "
    "This little galaxy is stitched together from our laughter, whispers, and dreams."
    "</p>",
    unsafe_allow_html=True
)
st.divider()

# ⭐ Scattered Stars Section
st.markdown("## 🌌 Touch A Star")
star_texts = [
    "✨ Our first hug under your roof felt like a secret promise—soft, sacred, and infinite.",
    "🌟 You are the calm in my storm, the melody beneath my breath, and the echo in my soul.",
    "💫 Every curve of your smile turns gravity off and sets my heart drifting among clouds.",
    "🌠 Your laugh—sunlight dancing on water—illuminates every corner of my being.",
    "🌙 You don’t just light up my sky; you are my night, my dream, my guiding star.",
    "⭐ In your voice I hear the lullaby of a thousand peaceful nights, singing me home.",
    "🌸 The moment you looked at me like I mattered, I understood the meaning of forever.",
    "🪐 A thousand lifetimes wouldn’t suffice to explore the depths of your kindness.",
    "☄️ Your touch writes poetry on my skin, letters of longing and hope entwined.",
    "🌌 In your eyes, I see galaxies I never knew existed—endless and beautiful.",
    "🌠 Together, we are a constellation of moments too precious to ever forget.",
    "✨ The warmth of your hand in mine is the spark that sets my entire world aglow."
]

for row in range(3):
    cols = st.columns(4)
    for idx, col in enumerate(cols):
        text = star_texts[row*4 + idx]
        with col:
            if st.button("⭐", key=f"star_{row}_{idx}"):
                st.success(text)
st.divider()

# 📖 Timeline
st.markdown("## 🕰️ Our Love Timeline")

with st.expander("💗 When We First Met"):
    st.write(
        "You walked in carrying numbers and formulas, but you brought magic with you. "
        "There was something in the way you smiled, something unspoken and infinite. "
        "Every second with you blurred the line between tutor and heartbeat. "
        "That evening, something in the universe shifted, gently, beautifully—and I felt it."
    )

with st.expander("💞 When I Realized It Was Real"):
    st.write(
        "It wasn’t a lightning strike—it was a slow bloom, the warmth of sunlight after winter. "
        "I realized it in the way you listened, the way your presence made silence feel like music. "
        "It was real the day I understood I could never un-love you, even if I tried."
    )

with st.expander("💖 My Favorite Ordinary Moment"):
    st.write(
        "You leaning over my notebook, correcting a small mistake with a grin. "
        "The soft bump of your elbow against mine. The comfort of your nearness. "
        "Those tiny moments, often overlooked, now live in my memory like sacred lullabies. "
        "It was never about grand gestures—it was about *you*, simply being there."
    )

with st.expander("🎂 A Dream I Have With You"):
    st.write(
        "In a sunlit kitchen, flour on your cheek, my arms around your waist, "
        "and laughter echoing off the walls—we bake not just cakes, but pieces of our love story. "
        "I dream of lazy Sunday mornings, your sleepy smile, our forever in the aroma of coffee and affection."
    )
st.divider()

# 💌 Love Letter
st.markdown("## 💌 A Letter From My Heart")

if st.button("Read My Love Letter"):
    st.markdown("""
    <div class="love-letter">
        Love didn’t hit me like lightning — it grew in the quietest ways. In the way you’d patiently walk me through a math problem, how we’d go off track laughing about school stories, or pause mid-sentence just to gush over *The Seven Husbands of Evelyn Hugo*. Somehow, somewhere between giggles and formulas, between your voice and your eyes, I fell. We haven’t even been in each other’s arms yet, but it feels like my heart has known the shape of yours forever. You make everything feel lighter — even the heaviest parts of me. On your birthday, I hope you feel all the magic you bring into this world. I wish you joy that wraps around you like warmth in winter, dreams that bloom wildly, and a love that never makes you question your worth — because you deserve it all, and more.Love, Uroosh 
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<hr style='border-top: 2px dashed #ffb3c6; margin-top: 50px;'>

<p style='text-align: center; font-size: 16px; color: #ffaad4;'>
Made with all my heart by Uroosh — for the girl who turned my world into a universe 💫
</p>
""", unsafe_allow_html=True)