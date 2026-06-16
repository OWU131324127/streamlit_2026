import streamlit as st
import random
import requests

idol_images = {
    "きゅるりんってしてみて": "images/kyururin.jpg",
    "なにわ男子": "images/naiwa.jpg",
    "パンダドラゴン": "images/panda.jpg",
    "LE SSERAFIM": "images/rusera.jpg",
    "M!LK": "images/milk.jpeg",
    "WEST.": "images/west.jpg",
    "中島健人": "images/kento.jpg",
    "Travis Japan": "images/travis.jpg",
    "BIGBANG": "images/bigbang.jpg",
    "BTS": "images/bts.webp",
    "乃木坂46": "images/nagizaka.jpg",
    "TWICE": "images/twice.avif",
    "TWS": "images/tws.jpg",
    "IVE": "images/ive.jpg",
    "Stray Kids": "images/stray.jpg",
    "Hey!Say!JUMP": "images/jump.jpg",
    "GOT7": "images/got7.jpg",
    "King & Prince": "images/kinpri.jpg",
    "NEWS": "images/news.webp",
    "Aぇ! group": "images/Aa.jpg",
    "A.B.C-Z": "images/abc.jpg",
    "YENA": "images/yena.webp",
    "SUPER EIGHT": "images/super.jpg",
    "TOMORROW X TOGETHER": "images/txt.jpg",
    "DOMOTO": "images/domoto.jpg",
    "FRUITS ZIPPER": "images/fruits.jpg",
    "NewJeans": "images/newjeans.jpg",
    "Juice=Juice": "images/juice.jpg",
    "Buono!": "images/buono.jpg",
    "BABYMONSTER": "images/babym.webp",
    "日向坂46": "images/hinatazaka.jpg",
    "Kis-My-Ft2": "images/kismyft2.jpg",
    "Snow Man": "images/snowman.jpg",
    "らぶしっく": "images/lovesick.jpg",
    "Kep1er": "images/kep1er.jpg",
    "IZ*ONE": "images/izone.jpg",
    "悪魔のキッス": "images/akumanokiss.jpg",
    "AiScReam": "images/aiscream.jpg",
    "Billie": "images/billie.jpg",
    "SixTones": "images/sixtones.jpg",
    "B小町": "images/bkomachi.avif",
    "aespa": "images/aespa.png",
    "AVAM": "images/avam.jfif",
    "いぎなり東北産": "images/tohokusan.jpg",
    "SEVENTEEN": "images/seventeen.webp",
    "OH MY GIRL": "images/ohmygirl.jpg",
    "ILLIT": "images/illit.jpg",
    "最終未来少女": "images/saishumirai.png",
    "CANDY TUNE": "images/candytune.jpg",
    "MISAMO": "images/misamo.webp",
    "CUTIE STREET": "images/cutiestreet.jpeg",
    "SAY MY NAME": "images/saymyname.jpg",
    "NMIXX": "images/nmixx.jpg",
    "=LOVE": "images/equalslove.webp",

}

st.title("🎤 推し発見！アイドルおみくじ")
st.caption("好きな数字から今日の推しを診断！")

# 入力
name = st.text_input("名前を入力してください")

number = st.number_input(
    "好きな数字を入力してください（1~100）",
    min_value=1,
    max_value=100,
    value=1
)

# 運勢
fortunes = ["大吉", "中吉", "小吉", "吉"]

# ラッキー行動
actions = [
    "ダンスプラクティス動画を見る",
    "ライブ映像を見る",
    "推しの曲を聴く",
    "カラオケで推し曲を歌う",
    "推しのSNSをチェックする",
    "推し活仲間と話す",

    "推しの最新ニュースを検索する",
    "推しのMVを1本見る",
    "推しの昔の写真を見返す",
    "推しの好きな食べ物を調べる",
    "推しのプロフィールを読む",
    "推しの出演作品を見る",
    "推しの名言を探してみる",
    "推しの誕生日をチェックする",
    "推しのファンアートを見る",
    "推しのライブ衣装を調べる",

    "スマホの壁紙を推しにする",
    "推しの写真を保存する",
    "推しのグッズを整理する",
    "推しのアクリルスタンドと写真を撮る",
    "推しのチェキを見返す",
    "推しグッズを持ってお出かけする",

    "推しの曲を3曲連続で聴く",
    "推しのプレイリストを作る",
    "推しのおすすめ曲を友達に紹介する",
    "推しの好きなところを3つ考える",
    "推しへの応援メッセージを考える",
    "推し活の思い出を振り返る",

    "次のライブやイベント情報を確認する",
    "推し活貯金を100円する",
    "推しカラーのアイテムを身につける",
    "推しのハッシュタグを見てみる",
    "推しに関するクイズを作る",
    "推しの曲を聴きながら散歩する",
    "推しの写真フォルダを整理する",
    "推し活ノートをつける",
    "推しの魅力を誰かに語る",
    "推しへの感謝を心の中で伝える"
]

