import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="מספרי הגרלה מנצחים", layout="wide")

col1, col2, col3 = st.columns(3)
container1 = st.container()
container2 = st.container()

st.divider()
with container1:
    st.header("מיליונרירAI", divider=True)
    st.divider()

    if 'click_count' not in st.session_state:
        st.session_state.clock_count = 0

    max_clicks_allowed = 4


    if not st.checkbox("אני מסכים לכל תנאי השימוש"):
        st.title("חשוב! חובה לקרוא ולהסכים להצהרה הבאה לפני השימוש בשירות. המשך השימוש באתר משמעו הסכמתך לתנאים")

        st.markdown("המידע המוצג באתר מיועד למטרות אינפורמטיביות"
                    " בלבד ואין להסתמך עליו לצורך קבלת החלטות כספיות או אחרות."
                    "  המשתמש באתר אחראי לשימוש בו ולהשלכות באשר הן. האתר ומי מאחוריו "
                    "אינם אחראים בשום אופן לכל נזק או הפסד שעלול להיגרם כתוצאה"
                    " מהשימוש במידע המוצג בו.המידע המוצג הוא פרי ניתוח סטטיסטי מעמיק "
                    "וספקולציות מבוססות למידת מכונה בלבד ואינו מבטיח בשום צורה"
                    " רווח כלשהו. שימוש בשירות משמעו הסכמתך להצהרה זו. הצהרה זו"
                    "ונוספות מנוסחות בלשון זכר אך מתייחסות לכלל המגדרים.")

    else:
        st.write("תודה כעת אתה יכול להשתמש בשירות")

st.divider()

def main():
    path = r'/mnt/c/Users/user/PycharmProjects/Softwares_for_selling/loto/data_loto.csv'
    df = pd.read_csv(path)
    selected_data = df.loc[[int(month_of_interest)-1], ['most_nums_1','most_nums_2','most_nums_3','most_nums_4','most_nums_5','most_nums_6']]
    values = np.array(selected_data).flatten()
    rand = np.random.choice(values, int(num_of_nums_requested), replace=False)

    if not 0 < int(num_of_nums) <= 6:
        st.error("בחר ערך בין 1 ל 6 בלבד")
    if not 0 < int(month_of_interest) <= 12:
        st.error("בחר ערך בין 1 ל 12 בלבד")


    if max_nums_bttn:
        if st.session_state.clock_count < max_clicks_allowed:
            st.session_state.clock_count += 1
            progress_bar = st.progress(100, text="מכינים עבורך את המספרים המנצחים")
            st.write(rand)
            st.warning(f"נשאר לך שימושים {max_clicks_allowed - st.session_state.clock_count}  ")
            st.balloons()
        else:
            st.error("ניצלת את כל השימושים. אם ברצונך להמשיך להשתמש בשירות יש לרכוש חבילה נוספת")



def min_nums_func():
    min_nums = [35,36,37]
    mmax_clicks_allowed_min = 3
    rand = np.random.choice(min_nums, 1, replace=False)

    if min_bttn:
        if st.session_state.clock_count < mmax_clicks_allowed_min:
            st.session_state.clock_count += 1
            st.write(rand)
            st.warning(f"נשאר לך שימושים {mmax_clicks_allowed_min - st.session_state.clock_count}  ")
        else:
            st.error("ניצלת את כל השימושים. עליך לרכוש עוד כדי להמשיך להשתמש בשירות")

            # st.date_input()
            # st.number_input()





st.divider()
with container2:
    st.info("הכנס את החודש שאתה מעוניין לבדוק")
    month_of_interest = st.text_input("הכנס חודש(מספר)")
    num_of_nums = num_of_nums_requested = st.text_input("כמה מספרים אתה מעוניין לגלות (מ-1 עד 6)")
    max_nums_bttn = st.button("מצא לי את המספרים הכי טובים לחודש זה!", on_click=main)
    min_bttn = st.button("הצג לי את המספר הכי חלש החודש" , on_click=min_nums_func)
st.divider()


# if __name__ == "__main__":
#     main()
