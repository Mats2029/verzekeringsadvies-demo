
import streamlit as st

# Gebruikersinput
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

# Cyberverzekering advies tonen
if st.button("Toon advies voor cyberverzekeringen"):
    resultaten = []
    for v in verzekeraars:
        match = bereken_match(v, profiel)
        resultaten.append({
            "naam": v["naam"],
            "dekking": "Hoog" if v["dekking_hoog"] else "Basis",
            "snel": "Ja" if v["snelle_afhandeling"] else "Nee",
            "prijs": v["prijsniveau"].capitalize(),
            "match": match
        })
    resultaten = sorted(resultaten, key=lambda x: x["match"], reverse=True)

    # HTML-tabel genereren
    html = """
    <style>
    .table-clean {
        font-family: 'Segoe UI', sans-serif;
        border-collapse: collapse;
        width: 100%;
        margin-top: 1rem;
    }
    .table-clean th {
        background-color: #f9f9f9;
        padding: 12px 10px;
        text-align: left;
        font-size: 15px;
        color: #333;
    }
    .table-clean td {
        padding: 10px;
        font-size: 14px;
        color: #222;
        border-bottom: none;
    }
    .table-clean tr {
        background-color: #fff;
    }
    .table-clean tr:hover {
        background-color: #f1f7ff;
    }
    .match-bar {
        background: #e5eefe;
        border-radius: 4px;
        overflow: hidden;
        height: 18px;
        width: 100%;
    }
    .match-bar-fill {
        height: 100%;
        background-color: #1f77d0;
        text-align: center;
        color: white;
        font-size: 12px;
        line-height: 18px;
    }
    </style>
    <h3 style="margin-top: 30px;">2. Cyberverzekering – op maat gesorteerd</h3>
    <table class="table-clean">
    <thead>
    <tr>
        <th>Verzekeraar</th>
        <th>Dekkingsniveau</th>
        <th>Snelle afhandeling</th>
        <th>Prijsniveau</th>
        <th>Match</th>
    </tr>
    </thead>
    <tbody>
    """

    for r in resultaten:
        bar_width = r["match"]
        html += f"""
        <tr>
            <td>{r['naam']}</td>
            <td>{r['dekking']}</td>
            <td>{r['snel']}</td>
            <td>{r['prijs']}</td>
            <td>
                <div class="match-bar">
                    <div class="match-bar-fill" style="width:{bar_width}%;">{bar_width}%</div>
                </div>
            </td>
        </tr>
        """

    html += "</tbody></table>"

    st.markdown(html, unsafe_allow_html=True)
