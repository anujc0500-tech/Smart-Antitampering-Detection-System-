import streamlit as st

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Smart Anti-Tampering System",
    page_icon="🛡️",
    layout="wide"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
background:linear-gradient(135deg,#0f172a,#1e3a8a,#2563eb);
}

.hero{
padding:35px;
border-radius:20px;
background:rgba(255,255,255,0.12);
backdrop-filter:blur(12px);
box-shadow:0px 8px 25px rgba(0,0,0,0.3);
}

.feature-card{
background:white;
padding:20px;
border-radius:18px;
box-shadow:0 8px 20px rgba(0,0,0,.15);
transition:0.3s;
height:220px;
}

.feature-card:hover{
transform:translateY(-8px);
}

.bigtitle{
font-size:55px;
font-weight:bold;
color:white;
}

.subtitle{
font-size:22px;
color:white;
}

</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🔍 Verify Product",
        "📊 Dashboard",
        "📜 History",
        "🚀 Future",
        "ℹ About"
    ]
)

# -------------------- HOME --------------------

if page=="🏠 Home":

    left,right=st.columns([2,1])

    with left:

        st.markdown("""
<div class='hero'>

<div class='bigtitle'>
🛡 Smart Anti-Tampering System
</div>

<br>

<div class='subtitle'>
Protecting consumers from expiry-date fraud using
Digital Authentication,
QR Verification,
and Smart Detection.
</div>

</div>
""",unsafe_allow_html=True)

        st.write("")

        st.button("Verify Product")

    with right:

        st.success("✅ VERIFIED & SAFE")

        st.image(
            "https://images.unsplash.com/photo-1542838132-92c53300491e",
            use_container_width=True
        )

    st.write("")
    st.write("")

    st.header("Key Features")

    c1,c2,c3,c4=st.columns(4)

    with c1:

        st.markdown("""
<div class='feature-card'>

# 🛡

### Anti-Tampering

Detect expiry date manipulation.

</div>
""",unsafe_allow_html=True)

    with c2:

        st.markdown("""
<div class='feature-card'>

# 📱

### QR Verification

Instant product authentication.

</div>
""",unsafe_allow_html=True)

    with c3:

        st.markdown("""
<div class='feature-card'>

# ❤️

### Consumer Safety

Protect customers from fake products.

</div>
""",unsafe_allow_html=True)

    with c4:

        st.markdown("""
<div class='feature-card'>

# 📊

### Analytics

Track all verification records.

</div>
""",unsafe_allow_html=True)

    st.divider()

    st.header("How It Works")

    s1,s2,s3,s4=st.columns(4)

    s1.info("① Scan QR")
    s2.info("② Verify Product")
    s3.info("③ Check Database")
    s4.success("④ Safe / Tampered Result")import streamlit as st

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Smart Anti-Tampering System",
    page_icon="🛡️",
    layout="wide"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
background:linear-gradient(135deg,#0f172a,#1e3a8a,#2563eb);
}

.hero{
padding:35px;
border-radius:20px;
background:rgba(255,255,255,0.12);
backdrop-filter:blur(12px);
box-shadow:0px 8px 25px rgba(0,0,0,0.3);
}

.feature-card{
background:white;
padding:20px;
border-radius:18px;
box-shadow:0 8px 20px rgba(0,0,0,.15);
transition:0.3s;
height:220px;
}

.feature-card:hover{
transform:translateY(-8px);
}

.bigtitle{
font-size:55px;
font-weight:bold;
color:white;
}

.subtitle{
font-size:22px;
color:white;
}

</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🔍 Verify Product",
        "📊 Dashboard",
        "📜 History",
        "🚀 Future",
        "ℹ About"
    ]
)

# -------------------- HOME --------------------

