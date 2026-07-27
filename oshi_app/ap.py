import streamlit as st
import pandas as pd
import os
import uuid
import plotly.express as px
from streamlit_calendar import calendar
import streamlit.components.v1 as components

st.markdown("""
<style>

/* 背景 */
.stApp {
    background: #c7e7f7;
}

/* タイトル */
h1 {
    text-align: center;
}
.stApp {
    color: inherit;
}
div[data-testid="stMetric"] {
    background: white;
    color: #222222;
}

/* 小見出し */
h2, h3 {
    color: #5bb8ff;
}

/* メトリクス（ホームの数字） */
div[data-testid="stMetric"] {
    background: white;
    border: 2px solid #b8e6ff;
    border-radius: 18px;
    padding: 18px;
    box-shadow: 3px 3px 12px rgba(100,180,255,0.2);
}

/* タブ */
button[data-baseweb="tab"] {
    background-color: #e6f7ff;
    border-radius: 12px;
    margin: 0 4px;
    padding: 10px 18px;
    color: #4aa3df;
    font-weight: bold;
}

/* 選択中のタブ */
button[data-baseweb="tab"][aria-selected="true"] {
    background-color: #8fd3ff;
    color: white;
}

/* ボタン */
.stButton > button {
    background-color: #4aa3df;
    color: white;
    border-radius: 12px;
    border: none;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #2d8fd8;
}

/* 入力欄 */
.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    border-radius: 10px;
    border: 2px solid #b8e6ff;
}
.stTextInput input,
.stNumberInput input,
textarea {
    color: black !important;
}
div.stButton > button {
    height: 60px;
    font-size: 22px;
    border-radius: 15px;
}
/* 削除ボタン */
button[kind="secondary"] {
    background-color: #ffe6ee !important;
    color: #ff7fa3 !important;
    border: 1px solid #ffc1d6 !important;
    border-radius: 50px !important;
    font-size: 14px !important;
    height: 35px !important;
    padding: 0 15px !important;
}

button[kind="secondary"]:hover {
    background-color: #ffd1e1 !important;
}

.fc {
    color: black !important;
}

.fc-daygrid-day-number {
    color: black !important;
}

.fc-toolbar-title {
    color: black !important;
}

/* 削除ボタン */
div.delete-btn button{
    background:#ffd6e7 !important;
    color:#ff4f87 !important;
    border:2px solid #ffb6cf !important;
    border-radius:12px !important;
    font-size:14px !important;
    font-weight:bold !important;
    height:38px !important;
}

div.delete-btn button:hover{
    background:#ffc4dc !important;
}

</style>
""", unsafe_allow_html=True)
if "start" not in st.session_state:
    st.session_state.start = False


if not st.session_state.start:

    st.markdown("<br><br>", unsafe_allow_html=True)

    left, center, right = st.columns([0.5, 5, 0.5])

    with center:

        st.markdown("""
        <div style="
            background:#dff4ff;
            border:2px solid #8fd3ff;
            border-radius:18px;
            padding:25px;
            text-align:center;
            font-size:18px;
        ">

        <h2>🌤️ ライトモード推奨</h2>

        <p>
        💙 推し活をもっとかわいく楽しむために！<br><br>
        このアプリはライトモードでの利用を推奨しています。<br>
        右上の「︙」からライトモードに変更してご利用ください✨
        </p>

        </div>
        """, unsafe_allow_html=True)

    # ログイン情報
    if "user_name" not in st.session_state:
        st.session_state.user_name = ""

    if "birthday" not in st.session_state:
        st.session_state.birthday = ""

    if "favorite" not in st.session_state:
        st.session_state.favorite = ""

    st.subheader("ログイン")

    name = st.text_input("👤 名前")

    birthday = st.date_input(
        "🎂 誕生日",
        value=pd.to_datetime("2005-04-2"),  # 初期表示
        min_value=pd.to_datetime("1950-01-01"),
        max_value=pd.Timestamp.today()
    )

    favorite = st.text_input("💙 推し")

    st.markdown('<div class="login-btn">', unsafe_allow_html=True)

    login = st.button("ログイン", key="login_btn")

    st.markdown("</div>", unsafe_allow_html=True)

    if login:

        if name != "" and favorite != "":
            st.session_state.user_name = name
            st.session_state.birthday = birthday.strftime("%Y%m%d")
            st.session_state.favorite = favorite
            st.session_state.start = True
            st.rerun()
        else:
            st.error("名前と推しを入力してください！")

    # ←ここに追加！！
    st.stop()


# ↓ここから下はログイン後だけ実行される
home_tab, goods_tab, live_tab, history_tab, live_list_tab = st.tabs([
    "🏠 ホーム",
    "🛍 グッズ記録",
    "🎤 ライブ記録",
    "📋 購入履歴",
    "🎟 ライブ一覧"
])


user_id = f"{st.session_state.user_name}_{st.session_state.birthday}_{st.session_state.favorite}"

csv_file = f"goods_{user_id}.csv"
live_file = f"live_{user_id}.csv"

image_folder = "live_images"

