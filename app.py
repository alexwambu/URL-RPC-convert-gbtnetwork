import streamlit as st
from web3 import Web3

st.set_page_config(page_title="GBTNetwork Multi-RPC Monitor", page_icon="🌐")

# Stored RPCs in app session
if "rpc_list" not in st.session_state:
    st.session_state.rpc_list = [
        "https://gbtnetwork-render.onrender.com",  # Default
        "https://rpc.ankr.com/eth",                # Ethereum
        "https://bsc-dataseed.binance.org/"        # BSC
    ]

st.title("🔁 GBTNetwork RPC Multi-Connector")
st.markdown("Monitor and switch between multiple live RPC nodes without losing the original one.")

# Show stored RPCs
st.markdown("### 🔗 Stored RPC URLs:")
for i, rpc in enumerate(st.session_state.rpc_list):
    st.write(f"{i+1}. {rpc}")

# Add RPC
new_rpc = st.text_input("➕ Add a new RPC URL (must start with http/https):", "")
if st.button("Add RPC"):
    if new_rpc.startswith("http"):
        if new_rpc not in st.session_state.rpc_list:
            st.session_state.rpc_list.append(new_rpc)
            st.success("✅ RPC added.")
        else:
            st.warning("⚠️ RPC already exists.")
    else:
        st.error("❌ Invalid URL.")

# Choose RPC
active_rpc = st.selectbox("🌍 Select RPC to use:", st.session_state.rpc_list)

# Connect
try:
    w3 = Web3(Web3.HTTPProvider(active_rpc))
    if w3.isConnected():
        st.success(f"✅ Connected to Chain ID: `{w3.eth.chain_id}` | Block #{w3.eth.block_number}")
    else:
        st.error("❌ Connection failed.")
except Exception as e:
    st.error(f"❌ Error: {e}")

# Batch test
if st.button("🧪 Test All RPCs"):
    for rpc in st.session_state.rpc_list:
        try:
            temp = Web3(Web3.HTTPProvider(rpc))
            if temp.isConnected():
                st.write(f"✅ {rpc} → Chain ID: {temp.eth.chain_id} | Block: {temp.eth.block_number}")
            else:
                st.write(f"❌ {rpc} → Not Connected")
        except Exception as err:
            st.write(f"❌ {rpc} → Error: {err}")
