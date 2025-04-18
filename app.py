import streamlit as st


st.set_page_config(layout="wide", initial_sidebar_state="collapsed")


st.markdown(
   """
   <style>
       html, body, #root, .block-container {
           height: 100vh;
           width: 100vw;
           margin: 0;
           padding: 0;
           overflow: hidden;
           font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
           display: flex;
           justify-content: center;
           align-items: center;
           background: radial-gradient(circle, rgba(2,0,36,1) 0%, rgba(126,67,182,1) 64%, rgba(167,129,199,1) 94%);




       /* Hide Streamlit UI elements */
       #MainMenu, header, footer, .stAppHeader {
           display: none;
       }




       .content {
           text-align: center;
           margin: 0;
           padding: 0;
       }




       .title {
            font-size: 4rem;
            font-weight: 700;
            background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(221,209,209,1) 43%, rgba(166,214,212,1) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0 0 1rem 0;
            text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.2);
        }

       .description {
           font-size: 1.125rem;
           color: #cfcfcf;
           margin: 0 0 2rem 0;
       }




       .btn-primary {
           background: linear-gradient(90deg, #a785f7, #8a5dd1);
           color: white;
           padding: 12px 28px;
           border-radius: 9999px;
           font-size: 1rem;
           font-weight: 600;
           border: none;
           cursor: pointer;
           box-shadow: 0 4px 12px rgba(167, 133, 247, 0.3);
           transition: all 0.2s ease-in-out;
           animation: glow 1.5s infinite;
           
       }


       .btn-primary:hover {
           background: linear-gradient(90deg, #8a5dd1, #a785f7);
           box-shadow: 0 6px 16px rgba(167, 133, 247, 0.4);
           transform: translateY(-2px);
       }


       @keyframes glow {
            0% {
                box-shadow: 0 0 10px rgba(167, 133, 247, 0.7);
            }
            50% {
                box-shadow: 0 0 20px rgba(167, 133, 247, 1);
            }
            100% {
                box-shadow: 0 0 10px rgba(167, 133, 247, 0.7);
            }
        }


       @keyframes pulse {
           0% {
               transform: scale(1);
           }
           50% {
               transform: scale(1.05);
           }
           100% {
               transform: scale(1);
           }
   </style>




   <div class="content">
       <div class="title">Dr. Quick</div>
       <div class="description">
           Experience the next generation of human-computer interaction<br>
           with our audio-visual interface.
       </div>
   </div>
   """,
   unsafe_allow_html=True
)
    #    <button class="btn-primary">Let's Get Started →</button>

col1, col2, col3 = st.columns([0.4,0.4,0.1])
with col1:
    st.empty()  # Or add minimal content here

with col2:
    if st.button("Let's Get Started →"):
        st.switch_page("pages/test.py")

with col3:
    st.empty() 