if not os.path.exists(image_folder):
    os.makedirs(image_folder)

if not os.path.exists(live_file):
    live_df = pd.DataFrame(
       columns=[
            "日付",
            "推し",
            "ライブ名",
            "会場",
            "座席",
            "開演時間",
            "移動時間",
            "交通費",
            "チケット代",
            "満足度",
            "メモ",
            "写真"
        ]
    )
    live_df.to_csv(live_file, index=False)

live_df = pd.read_csv(live_file)

# ライブ日付形式を統一
if len(live_df) > 0:
    live_df["日付"] = pd.to_datetime(
        live_df["日付"], 
        errors="coerce"
    ).dt.strftime("%Y-%m-%d")

# CSVがなければ作成
if not os.path.exists(csv_file):
    df = pd.DataFrame(columns=[
    "日付",
    "推し",
    "カテゴリ",
    "商品名",
    "金額",
    "購入場所",
    "URL",
    "メモ"
    ])
    df.to_csv(csv_file, index=False)

# CSV読み込み
df = pd.read_csv(csv_file)

if "購入場所" not in df.columns:
    df["購入場所"] = ""

if "URL" not in df.columns:
    df["URL"] = ""

if "メモ" not in df.columns:
    df["メモ"] = ""

if "写真" not in live_df.columns:
    live_df["写真"] = ""

# 日付形式を統一
if len(df) > 0:
    df["日付"] = pd.to_datetime(df["日付"], errors="coerce").dt.strftime("%Y-%m-%d")

with home_tab:
    st.title("🎤 推し活ダッシュボード")

    if st.button("🚪 ログアウト"):

        st.session_state.start = False
        st.session_state.user_name = ""
        st.session_state.birthday = ""
        st.session_state.favorite = ""

        st.rerun()

      # 今月の支出
    today = pd.Timestamp.today()

    month_df = df.copy()

    month_df["日付"] = pd.to_datetime(month_df["日付"])

    this_month = month_df[
        (month_df["日付"].dt.month == today.month) &
        (month_df["日付"].dt.year == today.year)
    ]
    month_total = this_month["金額"].sum()

    col1, col2, col3 = st.columns(3)

    col1.metric("🛍 購入回数", len(df))
    col2.metric("💰 合計金額", f"¥{df['金額'].sum():,}")
    col3.metric("💖 推し数", df["推し"].nunique())

    col4, col5 = st.columns(2)

    col4.metric("🎤 ライブ回数", len(live_df))
    col5.metric("📅 今月の支出", f"¥{month_total:,}")

with goods_tab:
    st.title("🛍 グッズ購入記録")

    # 入力フォーム
    with st.form("goods_form"):
        date = st.date_input(
        "購入日",
        key="goods_date"
    )
        idol = st.text_input(
        "推し",
        key="goods_idol"
    )
        category = st.selectbox(
            "カテゴリ",
            ["チケット","CD","Blu-ray","グッズ","ガチャ","トレカ","その他"],
            key="goods_category"
    )
        item = st.text_input(
            "商品名",
            key="goods_item"
    )
        price = st.number_input(
            "金額",
            min_value=0,
            key="goods_price"
    )

        place = st.text_input(
            "🛍 購入場所",
            placeholder="ライブ会場・アニメイト・楽天など",
            key="goods_place"
    )

        url = st.text_input(
            "🔗 商品URL",
            placeholder="https://...",
            key="goods_url"
    )

        memo = st.text_area(
            "📝 メモ",
            key="goods_memo"
    )

        submit = st.form_submit_button("保存")

    # 保存
    if submit:

        if idol == "" or item == "" or price == 0:

            st.error("⚠ 推し・商品名・金額は必須です！")

        else:

            new_data = pd.DataFrame([{
                "日付": date,
                "推し": idol,
                "カテゴリ": category,
                "商品名": item,
                "金額": price,
                "購入場所": place,
                "URL": url,
                "メモ": memo
            }])

            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(csv_file, index=False)

            st.success("保存しました！🎉")

        st.divider()

        st.caption("🗑 間違えた場合はこちら")

        delete_goods = st.selectbox(
            "削除する商品",
            df.index,
            format_func=lambda x:
            f"{df.loc[x,'商品名']}（{df.loc[x,'推し']}）"
        )

        if st.button("グッズ削除"):
            df = df.drop(delete_goods)
            df = df.reset_index(drop=True)
            df.to_csv(csv_file, index=False)

            st.success("削除しました")
            st.rerun()