if st.button("🎯 アイドルおみくじを引く"):

    # 数字によってアイドルを決定
    if number <= 2:
        idol = "きゅるりんってしてみて"
        song = "わたしのex.ダーリン"

    elif number <= 3:
        idol = "なにわ男子"
        song = "ダイヤモンドスマイル"


    elif number <= 4:
        idol = "パンダドラゴン"
        song = "決戦！ヴァレンティーノ"

    elif number <= 6:
        idol = "LE SSERAFIM"
        song = "CRAZY"    
    
    elif number <= 8:
        idol = "M!LK"
        song = "爆裂愛してる"

    elif number <= 10:
        idol = "WEST."
        song = "これでいいのだ！"

    elif number <= 12:
        idol = "中島健人"
        song = "最初はキュン！"

    elif number <= 14:
        idol = "M!LK"
        song = "テレパシー"
    
    elif number <= 16:
        idol = "Travis Japan"
        song = "陰ニモ日向ニモ"

    elif number <= 18:
        idol = "BIGBANG"
        song = "HARUHARU"

    elif number <= 19:
        idol = "BABYMONSTER"
        song = "DRIP"

    elif number <= 20:
        idol = "BTS"
        song = "SWIM"

    elif number <= 21:
        idol = "乃木坂46"
        song = "シンクロニシティ"

    elif number <= 22:
        idol = "TWICE"
        song = "YES or YES"

    elif number <= 23:
        idol = "日向坂46"
        song = "アザトカワイイ"

    elif number <= 24:
        idol = "IVE"
        song = "BANGBANG"

    elif number <= 25:
        idol = "Juice=Juice"
        song = "アモーレ・ファティ"

    elif number <= 26:
        idol = "Stray Kids"
        song = "CASE 143"

    elif number <= 27:
        idol = "Buono!"
        song = "初恋サイダー"

    elif number <= 28:
        idol = "Hey!Say!JUMP"
        song = "encore"

    elif number <= 29:
        idol = "パンダドラゴン"
        song = "万国みゅ～じっく"

    elif number <= 30:
        idol = "GOT7"
        song = "Just right"
    
    elif number <= 31:
        idol = "なにわ男子"
        song = "Poppin’ Hoppin’ Lovin’"

    elif number <= 32:
        idol = "King & Prince"
        song = "HEART"

    elif number <= 33:
        idol = "NEWS"
        song = "KAGUYA"

    elif number <= 34:
        idol = "BTS"
        song = "Stay Gold"

    elif number <= 35:
        idol = "Aぇ! group"
        song = "《A》BEGINNING"

    elif number <= 36:
        idol = "YENA"
        song = "Catch Catch"

    elif number <= 37:
        idol = "SUPER EIGHT"
        song = "ズッコケ男道"

    elif number <= 38:
        idol = "BIGBANG"
        song = "声をきかせて"

    elif number <= 39:
        idol = "Kis-My-Ft2"
        song = "SNOW DOMEの約束"

    elif number <= 40:
        idol = "TOMORROW X TOGETHER"
        song = "Stick With You"

    elif number <= 41:
        idol = "DOMOTO"
        song = "愛のかたまり"

    elif number <= 42:
        idol = "TWICE"
        song = "Like OOH-AHH"

    elif number <= 43:
        idol = "Snow Man"
        song = "ナミダの海を越えて行け"

    elif number <= 44:
        idol = "LE SSERAFIM"
        song = "BOOMPALA"

    elif number <= 45:
        idol = "TOMORROW X TOGETHER"
        song = "ito"

    elif number <= 46:
        idol = "NewJeans"
        song = "Super Shy"

    elif number <= 47:
        idol = "A.B.C-Z"
        song = "砂のグラス"

    elif number <= 48:
        idol = "WEST."
        song = "愛執"

    elif number <= 49:
        idol = "らぶしっく"
        song = "愛されフェイスでありたい！"

    elif number <= 50:
        idol = "Kep1er"
        song = "WA DA DA"

    elif number <= 51:
        idol = "WEST."
        song = "Mood"

    elif number <= 52:
        idol = "Snow Man"
        song = "タペストリー"

    elif number <= 53:
        idol = "IVE"
        song = "I AM"

    elif number <= 54:
        idol = "TOMORROW X TOGETHER"
        song = "9と4分の3番線で君を待つ"

    elif number <= 55:
        idol = "IZ*ONE"
        song = "Panorama"

    elif number <= 56:
        idol = "悪魔のキッス"
        song = "カスタムラブドール"

    elif number <= 57:
        idol = "AiScReam"
        song = "愛♡スクリ～ム！"

    elif number <= 58:
        idol = "Billie"
        song = "GingaMingaYo"

    elif number <= 59:
        idol = "SixTones"
        song = "こっから"

    elif number <= 60:
        idol = "B小町"
        song = "トワイライト"

    elif number <= 61:
        idol = "Snow Man"
        song = "カリスマックス"

    elif number <= 62:
        idol = "aespa"
        song = "Whiplash"

    elif number <= 63:
        idol = "らぶしっく"
        song = "アリスハプニング"

    elif number <= 64:
        idol = "AVAM"
        song = "僕の世界は蒼で染まっていく"

    elif number <= 65:
        idol = "なにわ男子"
        song = "初心LOVE"

    elif number <= 66:
        idol = "IVE"
        song = "ATTITUDE"

    elif number <= 68:
        idol = "FRUITS ZIPPER"
        song = "かがみ"

    elif number <= 70:
        idol = "TWS"
        song = "plot twist"

    elif number <= 72:
        idol = "いぎなり東北産"
        song = "わざとあざとエキスパート"

    elif number <= 74:
        idol = "SEVENTEEN"
        song = "MAESTRO"

    elif number <= 76:
        idol = "TWS"
        song = "OVERDRIVE"

    elif number <= 78:
        idol = "OH MY GIRL"
        song = "Dolphin"

    elif number <= 79:
        idol = "A.B.C-Z"
        song = "JOYしたいキモチ"

    elif number <= 80:
        idol = "ILLIT"
        song = "It's Me"

    elif number <= 82:
        idol = "最終未来少女"
        song = "AI SEE CHAT"

    elif number <= 84:
        idol = "CANDY TUNE"
        song = "キス・ミー・パティシエ"

    elif number <= 85:
        idol = "Travis Japan"
        song = "Tokyo Crazy Night"

    elif number <= 86:
        idol = "B小町"
        song = "SHINING SONG"

    elif number <= 88:
        idol = "MISAMO"
        song = "Marshmallow"

    elif number <= 90:
        idol = "CUTIE STREET"
        song = "かわいいだけじゃだめですか？"

    elif number <= 92:
        idol = "SAY MY NAME"
        song = "ShaLala"

    elif number <= 94:
        idol = "SixTones"
        song = "マスカラ"

    elif number <= 96:
        idol = "NMIXX"
        song = "DICE"

    elif number <= 98:
        idol = "Hey!Say!JUMP"
        song = "Puppy Boo"

    else:
        idol = "=LOVE"
        song = "ラブソングに襲われる"


    fortune = random.choice(fortunes)
    action = random.choice(actions)

    st.markdown("---")

    st.markdown(
    f"<h2 style='text-align:center;'>🌟 {name}さんの診断結果 🌟</h2>",
    unsafe_allow_html=True
    )

    st.write("")

    st.markdown("### 🎤 あなたにおすすめのアイドル")

    st.markdown(
        f"<h1 style='text-align:center;'>💖 {idol} 💖</h1>",
        unsafe_allow_html=True
    )

    if idol in idol_images:
        col1, col2, col3 = st.columns([1, 4, 1])

        with col2:
            st.image(idol_images[idol], use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.link_button(
            "🔍 Google検索",
            f"https://www.google.com/search?q={idol}"
        )

    with col2:
        st.link_button(
            "🎵 YouTube検索",
            f"https://www.youtube.com/results?search_query={idol}+{song}"
        )

    st.write("")

    st.markdown("### 📊 今日の診断結果")

    if fortune == "大吉":
        st.balloons()
        comment = "今日は推し活日和！最高の一日になりそう✨"

    elif fortune == "中吉":
        comment = "良いことが起こる予感！推しの曲をたくさん聴こう🎧"

    elif fortune == "小吉":
        comment = "小さな幸せを見つけられる日かも🍀"

    else:
        comment = "マイペースに推し活を楽しもう😊"

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        <div style="
            border:2px solid #ffb6d9;
            border-radius:25px;
            padding:20px;
            height:180px;
            text-align:center;
        ">
            <h3>🎲 推し活運勢</h3>
            <h2>{fortune}</h2>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        st.markdown(f"""
        <div style="
            border:2px solid #d8c2ff;
            border-radius:25px;
            padding:20px;
            height:auto;
            min-height:200px;
            text-align:center;
        ">
            <h3>💬 メッセージ</h3>
            <h4>{comment}</h4>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="
            border:2px solid #bde9ff;
            border-radius:25px;
            padding:20px;
            height:180px;
            text-align:center;
        ">
            <h3>🎵 おすすめ曲</h3>
            <h3 style="font-size:30px;">{song}</h3>
        </div>
        """, unsafe_allow_html=True)


        st.write("")

        st.markdown(f"""
        <div style="
            border:2px solid #fff0b3;
            border-radius:25px;
            padding:20px;
            height:auto;
            min-height:200px;
            text-align:center;
        ">
            <h3>🍀 ラッキー行動</h3>
            <h4>{action}</h4>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.markdown("---")
    st.markdown(
        """
        <div style="
            text-align:center;
            padding:20px;
        ">
            <h3>💖 Thank You 💖</h3>
            <p>
            おみくじを引いてくれてありがとう！<br>
            素敵な推しとの出会いがありますように✨<br>
            また遊びに来てね 🎤🌈
            </p>
        </div>
        """,
        unsafe_allow_html=True
        )

#streamlit run app.py --server.enableCORS=false
