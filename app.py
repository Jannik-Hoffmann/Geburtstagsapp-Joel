import streamlit as st
import time
from streamlit_js_eval import streamlit_js_eval
from streamlit_extras.let_it_rain import rain
import random

def play_background_music():
    # Verwenden von HTML/JS, um das Audio im Hintergrund automatisch zu starten
    st.markdown("""
    <audio id="background-audio" autoplay loop>
        <source src="audio/background.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    <script>
        var audio = document.getElementById("background-audio");
        audio.volume = 1;  # Lautstärke einstellen (optional)
    </script>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="MEGA-GEWINNSPIEL!!!", layout="wide")
    
    # Hintergrundmusik starten
    play_background_music()
    
    # CSS für Comic Sans, blinkende Elemente, bunte Farben und andere Stilelemente
    st.markdown("""
    <style>
    @keyframes blink {
        0% { opacity: 0; }
        50% { opacity: 1; }
        100% { opacity: 0; }
    }
    .blinking {
        animation: blink 0.5s linear infinite;
    }
    .big-text {
        font-size: 36px;
        font-weight: bold;
        color: #FF1493;
        text-shadow: 2px 2px #FFD700;
        font-family: 'Comic Sans MS', 'Comic Sans', cursive;
    }
    .rainbow-text {
        background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 24px;
        font-weight: bold;
        font-family: 'Comic Sans MS', 'Comic Sans', cursive;
    }
    .centered {
        text-align: center;
        font-family: 'Comic Sans MS', 'Comic Sans', cursive;
    }
    body {
        background-color: #FFD700;
        background-image: url("https://www.transparenttextures.com/patterns/cubes.png");
        font-family: 'Comic Sans MS', 'Comic Sans', cursive;
    }
    </style>
    """, unsafe_allow_html=True)
    
    if 'stage' not in st.session_state:
        st.session_state.stage = 0
    
    if st.session_state.stage == 0:
        st.markdown('<p class="big-text centered blinking">🎉 MEGA-GEWINNSPIEL!!! 🎉</p>', unsafe_allow_html=True)
        st.markdown('<p class="rainbow-text centered">Du könntest der glückliche Millionär sein!</p>', unsafe_allow_html=True)
        st.markdown('<p class="blinking centered">Sie sind der 1.000.000. Besucher!</p>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("💰 JETZT GEWINNEN! 💰", key="win_button"):
                st.session_state.stage = 1
                st.rerun()
        with col2:
            if st.button("🎁 BONUS-PREIS! 🎁", key="bonus_button"):
                bonus_prize()
        with col3:
            if st.button("🔥 SONDER-ANGEBOT! 🔥", key="special_button"):
                special_offer()
        
        st.markdown('<p class="blinking centered">⏰ Angebot endet in 5 Minuten! ⏰</p>', unsafe_allow_html=True)
    
    elif st.session_state.stage == 1:
        rain(
            emoji="💸",
            font_size=54,
            falling_speed=5,
            animation_length="infinite",
        )
        st.balloons()
        st.markdown('<p class="big-text centered">🎊 JACKPOT!!! 🎊</p>', unsafe_allow_html=True)
        streamlit_js_eval(js_expressions="Notification.requestPermission().then(perm => { if(perm === 'granted') { new Notification('Herzlichen Glückwunsch zum Geburtstag Joel! 🥳🎂🎁'); } })")
        
        # Soundeffekt für Gewinn
        st.audio("https://upload.wikimedia.org/wikipedia/commons/6/6c/Success-sound-effect.ogg", format='audio/ogg', start_time=0)
        
        if st.button("🚀 GEWINN EINLÖSEN? 🚀"):
            st.session_state.stage = 2
            st.rerun()
    
    elif st.session_state.stage == 2:
        st.markdown('<p class="big-text centered">🎈 HAPPY BIRTHDAY JOEL! 🎈</p>', unsafe_allow_html=True)
        
        st.image("https://th.bing.com/th/id/OIG2.6kzH1TbTsAKYGQxEOxIB?pid=ImgGn")
        
        st.write("""
        Lieber Joel,

        Überraschung! 🎉 Du hast keinen Millionengewinn gemacht, aber etwas viel Besseres:
        Einen Gutschein für ein unvergessliches Abenteuer mit Nils und Jannik 🌟🌟🌟!

        Wir schenken dir einen Tag voller Action, Spaß und Erinnerungen. 

        Ein paar gute Ideen haben wir schon und freuen uns darauf, die Details mit dir zu planen.
        Egal, was du wählst, wir werden einen fantastischen Tag zusammen verbringen!

        Alles Gute zum Geburtstag!
        Deine Freunde
        Nils und Jannik 🎂 🎁🎈
                 """)
        # Witziger Zusatz
        st.markdown("---")
        st.markdown('<p class="rainbow-text">🎰 BONUS-CHANCE! 🎰</p>', unsafe_allow_html=True)
        st.write("Drücke den Knopf für die Chance auf einen LUXUS-URLAUB!")
        if st.button("🏝️ Urlaubs-Lotterie 🏝️"):
            result = random.choice(["Leider kein Gewinn", "Fast! Vielleicht beim nächsten Mal", "Du hast... eine Umarmung gewonnen! 🤗"])
            st.write(result)
        
        if st.button("Zurück zum Anfang"):
            st.session_state.stage = 0
            st.rerun()

    # Easter Egg
    time.sleep(40)
    if st.button("🍰 Geheimer Kuchen-Button 🍰", key="secret"):
        st.write("Du hast den geheimen Kuchen gefunden! Hier ist ein virtuelles Stück nur für dich: 🍰")

# Funktion für den Bonus-Preis
def bonus_prize():
    st.markdown("## 🎁 Dein Bonus-Preis! 🎁")
    prize = random.choice([
        "Du hast einen virtuellen Welpen gewonnen! 🐶",
        "Du hast einen Gutschein für eine Umarmung gewonnen! 🤗",
        "Du bekommst... einen unsichtbaren Ferrari! 🏎️💨",
        "Ein Jahr kostenlose Luft! Atme tief durch! 🌬️",
        "Du hast... nichts gewonnen! 😅"
    ])
    st.success(prize)

# Funktion für das Sonder-Angebot
def special_offer():
    st.markdown("## 🔥 Dein spezielles Angebot! 🔥")
    offer = random.choice([
        "Nur heute: Kaufe 1, bekomme 1 zu 100% Rabatt! (Auf Luft)",
        "Exklusiv: Virtuelle Eintrittskarten für das nächste Konzert... auf dem Mond! 🌕",
        "Super Spar-Angebot: Eine Einladung zu einem imaginären Dinner mit Promis! 🍽️✨",
        "Deal des Tages: Ein Ticket für die Reise in die 4. Dimension! ⏳",
        "Nur für kurze Zeit: Virtuelle Luxusvillen mit Blick auf den virtuellen Ozean! 🏝️"
    ])
    st.warning(offer)

if __name__ == "__main__":
    main()
