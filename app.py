
import streamlit as st
import pandas as pd

# Gebruikersinvoer
st.title("AI-verzekeringsadvies voor ICT-bedrijven")

st.header("1. Bedrijfsgegevens invullen")

medewerkers = st.slider("Aantal medewerkers", 0, 100, 5)
werkt_met_data = st.checkbox("Werk je met persoonsgegevens van klanten?", value=True)
levert_software = st.checkbox("Lever je software of digitale producten aan klanten?", value=True)
snelle_afhandeling_belangrijk = st.checkbox("Is snelle schadeafhandeling belangrijk voor jou?", value=True)
budget_voorkeur = st.selectbox("Wat is je budgetvoorkeur?", ["laag", "gemiddeld", "hoog"])

# Matching-logica
profiel = {
    "medewerkers": medewerkers,
    "werkt_met_data": werkt_met_data,
    "levert_software": levert_software,
    "snelle_afhandeling_belangrijk": snelle_afhandeling_belangrijk,
    "budget_voorkeur": budget_voorkeur
}

verzekeraars = [
    {
        "naam": "WebRisk",
        "dekking_hoog": True,
        "geschikt_grootbedrijf": True,
        "snelle_afhandeling": False,
        "prijsniveau": "hoog"
    },
    {
        "naam": "SecureInsure",
        "dekking_hoog": False,
        "geschikt_grootbedrijf": False,
        "snelle_afhandeling": True,
        "prijsniveau": "gemiddeld"
    },
    {
        "naam": "CyberSafe NL",
        "dekking_hoog": True,
        "geschikt_grootbedrijf": False,
        "snelle_afhandeling": True,
        "prijsniveau": "gemiddeld"
    },
    {
        "naam": "SafeByte",
        "dekking_hoog": True,
        "geschikt_grootbedrijf": False,
        "snelle_afhandeling": False,
        "prijsniveau": "laag"
    },
    {
        "naam": "DigiShield",
        "dekking_hoog": False,
        "geschikt_grootbedrijf": False,
        "snelle_afhandeling": False,
        "prijsniveau": "laag"
    }
]

def bereken_match(verzekeraar, profiel):
    score = 0
    max_score = 4
    if verzekeraar["dekking_hoog"] and profiel["werkt_met_data"]:
        score += 1
    if verzekeraar["geschikt_grootbedrijf"] and profiel["medewerkers"] > 10:
        score += 1
    if verzekeraar["snelle_afhandeling"] and profiel["snelle_afhandeling_belangrijk"]:
        score += 1
    if verzekeraar["prijsniveau"] == profiel["budget_voorkeur"]:
        score += 1
    return round((score / max_score) * 100)

# Vergelijkingstabel op basis van input
if st.button("Toon advies voor cyberverzekeringen"):
    resultaten = []
    for v in verzekeraars:
        match = bereken_match(v, profiel)
        resultaten.append({
            "Verzekeraar": v["naam"],
            "Dekkingsniveau": "Hoog" if v["dekking_hoog"] else "Basis",
            "Snelle afhandeling": "Ja" if v["snelle_afhandeling"] else "Nee",
            "Prijsniveau": v["prijsniveau"].capitalize(),
            "Match met jouw profiel (%)": match
        })
    df_resultaten = pd.DataFrame(resultaten)
    df_resultaten = df_resultaten.sort_values(by="Match met jouw profiel (%)", ascending=False)
    st.header("2. Cyberverzekering – op maat gesorteerd")
    st.dataframe(df_resultaten, use_container_width=True)
