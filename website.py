import streamlit as st 
from streamlit_option_menu import option_menu
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title = "Bruna's Awesome Website", page_icon = ":tada:", layout = "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
with st.container():
    st.title("University of North Carolina Men's Basketball Profiles")
    st.header("Use the sidebar menu to select which player's statistics to view!")
    st.write("All the statistics used in this website were found [here](https://goheels.com/sports/mens-basketball/stats)")


with st.sidebar:
    player = option_menu(
        menu_title=" Which UNC Player's Statistics Would You Like To See?",
        options = ["Home", "Key", "Armando Bacot", "Caleb Love", "RJ Davis", "Puff Johnson", "Leaky Black", "Brady Manek"],
        icons = ["house-fill", "key-fill"],
        default_index = 0
    )

st.write("---")
if player == "Home":
    lottie_basketball = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_wOCCGc.json")
    st_lottie(lottie_basketball, height = 300, key = "basketball")
  

if player == "Armando Bacot":
    with st. container():
        st.header(f"{player}'s Statistics for 2021-2022")
        st.write("##")
        st.image(
            "https://tarheeltribune.files.wordpress.com/2022/03/bacot-ff-e1648757473338.png",
            width = 200,
        )
        st.write("[Armando Bacot Highlights 2021-2022](https://www.youtube.com/watch?v=Q_-_FFs-xlw)")
        bacot:list[dict[str, str]] = [{"GP": "39", "GS": "39", "MIN/G": "31.7", "FGM": "244", "FGA": "429", "FG%": ".569", "3PT": "1", "3PTA": "8", "3PT%": ".125", "PTS": "633", "AVG": "16.3", "OFF REB": "163", "DEF REB": "348", "REB": "511", "AST": "59"}]
        st.table(bacot)

if player == "Caleb Love":
    st.header(f"{player}'s Statistics for 2021-2022")
    st.write("##")
    st.image(
            "https://goheels.com/images/2021/9/21/Love_Caleb_mbb_67.jpg",
            width = 200,
        )
    st.write("[Caleb Love Highlights 2021-2022](https://www.youtube.com/watch?v=plYqvwlmZk4)")
    love:list[dict[str, str]] = [{"GP": "39", "GS": "38", "MIN/G": "34.0", "FGM": "178", "FGA": "419", "FG%": ".429", "3PT": "66", "3PTA": "180", "3PT%": ".367", "PTS": "527", "AVG": "13.5", "OFF REB": "8", "DEF REB": "125", "REB": "133", "AST": "139"}]
    st.table(love)
if player == "RJ Davis":
    st.header(f"{player}'s Statistics for 2021-2022")
    st.write("##")
    st.image(
            "https://d141rwalb2fvgk.cloudfront.net/images/2021/9/21/Davis_RJ_mbb_77.jpg?width=300",
            width = 200,
        )
    st.write("[RJ Davis Highlights 2021-2022](https://www.youtube.com/watch?v=SFUMmMtpmFw)")
    davis:list[dict[str, str]] = [{"GP": "39", "GS": "39", "MIN/G": "31.7", "FGM": "244", "FGA": "429", "FG%": ".569", "3PT": "1", "3PTA": "8", "3PT%": ".125", "PTS": "633", "AVG": "16.3", "OFF REB": "22", "DEF REB": "144", "REB": "166", "AST": "142"}]
    st.table(davis)
if player == "Puff Johnson":
    st.header(f"{player}'s Statistics for 2021-2022")
    st.write("##")
    st.image(
            "https://www.gannett-cdn.com/presto/2022/03/31/PPHX/7642f62a-47fb-484e-b715-628c20a824ec-e0856f764cd24480b196563a63e33b40.jpg",
            width = 400,
        )
    st.write("[Puff Johnson Highlights 2021-2022](https://www.youtube.com/watch?v=himb9MuHyUU)")
    johnson:list[dict[str, str]] = [{"GP": "24", "GS": "0", "MIN/G": "10.4", "FGM": "28", "FGA": "61", "FG%": ".459", "3PT": "6", "3PTA": "26", "3PT%": ".231", "PTS": "75", "AVG": "3.1", "OFF REB": "18", "DEF REB": "29", "REB": "47", "AST": "11"}]
    st.table(johnson)
if player == "Leaky Black":
    st.header(f"{player}'s Statistics for 2021-2022")
    st.write("##")
    st.image(
            "https://goheels.com/images/2021/10/1/Black_Leaky_mbb_115.jpg",
            width = 200,
        )
    st.write("[Leaky Black Highlights 2021-2022](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=video&cd=&cad=rja&uact=8&ved=2ahUKEwjRpLWrtob3AhVpoHIEHaRPDr8QuAJ6BAgKEAU&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DX3YwKnO5jj4&usg=AOvVaw25_Iy75h3_q0CMi7W07HD_)")
    black:list[dict[str, str]] = [{"GP": "38", "GS": "28", "MIN/G": "29.7", "FGM": "68", "FGA": "146", "FG%": ".466", "3PT": "17", "3PTA": "51", "3PT%": ".333", "PTS": "186", "AVG": "4.9", "OFF REB": "49", "DEF REB": "113", "REB": "162", "AST": "104"}]
    st.table(black)
if player == "Brady Manek":
    st.header(f"{player}'s Statistics for 2021-2022")
    st.write("##")
    st.image(
            "https://goheels.com/images/2021/9/21/Manek_Brady_mbb_13.jpg",
            width = 200,
        )
    st.write("[Brady Manek Highlights 2021-2022](https://www.youtube.com/watch?v=TfT2uw4KJ3A)")
    manek:list[dict[str, str]] = [{"GP": "39", "GS": "27", "MIN/G": "30.4", "FGM": "219", "FGA": "444", "FG%": ".493", "3PT": "98", "3PTA": "243", "3PT%": ".403", "PTS": "589", "AVG": "15.1", "OFF REB": "58", "DEF REB": "179", "REB": "237", "AST": "70"}]
    st.table(manek)
if player == "Key":
    st.write(
    """
    - GP = Games Played
    - GS = Games Started
    - MIN/G = Average Minutes Per Game
    - FGM = Field Goals Made
    - FGA = Field Goals Attempted
    - FG% = Field Goal Percentage
    - 3PT = 3 Pointers 
    - 3PTA = 3 Pointers Attempted
    - PTS = Total Points Made 
    - AVG = Average Points Per Game
    - OFF REB = Offensive Rebound
    - DEF REB = Defensive Rebounds
    - REB = Total Rebounds
    - AST = Total Assists
    """
    )

  