with live_tab:

    st.title("🎤 ライブ記録")

    with st.form("live_form"):

        live_date = st.date_input(
            "ライブ日",
            key="live_date"
    )

        live_idol = st.text_input(
            "推し",
            key="live_idol"
    )

        live_name = st.text_input(
            "ライブ名",
            key="live_name"
    )

        place = st.text_input(
            "会場",
            key="live_place"
    )

        seat = st.text_input(
            "座席",
            key="live_seat"
    )


        # 詳細入力
        with st.expander("📌 詳細情報を追加"):

            start_time = st.time_input(
                "開演時間",
                key="live_time"
            )

            move_time = st.number_input(
                "家から会場までの移動時間（分）",
                key="live_move",
                min_value=0
            )

            transport_cost = st.number_input(
                "交通費",
                key="live_transport",
                min_value=0
            )

            ticket_cost = st.number_input(
                "チケット代",
                key="live_ticket",
                min_value=0
            )

            memo = st.text_area(
                "メモ",
                key="live_memo"
            )

            photo = st.file_uploader(
                "📷 ライブ写真",
                type=["jpg","jpeg","png"],
                key="live_photo"
            )


            star = st.slider(
                "満足度",
                1,
                5,
                key="live_star"
            )


        submit_live = st.form_submit_button(
            "保存"
        )
    if submit_live:
        photo_path = ""

        if live_idol == "" or live_name == "" or place == "":

            st.error("⚠ 推し・ライブ名・会場は必須です！")

        else:

            photo_path = ""

            if photo is not None:

                ext = photo.name.split(".")[-1]

                filename = f"{uuid.uuid4()}.{ext}"

                photo_path = os.path.join(
                    image_folder,
                    filename
                )

                with open(photo_path, "wb") as f:
                    f.write(photo.getbuffer())

            new_live = pd.DataFrame([{
                "日付": live_date,
                "推し": live_idol,
                "ライブ名": live_name,
                "会場": place,
                "座席": seat,
                "開演時間": start_time,
                "移動時間": move_time,
                "交通費": transport_cost,
                "チケット代": ticket_cost,
                "満足度": star,
                "メモ": memo,
                "写真": photo_path
            }])

            live_df = pd.concat([live_df, new_live], ignore_index=True)

            live_df.to_csv(live_file, index=False)

            st.success("ライブ記録を保存しました！🎉")

    st.subheader("ライブ履歴")

    st.dataframe(live_df)

    st.divider()

    st.caption("🗑削除")


    if len(live_df) > 0:

        delete_live = st.selectbox(
            "削除するライブ",
            live_df.index,
            format_func=lambda x:
            f"{live_df.loc[x,'ライブ名']}（{live_df.loc[x,'推し']}）"
        )


        if st.button("ライブ削除"):

            live_df = live_df.drop(delete_live)
            live_df = live_df.reset_index(drop=True)

            live_df.to_csv(
                live_file,
                index=False
            )

            st.success("削除しました")
            st.rerun()

with history_tab:

    st.title("📋 購入履歴")

    idol_list = sorted(
        df["推し"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    search_idol = st.selectbox(
        "💙 推しで絞り込み",
        ["全員"] + idol_list
    )

    if search_idol == "全員":
        view_df = df
    else:
        view_df = df[df["推し"] == search_idol]

    if len(view_df) == 0:

        st.info("購入履歴がありません")

    else:

        for index, row in view_df.iterrows():

            with st.expander(f"🛍 {row['商品名']}　¥{int(row['金額']):,}"):

                st.write(f"💙 推し：{row['推し']}")
                st.write(f"📅 購入日：{row['日付']}")
                st.write(f"🏷 カテゴリ：{row['カテゴリ']}")
                st.write(f"💰 金額：¥{int(row['金額']):,}")
                st.write(f"🛍 購入場所：{row['購入場所']}")

                url = str(row["URL"])

                if url != "" and url != "nan":
                    st.link_button("🔗 商品ページ", url)

                if row["メモ"] != "":
                    st.info(row["メモ"])

                if st.button("🗑削除", key=f"goods_delete_{index}"):

                    df = df.drop(index).reset_index(drop=True)
                    df.to_csv(csv_file, index=False)
                    st.rerun()

with live_list_tab:

    st.title("🎟 ライブ一覧")

    if len(live_df) == 0:
        st.info("まだライブ登録がありません")

    else:
        for index, row in live_df.iterrows():

            with st.expander(f"🎤 {row['ライブ名']}（{row['日付']}）"):

                st.write(f"💙 推し：{row['推し']}")
                st.write(f"📍 会場：{row['会場']}")
                st.write(f"💺 座席：{row['座席']}")
                st.write(f"⭐ 満足度：{'⭐'*int(row['満足度'])}")

                if row["写真"] != "":

                    st.image(
                        row["写真"],
                        width=350
                    )

                st.divider()

                st.write(f"🕒 開演時間：{row['開演時間']}")
                st.write(f"🚃 移動時間：{row['移動時間']} 分")
                st.write(f"🚗 交通費：¥{int(row['交通費']):,}")
                st.write(f"🎫 チケット代：¥{int(row['チケット代']):,}")

                total = int(row["交通費"]) + int(row["チケット代"])
                st.success(f"💰 合計：¥{total:,}")

                st.write("📝 メモ")
                st.info(row["メモ"])

                if st.button("🗑削除", key=f"delete_{index}"):

                    live_df = live_df.drop(index).reset_index(drop=True)
                    live_df.to_csv(live_file, index=False)
                    st.rerun()


#streamlit run oshi_app/ap.py --server.enableCORS=false
