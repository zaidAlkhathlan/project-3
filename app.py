import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

# Navbar in the header
st.markdown(
    """
    <style>
        .navbar {
            background-color: #7a5536;
            padding: 10px 20px;
            text-align: center;
            font-size: 20px;
        }
        .navbar a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
            font-weight: bold;
        }
        .navbar a:hover {
            text-decoration: underline;
        }
        .content {
            direction: rtl;
            text-align: right;
            padding: 20px;
            margin: 10px 0;
            border-radius: 10px;
            background: #cdc8c840;
        }
        .content h2 {
            color: #7a5536;
            margin-bottom: 20px;
        }
        .content p {
            font-size: 25px;
            color: #7a5536;
            line-height: 1.6;
        }
        .image-container {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }
    </style>
    <div class="navbar">
    </div>
    """, unsafe_allow_html=True
)

# Header Section
col1, col2 = st.columns([6, 1])  
with col2:
    st.image("Photo/Aqqar.png", width=150)  

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([3, 4])  
with col1:
    st.image("Photo/logo.png", width=450)  
with col2:
    st.markdown(
        """
        <div class="content">
            <h2>في الرياض، سكنك المثالي موجود بانتظارك</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

# Introduction Section
st.markdown(
    """
    <div class="content">
        <p>
            الرياض مو بس عاصمة المملكة، أهم وجهة سياحية وأكثر مدينة للفرص الوظيفية
            هذا غير أن بيئتها ومخرجاتها التعليمية عالية، فالإقبال على السكن فيها عالي
        </p>
        <p>
            أكيد قد جاء ببالك وين المكان المثالي لك بالرياض ويناسب تفضيلاتك الشخصية
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Directions and Prices Section
st.markdown(
    """
    <div class="content">
        <p>بداية بنوريك تقسيم جهات الرياض </p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 2])  
with col2:
    st.image("Photo/dire.png", width=550)  
with col1:
    st.image("Photo/copm.png", width=250)  

# House Prices Section
st.markdown(
    """
    <div class="content">
        <p>إذا معك ميزانية حلوة وحاب تشري بيت ملك، خلني اوريك متوسط أسعار البيوت في مناطق الرياض</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 4])  
with col2:
    st.image("Photo/NEC.png", width=1050)  

col1, col2 = st.columns([1, 3])  
with col2:
    st.image("Photo/WS.png", width=900)  

# Land Prices Section
st.markdown(
    """
    <div class="content">
        <p>اذا انت والله تقول لا ودي اشري لي ارض وابني بيتي على كيفي اكيد يهمك سعر المتر</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 4])  
with col2:
    st.image("Photo/MNCS.png", width=1050)  

col1, col2 = st.columns([1, 3])  
with col2:
    st.image("Photo/MWS.png", width=700)  

# Apartment Prices Section
st.markdown(
    """
    <div class="content">
        <p>أما لو كنت عزابي او عايلتك صغيره ودك بسكن على قدك، فالشقق بتكون أسهل عليك هنا يوضح لك اعلى واقل  متوسط اسعار الشقق </p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 4])  
with col2:
    st.image("Photo/Avg5.png", width=1050)  

# Budget Recommendations Section
st.markdown(
    """
    <div class="content">
        <p>  🔹 اغلب الأحياء الأعلى سعرًا موجودة في شمال الرياض، وهذا يعكس أن الطلب هناك مرتفع والأسعار غالبًا مرتفعة بشكل عام.
         </p>

   <p> 🔹 الفرق في الأسعار بينهم يعتمد على الموقع داخل الشمال نفسه، قرب الحي من الطرق الرئيسية، الخدمات، والمشاريع الجديدة اللي تصير حوله.</p>
    </div>
    """,
    unsafe_allow_html=True
)


col1, col2 = st.columns([1, 4])  
with col2:
    st.image("Photo/Avg.png", width=1050)  