if page=="🏠 Home":

    left,right=st.columns([2,1])

    with left:

        st.markdown("""
<div class='hero'>

<div class='bigtitle'>
🛡 Smart Anti-Tampering System
</div>

<br>

<div class='subtitle'>
Protecting consumers from expiry-date fraud using
Digital Authentication,
QR Verification,
and Smart Detection.
</div>

</div>
""",unsafe_allow_html=True)

        st.write("")

        st.button("Verify Product")

    with right:

        st.success("✅ VERIFIED & SAFE")

        st.image(
            "https://images.unsplash.com/photo-1542838132-92c53300491e",
            use_container_width=True
        )

    st.write("")
    st.write("")

    st.header("Key Features")

    c1,c2,c3,c4=st.columns(4)

    with c1:

        st.markdown("""
<div class='feature-card'>

# 🛡

### Anti-Tampering

Detect expiry date manipulation.

</div>
""",unsafe_allow_html=True)

    with c2:

        st.markdown("""
<div class='feature-card'>

# 📱

### QR Verification

Instant product authentication.

</div>
""",unsafe_allow_html=True)

    with c3:

        st.markdown("""
<div class='feature-card'>

# ❤️

### Consumer Safety

Protect customers from fake products.

</div>
""",unsafe_allow_html=True)

    with c4:

        st.markdown("""
<div class='feature-card'>

# 📊

### Analytics

Track all verification records.

</div>
""",unsafe_allow_html=True)

    st.divider()

    st.header("How It Works")

    s1,s2,s3,s4=st.columns(4)

    s1.info("① Scan QR")
    s2.info("② Verify Product")
    s3.info("③ Check Database")
    s4.success("④ Safe / Tampered Result")import streamlit as st

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Smart Anti-Tampering System",
    page_icon="🛡️",
    layout="wide"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
background:linear-gradient(135deg,#0f172a,#1e3a8a,#2563eb);
}

.hero{
padding:35px;
border-radius:20px;
background:rgba(255,255,255,0.12);
backdrop-filter:blur(12px);
box-shadow:0px 8px 25px rgba(0,0,0,0.3);
}

.feature-card{
background:white;
padding:20px;
border-radius:18px;
box-shadow:0 8px 20px rgba(0,0,0,.15);
transition:0.3s;
height:220px;
}

.feature-card:hover{
transform:translateY(-8px);
}

.bigtitle{
font-size:55px;
font-weight:bold;
color:white;
}

.subtitle{
font-size:22px;
color:white;
}

</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🔍 Verify Product",
        "📊 Dashboard",
        "📜 History",
        "🚀 Future",
        "ℹ About"
    ]
)

# -------------------- HOME --------------------

if page=="🏠 Home":

    left,right=st.columns([2,1])

    with left:

        st.markdown("""
<div class='hero'>

<div class='bigtitle'>
🛡 Smart Anti-Tampering System
</div>

<br>

<div class='subtitle'>
Protecting consumers from expiry-date fraud using
Digital Authentication,
QR Verification,
and Smart Detection.
</div>

</div>
""",unsafe_allow_html=True)

        st.write("")

        st.button("Verify Product")

    with right:

        st.success("✅ VERIFIED & SAFE")

        st.image(
            "https://images.unsplash.com/photo-1542838132-92c53300491e",
            use_container_width=True
        )

    st.write("")
    st.write("")

    st.header("Key Features")

    c1,c2,c3,c4=st.columns(4)

    with c1:

        st.markdown("""
<div class='feature-card'>

# 🛡

### Anti-Tampering

Detect expiry date manipulation.

</div>
""",unsafe_allow_html=True)

    with c2:

        st.markdown("""
<div class='feature-card'>

# 📱

### QR Verification

Instant product authentication.

</div>
""",unsafe_allow_html=True)

    with c3:

        st.markdown("""
<div class='feature-card'>

# ❤️

### Consumer Safety

Protect customers from fake products.

</div>
""",unsafe_allow_html=True)

    with c4:

        st.markdown("""
<div class='feature-card'>

# 📊

### Analytics

Track all verification records.

</div>
""",unsafe_allow_html=True)

    st.divider()

    st.header("How It Works")

    s1,s2,s3,s4=st.columns(4)

    s1.info("① Scan QR")
    s2.info("② Verify Product")
    s3.info("③ Check Database")
    s4.success("④ Safe / Tampered Result")# -------------------- DASHBOARD --------------------

