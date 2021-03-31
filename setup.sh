#mkdir -p ~/.streamlit
#echo "[server]
#headless = true
#port = $PORT
#enableCORS = false
#" > ~/.streamlit/config.toml

mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"stephsumo@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml