import streamlit as st
import requestdata
import pandas as pd
import pickle

def main():
    st.title("The Spotify Music Recommender")
    html_temp = """
    <div style="background-color:black ;padding:10px">
    <h2 style="color:white;text-align:center;"> PyTunes </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.header(" DISCOVER THE ALBUMS YOU WOULD LOVE, HERE ! ")
    song_url1 = st.text_input("Enter the spotify web player's url of the spotify Album you love:")
    df3=pd.read_csv('clust.csv')
    list1=[]
    for i in range(1928,2021):
        list1.append(i)
    tuple1=tuple(list1)
    display = tuple1
    options = list(range(len(display)))
    value = st.selectbox("what year do you want to musically explore?", options, format_func=lambda x: display[x])
    value=value+1928
    
    
  
    
    st.sidebar.header("EXPLORE MUSIC LIKE NEVER BEFORE!")
    st.sidebar.subheader("What can PyTunes do for you?")
    st.sidebar.markdown("PyTunes is your Musical Genie! Bored of listening to the same songs again and again? PyTunes will suggest you songs based on your musical taste and preference! We have a repository of songs right from the 1920's to 2020!  ")
    st.sidebar.subheader("How does it work?")
    st.sidebar.markdown("Go to spotify's Webplayer(here: https://tinyurl.com/ybbv2frv) and copy the URL of the Album or the Playlist you love! Enter the time period you would like to visit! PyTune's recommender algorithm will analyse your Musical preference and cherry pick spotify's tracks just for you, based on your Musical taste! Enjoy these recommendations!")
    st.sidebar.subheader("Created By:")
    st.sidebar.markdown("Saurabh Khanolkar")
    st.sidebar.markdown("Email : saurabh.khanolkar@gmail.com")
    st.sidebar.markdown("Linkedin : https://tinyurl.com/ybbegcs4")
    st.sidebar.subheader("A shoutout to Spotify's Web API for making this possible!")
    
    
    try:
        if st.button("Recommend me Albums!"):
            x=song_url1.split('/')
            song_url=x[4]
            y=song_url.split('?')
            song_url2=y[0]
            r=requestdata.pora_idalbum(song_url2)
            df=pd.DataFrame(r)
            loadpkl=pickle.load(open('model1.pkl','rb'))
            pred=loadpkl.predict(df)
            st.write("You might like these Albums:")
            
            for i in range(len(df3)):
                if(df3['year'][i]==value):
                    break
            
            for q in range(len(df3)):
                if(df3['year'][q]==value+1):
                    break
            
            count=0
            for r in range(i+2,q+3):
                if(pred==df3['0'][r]):
                    st.write(df3['name'][r])
                    count=count+1
                    if count>5:
                        break
    
    except:
        st.write("Please enter a valid spotify album url!!")
        
    st.header(" DISCOVER THE PLAYLISTS YOU WOULD LOVE, HERE ! ")
    song_url3 = st.text_input("Enter the spotify webplayer's url of the spotify playlist you love:")
    list1=[]
    for i in range(1928,2021):
        list1.append(i)
    tuple1=tuple(list1)
    display = tuple1
    options = list(range(len(display)))
    value = st.selectbox("what year will you musically explore?", options, format_func=lambda x: display[x])
    value=value+1928
    
    try:
    
        if st.button("Recommend me playlists!"):
            x=song_url3.split('/')
            song_url=x[4]
            y=song_url.split('?')
            song_url4=y[0]
            
            r=requestdata.pora_idplaylist(song_url4)
            df=pd.DataFrame(r)
            loadpkl=pickle.load(open('model1.pkl','rb'))
            pred=loadpkl.predict(df)
            st.write("You might like these Tracks:")
            
            for i in range(len(df3)):
                if(df3['year'][i]==value):
                    break
            
            for q in range(len(df3)):
                if(df3['year'][q]==value+1):
                    break
            
            count=0
            for r in range(i+2,q+3):
                if(pred==df3['0'][r]):
                    st.write(df3['name'][r])
                    count=count+1
                    if count>5:
                        break
         
    except:
             st.write("Please enter a valid spotify playlist url!!")
        
            
    st.markdown('<b>CHECK OUT THE SIDEBAR FOR MORE INFORMATION!</b>', unsafe_allow_html=True)   
       


if __name__=='__main__':
    main()