elif page == "📊 Dashboard":

    import pandas as pd
    import plotly.express as px

    st.title("📊 Analytics Dashboard")

    st.write("Real-Time Product Verification Statistics")

    st.write("")

    # ---------------- KPI CARDS ----------------

    c1,c2,c3,c4=st.columns(4)

    with c1:
        st.metric(
            "Products Verified",
            "2,580",
            "+152 Today"
        )

    with c2:
        st.metric(
            "Authentic Products",
            "2,430",
            "+95%"
        )

    with c3:
        st.metric(
            "Tampered Products",
            "150",
            "-12%"
        )

    with c4:
        st.metric(
            "Consumer Reports",
            "74",
            "+8"
        )

    st.divider()

    # ---------------- PIE CHART ----------------

    pie = pd.DataFrame({

        "Status":[
            "Authentic",
            "Tampered"
        ],

        "Products":[
            2430,
            150
        ]

    })

    fig = px.pie(

        pie,

        names="Status",

        values="Products",

        hole=.55,

        title="Product Verification Results"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ---------------- BAR CHART ----------------

    data = pd.DataFrame({

        "Month":[

            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"

        ],

        "Verified":[

            250,
            410,
            520,
            620,
            780,
            920

        ]

    })

    fig2 = px.bar(

        data,

        x="Month",

        y="Verified",

        text="Verified",

        title="Monthly Product Verification"

    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.divider()

    # ---------------- LINE CHART ----------------

    trend = pd.DataFrame({

        "Week":[

            "Week 1",
            "Week 2",
            "Week 3",
            "Week 4"

        ],

        "Authentic":[

            120,
            180,
            240,
            310

        ],

        "Tampered":[

            18,
            24,
            15,
            11

        ]

    })

    fig3 = px.line(

        trend,

        x="Week",

        y=["Authentic","Tampered"],

        markers=True,

        title="Weekly Verification Trend"

    )

    st.plotly_chart(

        fig3,

        use_container_width=True

    )

    st.divider()

    st.subheader("Performance Summary")

    left,right=st.columns(2)

    with left:

        st.success("""
✔ 95% Products are Genuine

✔ Verification System Working

✔ Consumer Trust Increased

✔ Fraud Cases Reduced
""")

    with right:

        st.info("""
Future AI Features

• Machine Learning Detection

• Blockchain Security

• RFID Tracking

• NFC Verification

• Temperature Monitoring
""")# -------------------- HISTORY --------------------

elif page == "📜 History":

    import pandas as pd

    st.title("📜 Verification History")

    history = pd.DataFrame({

        "Product":[
            "Safe Chips",
            "Fresh Juice",
            "Energy Drink",
            "Chocolate",
            "Cooking Oil"
        ],

        "Batch":[
            "A12BC3D4",
            "J89XZ21",
            "E4521",
            "CH998",
            "CO145"
        ],

        "Expiry":[
            "01/05/2027",
            "12/10/2026",
            "20/11/2026",
            "15/03/2027",
            "10/12/2026"
        ],

        "Status":[
            "Authentic",
            "Authentic",
            "Tampered",
            "Authentic",
            "Tampered"
        ],

        "Time":[
            "10:15 AM",
            "10:40 AM",
            "11:20 AM",
            "12:10 PM",
            "1:05 PM"
        ]

    })

    st.dataframe(history, use_container_width=True)

    st.success("✔ Verification records loaded successfully.")


# -------------------- FUTURE --------------------

elif page == "🚀 Future":

    st.title("🚀 Future Enhancements")

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
### 🤖 AI Detection
Detect tampering automatically using Artificial Intelligence.
""")

        st.info("""
### 🔗 Blockchain
Store product information securely.
""")

        st.info("""
### 📡 RFID
Track products through the supply chain.
""")

        st.info("""
### 📱 Mobile App
Consumers can verify products instantly.
""")

    with col2:
        st.success("""
### 📶 NFC Verification
Tap your phone to verify products.
""")

        st.success("""
### ☁ Cloud Database
Real-time verification from anywhere.
""")

        st.success("""
### 🌡 Temperature Monitoring
Monitor cold-chain products.
""")

        st.success("""
### 📊 Machine Learning
Predict fraud and suspicious activity.
""")


# -------------------- ABOUT --------------------

elif page == "ℹ About":

    st.title("ℹ About This Project")

    st.subheader("Problem")

    st.write("""
Many sellers illegally modify expiry dates using chemicals like acetone,
allowing expired products to be sold again.
This creates serious health risks for consumers.
""")

    st.subheader("Solution")

    st.write("""
Our Smart Anti-Tampering System verifies product authenticity
through QR verification and digital records.
""")

    st.subheader("Objectives")

    st.markdown("""

- Protect consumers

- Reduce food fraud

- Increase manufacturer trust

- Digital product verification

- Prevent expiry-date manipulation

""")

    st.subheader("Innovation")

    st.success("""
A smart verification platform that combines
QR authentication, secure databases,
and future AI-powered tampering detection.
""")

    st.divider()

    st.subheader("Project Team")

    st.write("👨‍💻 Team Name : Your Team")

    st.write("🏫 School : Your School")

    st.write("👨‍🏫 Guide : Project Mentor")

    st.write("📧 Email : your@email.com")

    st.write("📞 Phone : +91-XXXXXXXXXX")

    st.divider()

    st.markdown(
        "<center><h4>Made with ❤️ using Streamlit</h4></center>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<center>Science Exhibition 2026</center>",
        unsafe_allow_html=True
    )
