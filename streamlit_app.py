import time
import streamlit as st
from transformers import pipeline

# zaczynamy od zaimportowania bibliotek
st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')

st.title('LanguageApp')
st.image("img.png", use_container_width=True)
# title, jak sama nazwa wskazuje, używamy do wyświetlenia tytułu naszej aplikacji


st.subheader("O aplikacji")

st.markdown("""
Aplikacja korzysta z **modeli uczenia maszynowego**, aby przetwarzać tekst w języku angielskim.  
Dostępne funkcje:

1. **Analiza emocji tekstu**  
   Ocenia, czy wpisany tekst ma wydźwięk **pozytywny**, **negatywny** lub **neutralny**.

2. **Tłumaczenie EN → DE**  
   Tłumaczy tekst z **języka angielskiego na niemiecki** z wykorzystaniem modelu NLP.

""")


option = st.selectbox(
    "Opcje",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Tłumacz angielsko-niemiecki",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    text = st.text_area(label="Wpisz tekst")

    if st.button("Analizuj"):
        if text:
            with st.spinner("Jeszcze tylko chwilka..."):
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress.progress(i + 1)

                classifier = pipeline("sentiment-analysis")
                answer = classifier(text)

            st.success("Sukces!")
            st.write("**Wynik:**")
            st.write(answer)
        else:
            st.error("Wpisz tekst!")


if option == "Tłumacz angielsko-niemiecki":
    text = st.text_area("Wpisz tekst po angielsku")

    if st.button("Tłumacz"):
        if text:
            with st.spinner("Jeszcze tylko chwilka..."):
                progress = st.progress(0)

                for i in range(100):
                    time.sleep(0.01)
                    progress.progress(i + 1)

                translator = pipeline("translation_en_to_de")
                result = translator(text)

            st.success("Tłumaczenie zakończone!")
            st.write("**Tłumaczenie:**")
            st.success(result[0]["translation_text"])
        else:
            st.error("Wpisz tekst!")

st.write("---")
st.title("Numer indeksu: s25983")

