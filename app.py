import streamlit as st
import openai

# Clave API (usá secrets o colocala directamente acá para pruebas)
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("CodeStudy AI 🧠")
st.markdown("Generador de explicaciones, ejercicios y desafíos personalizados para aprender programación con IA.")

lenguaje = st.selectbox("Lenguaje de programación", ["Python", "JavaScript", "Java", "C#", "C++"])
tipo_ayuda = st.selectbox("Tipo de ayuda", ["Explicación", "Ejercicio", "Desafío práctico"])
nivel = st.selectbox("Nivel del usuario", ["Principiante", "Intermedio", "Avanzado"])
tema = st.text_input("Tema o concepto a estudiar", placeholder="Ej: Arrays, funciones, promesas...")

if st.button("Generar contenido con IA"):
    if not tema.strip():
        st.warning("Por favor, escribí un tema.")
    else:
        with st.spinner("Generando... ⏳"):
            prompt = (
                f"Actuá como un tutor experto en programación. Explicá de forma clara y sencilla el siguiente concepto: {tema}. "
                f"Nivel del usuario: {nivel}. "
                f"Lenguaje de programación: {lenguaje}. "
                f"Tu respuesta debe ser didáctica, contener ejemplos y estar enfocada en que el estudiante entienda el tema fácilmente. "
                f"Si se pidió un ejercicio o desafío, crealo con enunciado y solución explicada."
            )

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=1000,
                )
                output = response.choices[0].message.content
                st.markdown("### ✨ Resultado:")
                st.write(output)
            except Exception as e:
                st.error(f"Error al consultar la API: {e}")
