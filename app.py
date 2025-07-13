import streamlit as st

def get_risk_profile(sector, employees, personal_data, delivers_software):
    profile = {
        "Beroepsaansprakelijkheid": "Essentieel" if delivers_software else "Sterk aanbevolen",
        "Cyberverzekering": "Essentieel" if personal_data else "Sterk aanbevolen",
        "Bedrijfsaansprakelijkheid": "Sterk aanbevolen" if employees > 0 else "Optioneel"
    }
    return profile

def main():
    st.title("AI-verzekeringsadvies voor ICT-bedrijven")

    st.header("1. Bedrijfsgegevens invullen")

    sector = st.selectbox("Wat is je sector?", ["ICT", "Marketing", "Consultancy"])
    employees = st.slider("Aantal medewerkers", 0, 100, 5)
    personal_data = st.checkbox("Werk je met persoonsgegevens van klanten?", value=True)
    delivers_software = st.checkbox("Lever je software of digitale producten aan klanten?", value=True)

    if st.button("Toon verzekeringsadvies"):
        profile = get_risk_profile(sector, employees, personal_data, delivers_software)

        st.header("2. Jouw verzekeringsadvies")
        color_map = {
            "Essentieel": "🔴",
            "Sterk aanbevolen": "🟠",
            "Optioneel": "🟡"
        }

        for insurance, score in profile.items():
            st.markdown(f"{color_map[score]} **{insurance}** – {score}")

        st.markdown("---")
        st.subheader("Klik op een verzekering om meer te zien (komt in versie 2 😉)")

main()