# Budget Recommendations Section
st.markdown(
    """
    <div class="content">  
        <p> 🔹 حتى الأحياء الأرخص كلها شمال الرياض بعد!، اذا ميزانيتك تحت المليون، عندك خيارات مثل العقيق والمصيف 
         </p>

   <p> 🔹 لكن لو عندك مجال تدفع فوق المليون بشوي، ممكن تشوف العارض والنرجس </p>
    </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Final Recommendations Section
st.markdown(
    """
    <div class="content">
        <p>اذا والله تشوف ميزانيتك ماتسمح او تحب التغيير ودك تستاجر شقة حاب انوهك لا تتردد باختيار شقتك لان الشقق برياض تتأجر بسرعه مايمديك تستخير الا الطيور طارت بارزاقه</p>
        <p>!!متخيل انه اغلب الشقق ب ١٦ يوم تتأجر</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Conclusion Section
st.markdown(
    """
    <div class="content">
        <p style="font-size: 45px;">! في الرياض، لكل شخص مكانه المثالي</p>
        <p>لو كنت من القصيم وتبي بيت قريب لديرتك وما ماودك بزحمة الرياض، الشمال بيكون الأنسب لك -</p>
        <p>أو إذا جاي للرياض بعرض وظيفي في ليسن فالي، فالغرب هو الخيار المثالي -</p>
        <p>اما اذا تحب الرياض القديمة، مثل قصر الحكم والمعيقلية، فجنوب الرياض هو المكان اللي يوازي ذوقك -</p>
        <p style="font-size: 40px;">الرياض مليانة خيارات! وكل واحد يقدر يلقى المكان اللي يناسبه على حسب ميزانيته وتفضيلاته.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Navbar in the footer
st.markdown(
    """
    <div class="navbar">
    </div>
    """, unsafe_allow_html=True
)




# Load the datasets
@st.cache_data
def load_villa_data():
    villa_file = "Data/Riyadh_Aqqar.xlsx"
    df_villa = pd.read_excel(villa_file, sheet_name="Villas")
    df_villa = df_villa[['الحي', 'السعر الاجمالي']].dropna()
    df_villa.rename(columns={'الحي': 'neighbourhood', 'السعر الاجمالي': 'price'}, inplace=True)
    df_villa['price'] = pd.to_numeric(df_villa['price'], errors='coerce')
    return df_villa.dropna()

@st.cache_data
def load_apartment_data():
    apt_file = "Data/Riyadh_Aqqar.xlsx"
    df_apt = pd.read_excel(apt_file, sheet_name="Apartments")
    df_apt = df_apt[['الحي', 'السعر الاجمالي']].dropna()
    df_apt.rename(columns={'الحي': 'district', 'السعر الاجمالي': 'price'}, inplace=True)
    df_apt['price'] = pd.to_numeric(df_apt['price'], errors='coerce')
    return df_apt.dropna()

villa_data = load_villa_data()
apartment_data = load_apartment_data()

# Streamlit UI
st.title("🏡 أفضل الأحياء في الرياض للشراء")
st.write("أدخل ميزانيتك ونوع العقار لمعرفة أفضل الأحياء المناسبة للشراء في مدينة الرياض.")

# User selects property type
property_type = st.radio("اختر نوع العقار:", ["فيلا", "شقة"])

# Get price range to guide user
if property_type == "شقة":
    min_price, max_price = apartment_data['price'].min(), apartment_data['price'].max()
else:
    min_price, max_price = villa_data['price'].min(), villa_data['price'].max()

st.write(f"💰 نطاق الأسعار المتاح لـ {property_type}: {min_price:,.0f} - {max_price:,.0f} ريال سعودي")

# Set default budget value based on property type
default_budget = max(min_price, 500000) if property_type == "شقة" else max(min_price, 1000000)
budget = st.number_input("أدخل ميزانيتك (بالريال السعودي):", min_value=0, value=int(default_budget), step=50000)

# Load appropriate dataset
if property_type == "فيلا":
    filtered_data = villa_data[villa_data['price'] <= budget]
    location_col = 'neighbourhood'
else:
    filtered_data = apartment_data[apartment_data['price'] <= budget]
    location_col = 'district'

if filtered_data.empty:
    st.warning("⚠️ لا توجد عقارات متاحة ضمن ميزانيتك. حاول زيادة الميزانية أو اختيار نوع عقار آخر.")
else:
    st.subheader("أفضل حي مقترح:")
    best_neighborhood = filtered_data.groupby(location_col)['price'].median().idxmax()
    st.success(f"🏆 أفضل حي يناسب ميزانيتك هو: **{best_neighborhood}** (بناءً على قيمة السعر الوسطي).")
