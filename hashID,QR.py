import streamlit as st
import qrcode
from PIL import Image
import urllib.parse
import requests

st.title('まずハッシュタグIDを出してみよう')
st.caption('必要な項目を入れよう。これは18.0の場合のものです')

user_id=st.text_input('user_id入力欄')

q=st.text_input('調べたいハッシュタグの名前を書こう。＃はいらないよ')
print(q)
st.button('調べたいこと')

access_token=st.text_input('取得したアクセストークンをいれよう')
st.button('access_token')

def get_hash_id(user_id,q,access_token):
    if not user_id or not q or not access_token:
        return st.text( "未記入の項目があります")
    else:
        base_url="https://graph.facebook.com/v18.0/ig_hashtag_search?"
        params={"user_id":user_id, "q":q,"access_token":access_token}

        encoded_params=urllib.parse.urlencode(params)
        url=base_url+encoded_params
        response = requests.get(url)
        data=response.json()
        
        if 'error' in data:
            return st.text("エラーが表示される場合、何かに問題があると考えられます")
    
        else:
            return st.text( f'表示します{data}')

print(get_hash_id(user_id,q,access_token))


st.title('便利機能')

url = st.text_input('QRコードを生成したいURL:')
print(url)
if st.button('QRコード生成'):
    
    _img= qrcode.make(url)
    _img.save('qrcode.png')
    img=Image.open ('qrcode.png')
    st.image(img)
    

