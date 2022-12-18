import streamlit as st
import numpy as np
# import pandas as pd

hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """


st.set_page_config(page_title="Recipe Quickview", page_icon=":scroll:", layout="centered")

# Title the app
st.title("Recipe Quickview")




recipelist = ["Raviole", "Panettone", "Ragù"]

st.sidebar.header("🪄 Wizard")

chosen = st.sidebar.selectbox("Select Recipe", recipelist)
st.subheader(chosen.upper())

if chosen=="Raviole":
    st.markdown("""

    *Raviole* are sweets that are traditionally found around Bologna, Italy. 
    They are made by filling small discs of pasta with a sweet filling, such as marmalade 
    (in particular `mostarda`) or cream, which is often flavored with vanilla or other aromas. 
    Once baked, they are typically dusted with powdered sugar. Raviole are often made during
    the Christmas holidays. However, they can be enjoyed at any time of year, since they are
    commonly sold at bars and pastry shops.
    """)

    st.image("img/raviole.jpg", use_column_width=True)
    st.subheader("Ingredients")

    m_tot    = st.sidebar.number_input("Set amount of dough (g)", min_value=0, max_value=99999, value=1000, step=50)

    ing_n = ["Flour", "Sugar", "Butter", "Eggs"]
    ing_p = [56,18,14,12]

    ing_p[1]  = st.sidebar.slider(ing_n[1], 15, 25, ing_p[1], step=1, format="%d%%")
    ing_p[2]  = st.sidebar.slider(ing_n[2], 10, 20, ing_p[2], step=1, format="%d%%")
    ing_p[3]  = st.sidebar.slider(ing_n[3], 10, 20, ing_p[3], step=1, format="%d%%")
    ing_p[0]  = 100 - ing_p[1] - ing_p[2] - ing_p[3]

    if (ing_p[0] > 60):
        st.warning("Flour content is too high!", icon="⚠️")
    elif (ing_p[0] < 45):
        st.warning("Flour content is too low!", icon="⚠️")

    ing_p[0]  = st.sidebar.slider(ing_n[0], 45, 60, ing_p[0], step=1, format="%d%%", 
                                  disabled=True)

    st.write("The following table gives amounts for ", int(m_tot/28), "raviole*" )

    # Display Ingredient's Table
    ing_m    = (np.array(ing_p)/100 * m_tot).astype(int).astype(str)
    ing_m[3] = "{:s} ({:.1f}x)".format(ing_m[3], float(ing_m[3])/55)
    ing_m    = np.append(ing_m, [str(round(7*float(ing_m[0])/600)),
                                ing_m[0]+"*",
                                "q.s.",
                                "q.s."])
    ing_n.extend(["Baking powder", "+ Mostarda/Jam", "(opt.) Salt", "(opt.) Lemon zest"])
    tab   = np.rec.fromarrays([ing_n, ing_m], names=["Ingredient","Quantity (g)"])
    st.markdown(hide_table_row_index, unsafe_allow_html=True) # Hide row indices
    st.table(tab)
    st.caption("""
    ** These are approximate quantities assuming that: (1) Each raviola weights 28g, (2) The amount of filling is roughly equal to the amount of flour
    """)