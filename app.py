import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.title("Pantauan Saham Keluarga (IDX)")

# Pilihan kode saham IDX (wajib pakai akhiran .JK)
kode_saham = st.selectbox("Pilih Saham:", ["BBCA.JK", "BBRI.JK", "BMRI.JK", "TLKM.JK", "ASII.JK"])
periode = st.selectbox("Rentang Waktu:", ["1mo", "3mo", "6mo", "1y"])

# Mengambil data dari Yahoo Finance
data = yf.Ticker(kode_saham).history(period=periode)

# Menampilkan harga terakhir
harga_terakhir = data['Close'].iloc[-1]
st.metric(label=f"Harga Penutupan Terakhir ({kode_saham})", value=f"Rp {harga_terakhir:,.0f}")

# Membuat grafik Candlestick
fig = go.Figure(data=[go.Candlestick(
    x=data.index,
    open=data['Open'],
    high=data['High'],
    low=data['Low'],
    close=data['Close']
)])
fig.update_layout(xaxis_rangeslider_visible=False)
st.plotly_chart(fig)
