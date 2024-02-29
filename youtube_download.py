from pytube import YouTube
import os
import streamlit as st
import time

st.set_page_config(page_title="Youtube Download", layout='wide')

# titulo
st.markdown("<h1 style='text-align: center; color: black;'>Download de Video do Youtube</h1>", unsafe_allow_html=True)

url = st.text_input("Informe a Url do video: ", max_chars=100)
destino = st.text_input("Informe a pasta de destino: ", max_chars=100)

if st.button('Iniciar Donwload'):
    if len(url) != 0 and len(destino) != 0:
        yt = YouTube(url)

        video_stream = yt.streams.get_highest_resolution()

        # Criar Diretorio se não existir
        if not os.path.exists(destino):
            os.makedirs(destino)
            st.write(f'Diretorio foi criado: {destino}')

    st.write(f'Baixando {yt.title}')
    video_stream.download(destino)
    st.write('Download Concluido')

