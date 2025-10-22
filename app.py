import streamlit as st
import pandas as pd
import random

# Configuración general
st.set_page_config(page_title="Aliméntate Bien Chihuahua", layout="wide")
st.sidebar.title("Menú")
seccion = st.sidebar.radio("Ir a:", ["Inicio", "Diagnóstico personal", "Datos y estadísticas", "Consejos y alimentos locales", "Fuentes y créditos"])

# 1. Pantalla de inicio
if seccion == "Inicio":
    st.title("🥗 Aliméntate Bien Chihuahua")
    st.write("Conoce cómo influye tu alimentación en tu salud y descubre consejos para mejorar tus hábitos alimenticios.")
    st.image("assets/alimentos/manzana.jpg", caption="Manzana de Cuauhtémoc", use_column_width=True)

# 2. Diagnóstico personal
elif seccion == "Diagnóstico personal":
    st.header("📊 Diagnóstico Nutricional")
    peso = st.number_input("Ingresa tu peso (kg):", min_value=30.0, max_value=200.0)
    altura = st.number_input("Ingresa tu altura (m):", min_value=1.0, max_value=2.5)
    if st.button("Calcular IMC"):
        imc = peso / (altura ** 2)
        st.metric("Tu IMC es:", round(imc, 2))
        if imc < 18.5:
            st.warning("Bajo peso")
        elif imc < 25:
            st.success("Peso normal")
        elif imc < 30:
            st.info("Sobrepeso")
        else:
            st.error("Obesidad")
        st.bar_chart(pd.DataFrame({"IMC": [imc], "Normal": [22]}))

# 3. Datos y estadísticas
elif seccion == "Datos y estadísticas":
    st.header("📈 Estadísticas Nutricionales")
    st.write("Datos de salud y nutrición en Chihuahua y México.")
    try:
        df = pd.read_csv("data/estadisticas.csv")
        st.bar_chart(df.set_index("Región"))
    except:
        st.error("No se encontró el archivo de estadísticas. Asegúrate de tener 'estadisticas.csv' en la carpeta 'data'.")

# 4. Consejos y alimentos locales
elif seccion == "Consejos y alimentos locales":
    st.header("🌽 Alimentos Tradicionales y Consejos")
    grupo = st.selectbox("Selecciona un grupo alimenticio:", ["Frutas", "Verduras", "Granos", "Proteínas"])
    
    alimentos = {
        "Frutas": {"Manzana de Cuauhtémoc": "Rica en fibra y antioxidantes."},
        "Verduras": {"Chile": "Fuente de vitamina C y capsaicina."},
        "Granos": {"Maíz": "Base de la dieta mexicana, rico en carbohidratos complejos."},
        "Proteínas": {"Frijol": "Alto en proteína vegetal y hierro."}
    }

    for alimento, info in alimentos.get(grupo, {}).items():
        st.subheader(alimento)
        st.image(f"assets/alimentos/{alimento.lower().split()[0]}.jpg", width=200)
        st.write(info)

    if st.button("Dame un consejo"):
        consejos = [
            "Incluye frutas y verduras en cada comida.",
            "Evita bebidas azucaradas.",
            "Consume alimentos locales y frescos.",
            "Modera el consumo de sal y grasas saturadas."
        ]
        st.success(random.choice(consejos))

# 5. Fuentes y créditos
elif seccion == "Fuentes y créditos":
    st.header("📚 Fuentes y Créditos")
    st.markdown("""
    - INEGI: Encuesta Nacional de Salud y Nutrición  
    - Secretaría de Salud de Chihuahua  
    - FAO: Organización de las Naciones Unidas para la Alimentación  
    ---
    **Autores:** Equipo de desarrollo educativo  
    **Fecha:** Octubre 2025
    """)
