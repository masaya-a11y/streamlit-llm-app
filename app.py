import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# LLM応答関数
def get_llm_response(user_input: str, expert_type: str) -> str:
    expert_system_messages = {
        "医療専門家": "あなたは医療分野の専門家です。専門的かつ分かりやすく回答してください。",
        "法律専門家": "あなたは法律分野の専門家です。法的観点から丁寧に回答してください。",
        "IT専門家": "あなたはIT分野の専門家です。技術的な観点から分かりやすく回答してください。"
    }
    system_message = expert_system_messages.get(expert_type, "あなたは親切なアシスタントです。")
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_input),
    ]
    result = llm(messages)
    return result.content

# Webアプリ概要・操作説明
st.title("LLM専門家相談アプリ")
st.markdown("""
このアプリは、AI専門家に質問できるWebアプリです。  
下記の手順でご利用ください。  
1. 専門家の種類を選択してください。  
2. 質問内容を入力し、「送信」ボタンを押してください。  
AIが専門家として回答します。
""")

# 専門家選択
expert_type = st.radio(
    "専門家の種類を選択してください：",
    ("医療専門家", "法律専門家", "IT専門家")
)

# 入力フォーム
user_input = st.text_area("質問内容を入力してください：")

# 送信ボタン
if st.button("送信"):
    if user_input.strip():
        response = get_llm_response(user_input, expert_type)
        st.markdown("### 回答")
        st.write(response)
    else:
        st.warning("質問内容を入力してください。")

