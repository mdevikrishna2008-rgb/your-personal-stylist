import streamlit as st

# --- Core Data ---
categories = {
    "wedding": ["Religious wedding", "Reception", "Sangeet", "Mehndi", "Engagement"],
    "outing": ["Picnic", "Beach", "Park", "Shopping", "Dinner"],
    "celebration": ["Birthday", "Anniversary", "Promotion", "Graduation", "New Year"],
    "events": ["Conference", "Concert", "Gala", "Seminar", "Exhibition"],
    "tours and adventure": ["Hiking", "Camping", "City Tour", "Safari", "Road Trip"],
    "festival": ["Diwali", "Holi", "Christmas", "Eid", "Halloween"]
}

# --- Utility Functions ---

def generate_color_suggestions(skin_color, undertone):
    colors = []
    if undertone == "warm":
        if skin_color == "fair":
            colors = ["Soft pastels like peach and cream", "Earthy tones: beige, olive green", "Warm neutrals: gold, mustard", "Coral and terracotta", "Avoid: Harsh whites or icy blues"]
        elif skin_color == "medium":
            colors = ["Rich earth tones: brown, rust", "Warm jewel tones: amber, topaz", "Peach and apricot", "Gold and bronze accents", "Avoid: Cool grays or stark blacks"]
        elif skin_color == "olive":
            colors = ["Deep greens, mustard yellow", "Warm reds: terracotta", "Bronze and copper", "Earthy browns", "Avoid: Pale pinks or cool silvers"]
        else:
            colors = ["Bold jewel tones: emerald, ruby", "Deep oranges, golds", "Rich purples, deep blues", "Warm blacks", "Avoid: Dull beiges or pastels"]
    elif undertone == "cool":
        if skin_color == "fair":
            colors = ["Soft pinks, blues, lavenders", "Cool neutrals: gray, silver", "Rose and blush tones", "Icy pastels", "Avoid: Yellows or oranges"]
        elif skin_color == "medium":
            colors = ["Jewel tones: sapphire, ruby", "Cool grays, silvers", "Deep purples, blues", "Rose gold", "Avoid: Earthy browns or warm yellows"]
        elif skin_color == "olive":
            colors = ["Cool greens, teals", "Deep blues, purples", "Silver accents", "Cool reds: burgundy", "Avoid: Warm oranges or golds"]
        else:
            colors = ["Vibrant jewel tones: amethyst, turquoise", "Deep blacks, silvers", "Cool whites, grays", "Bold blues", "Avoid: Muted earth tones"]
    else:
        colors = ["Versatile neutrals: black, white, gray", "Soft pastels: lavender, mint", "Warm-cool mixes: rose, teal", "Beige and taupe", "Avoid: Extreme contrasts"]
    
    return "Recommended Colors for You:\n" + "\n".join(f"- {color}" for color in colors)

def generate_suggestions(main_cat, sub_cat, dress_preference, body_type, skin_color, undertone, climate, event_time):
    body_adjust = {
        "hourglass": "Fitted, accentuating curves.",
        "pear": "A-line, balancing hips.",
        "athletic": "Tailored, structured.",
        "rectangle": "Layered, adding shape.",
        "apple": "Empire-waist, slimming midsection.",
        "inverted triangle": "Wide-leg, softening shoulders.",
        "oval": "Flowy, comfortable.",
        "diamond": "Defined waist, flared bottoms."
    }.get(body_type.lower(), "Versatile pieces.")
    
    climate_adjust = "Light fabrics." if climate.lower() == "hot" else "Warm layers." if climate.lower() == "cold" else "Water-resistant." if climate.lower() == "rainy" else "Breathable."
    avoid = []
    if climate.lower() == "hot":
        avoid.append("Heavy layers or wool.")
    elif climate.lower() == "cold":
        avoid.append("Thin fabrics.")
    elif climate.lower() == "rainy":
        avoid.append("Light colors.")
    
    if main_cat == "wedding":
        if sub_cat == "Religious wedding":
            cat_influence = "Modest, traditional, with cultural elements."
            avoid.append("Revealing outfits or bright casual colors.")
        elif sub_cat == "Reception":
            cat_influence = "Elegant, festive, with sequins or embroidery."
        else:
            cat_influence = "Joyful, family-oriented, with light fabrics."
    elif main_cat == "outing":
        if sub_cat == "Beach":
            cat_influence = "Casual, sun-safe, with swimwear and sunscreen."
            avoid.append("Heavy makeup or formal shoes.")
        elif sub_cat == "Picnic":
            cat_influence = "Comfortable, outdoor-ready, with easy movement."
        elif sub_cat == "Park":
            cat_influence = "Relaxed, nature-inspired, with breathable materials."
        elif sub_cat == "Shopping":
            cat_influence = "Stylish yet practical, with comfortable walking shoes."
        else:
            cat_influence = "Smart casual, with light elegance."
    elif main_cat == "celebration":
        cat_influence = "Fun, celebratory, with pops of color or sparkle."
    elif main_cat == "events":
        if sub_cat == "Concert":
            cat_influence = "Edgy, expressive, with bold accessories."
        elif sub_cat == "Gala":
            cat_influence = "Sophisticated, with formal attire."
        else:
            cat_influence = "Professional, polished."
    elif main_cat == "tours and adventure":
        if sub_cat == "Hiking":
            cat_influence = "Durable, layered for activity, with sturdy shoes."
            avoid.append("Heels or delicate fabrics.")
        elif sub_cat == "Camping":
            cat_influence = "Practical, weather-proof, with multi-use items."
        else:
            cat_influence = "Adventurous, comfortable for travel."
    else:
        cat_influence = "Colorful, thematic, with festive accessories."
    
    outfit_options = []
    if dress_preference == "traditional":
        if main_cat == "outing" and sub_cat == "Beach":
            outfit_options = [
                f"Swim Cover-Up: Light sarong or tunic over swimsuit, {body_adjust}, {climate_adjust}. Try: Cotton for sun protection. Avoid: Heavy embroidery.",
                f"Beach Saree: Casual draped fabric with shorts underneath, sun-safe. Try: Tie-dye patterns. Avoid: Long trails in sand.",
                f"Modest Bikini with Wrap: Traditional modesty with beach fun. Try: Floral prints. Avoid: If not comfortable.",
                f"Salwar for Beach: Loose pants and top for walking. Try: Linen. Avoid: Tight fits.",
                f"Ethnic Dress: Short kurti with capris, practical. Try: Bright colors. Avoid: Formal elements."
            ]
        else:
            outfit_options = [
                f"Embroidered Saree: Flowy silk with {body_adjust}, {cat_influence}. Try: Gold borders. Avoid: Clingy if hot.",
                f"Lehenga Choli: Fitted top with skirt, highlighting {body_type}. Try: Rich reds. Avoid: Overly bright if evening.",
                f"Kurti with Dupatta: Layered tunic, versatile. Try: Cotton. Avoid: Short if professional.",
                f"Salwar Kameez: Balanced fit, elegant. Try: Subtle embroidery. Avoid: Baggy if athletic.",
                f"Anarkali Suit: Long tunic, for {main_cat}. Try: Pastels. Avoid: Heavy if casual."
            ]
    elif dress_preference == "western":
        if main_cat == "outing" and sub_cat == "Beach":
            outfit_options = [
                f"Swim Shorts and Top: Casual shorts with tank, {body_adjust}. Try: Quick-dry fabric. Avoid: Formal tops.",
                f"Bikini with Sarong: Two-piece with wrap, sun-friendly. Try: Bold patterns. Avoid: If modest.",
                f"Beach Dress: Flowy maxi with {climate_adjust}. Try: Sundress style. Avoid: Heavy materials.",
                f"Board Shorts and Tee: Sporty for water activities. Try: Neon colors. Avoid: Dull tones.",
                f"Cover-Up Dress: Light dress over swimsuit. Try: Crochet. Avoid: Opaque if hot."
            ]
        else:
            outfit_options = [
                f"Gown: Floor-length with {body_adjust}, {cat_influence}. Try: A-line. Avoid: Tight if apple.",
                f"Jeans and Top: Denim with shirt, casual. Try: High-waist. Avoid: Low-rise if oval.",
                f"Little Black Dress: Classic sheath. Try: Belts. Avoid: Plain if bold.",
                f"Maxi Dress: Flowy, comfortable. Try: Florals. Avoid: Thin in cold.",
                f"Bodycon Dress: Form-fitting. Try: For hourglass. Avoid: If not confident."
            ]
    elif dress_preference == "indo-western":
        outfit_options = [
            f"Lehenga with Cuts: Traditional with slits, {body_adjust}, {cat_influence}. Try: Shorter hem. Avoid: Too revealing.",
            f"Kurti and Jeans: Ethnic top with pants. Try: Slim fits. Avoid: Mismatches.",
            f"Fusion Blouse: Saree-inspired with jeans. Try: Bold patterns. Avoid: Clashing.",
            f"Jumpsuit: One-piece with touches. Try: For athletic. Avoid: Loose if inverted.",
            f"Skirt Set: Indo-western combo. Try: A-line. Avoid: Short if traditional."
        ]
    else:
        outfit_options = [
            f"Business Suit: Blazer and pants, {body_adjust}, {cat_influence}. Try: Tailored. Avoid: Brights.",
            f"Blouse and Skirt: Button-up with pencil. Try: Silk. Avoid: Casual shoes.",
            f"Blazer Dress: One-piece. Try: For rectangle. Avoid: Fitted if apple.",
            f"Trousers Set: Pants with blouse. Try: Neutrals. Avoid: Patterns if formal.",
            f"Sheath Dress: Slim professional. Try: Jackets. Avoid: Short hems."
        ]
    
    makeup_options = []
    if undertone == "warm":
        if main_cat == "outing" and sub_cat == "Beach":
            makeup_options = [
                f"Sun-Safe Glow: Dewy with SPF foundation. Try: Bronzer. Avoid: Heavy powder.",
                f"Natural Beach Look: Light blush and gloss. Try: Waterproof mascara. Avoid: Smoky eyes.",
                f"Bold Lips: Red lipstick for fun. Try: Nude eyes. Avoid: Cool pinks.",
                f"Minimalist: Just highlighter. Try: Gold. Avoid: Full face.",
                f"Playful: Colorful eyeshadow. Try: Bright liners. Avoid: If modest."
            ]
        else:
            makeup_options = [
                f"Smoky Eyes: Browns and golds. Try: Highlighter. Avoid: Blues.",
                f"Natural Glow: Peach blush. Try: Bronzer. Avoid: Powder.",
                f"Bold Lips: Red lipstick. Try: Nude eyes. Avoid: Cool pinks.",
                f"Glam Highlighter: Warm glow. Try: Gold dust. Avoid: Silvers.",
                f"Contoured: Bronze shading. Try: Earthy. Avoid: Harsh lines."
            ]
    elif undertone == "cool":
        makeup_options = [
            f"Smoky Eyes: Grays and silvers. Try: Blues. Avoid: Yellows.",
            f"Natural Glow: Rosy blush. Try: Pinks. Avoid: Oranges.",
            f"Bold Lips: Berry lipstick. Try: Silver eyeliner. Avoid: Corals.",
            f"Glam Highlighter: Icy shimmer. Try: Pearl. Avoid: Golds.",
            f"Contoured: Gray shading. Try: Jewels. Avoid: Browns."
        ]
    else:
        makeup_options = [
            f"Smoky Eyes: Balanced grays. Try: Versatile. Avoid: Extremes.",
            f"Natural Glow: Mixed blush. Try: Taupe. Avoid: One-tone.",
            f"Bold Lips: Neutral reds. Try: Rose gold. Avoid: Contrasts.",
            f"Glam Highlighter: Soft glow. Try: Beige. Avoid: Over-shine.",
            f"Contoured: Subtle shading. Try: Universal. Avoid: Heavy application."
        ]
    
    shoes_options = []
    if main_cat == "outing":
        if sub_cat == "Beach":
            shoes_options = [
                f"Sandals: Flip-flops for sand. Try: Waterproof. Avoid: Heels.",
                f"Beach Shoes: Strappy sandals. Try: Leather. Avoid: Closed-toe if hot.",
                f"Wedges: Low for walking. Try: Espadrilles. Avoid: High if unsteady.",
                f"Sneakers: Canvas for paths. Try: White. Avoid: Wet conditions.",
                f"Boots: Ankle for protection. Try: Rubber. Avoid: Delicate materials."
            ]
        elif sub_cat == "Picnic":
            shoes_options = [
                f"Sneakers: Comfortable for grass. Try: Canvas. Avoid: Heels.",
                f"Flats: Easy walking. Try: Leather. Avoid: Wet grass.",
                f"Sandals: Open for air. Try: Strappy. Avoid: Muddy areas.",
                f"Boots: Ankle for uneven ground. Try: Waterproof. Avoid: Formal.",
                f"Wedges: Low for balance. Try: Espadrilles. Avoid: High heels."
            ]
        elif sub_cat == "Park":
            shoes_options = [
                f"Sneakers: Breathable for walking. Try: Mesh. Avoid: Heels.",
                f"Flats: Comfortable paths. Try: Ballet. Avoid: Slippery.",
                f"Sandals: Casual stroll. Try: Birkenstocks. Avoid: Rain.",
                f"Boots: For trails. Try: Hiking style. Avoid: Delicate.",
                f"Wedges: Low elevation. Try: Cork. Avoid: Uneven terrain."
            ]
        elif sub_cat == "Shopping":
            shoes_options = [
                f"Sneakers: Walking all day. Try: Supportive. Avoid: Heels.",
                f"Flats: Comfortable stores. Try: Loafers. Avoid: Slippery floors.",
                f"Sandals: Airy for malls. Try: Comfort. Avoid: Outdoor walking.",
                f"Boots: Ankle for support. Try: Chelsea. Avoid: Hot weather.",
                f"Wedges: Low for balance. Try: Block. Avoid: Long distances."
            ]
        else:
            shoes_options = [
                f"Heels: Low for elegance. Try: Nude. Avoid: Too high.",
                f"Flats: Dressy ballet. Try: Satin. Avoid: Casual.",
                f"Sandals: Strappy evening. Try: Heeled. Avoid: Flat.",
                f"Boots: Ankle for polish. Try: Leather. Avoid: Sneakers.",
                f"Wedges: Mid for comfort. Try: Dressy. Avoid: Flats."
            ]
    elif main_cat == "tours and adventure":
        if sub_cat == "Hiking":
            shoes_options = [
                f"Hiking Boots: Sturdy for trails. Try: Waterproof. Avoid: Heels.",
                f"Sneakers: Trail-ready. Try: Grip sole. Avoid: Delicate.",
                f"Sandals: For light hikes. Try: Teva. Avoid: Rocky paths.",
                f"Boots: Ankle support. Try: Gore-Tex. Avoid: Flats.",
                f"Wedges: Low for uneven. Try: Outdoor. Avoid: High."
            ]
        elif sub_cat == "Camping":
            shoes_options = [
                f"Boots: Waterproof for mud. Try: Rubber. Avoid: Open-toe.",
                f"Sneakers: Comfortable camp. Try: Canvas. Avoid: Wet.",
                f"Sandals: For tents. Try: Quick-dry. Avoid: Cold nights.",
                f"Flats: Easy setup. Try: Leather. Avoid: Rough ground.",
                f"Wedges: Low for balance. Try: Espadrilles. Avoid: Heels."
            ]
        else:
            shoes_options = [
                f"Sneakers: Walking city. Try: Comfort. Avoid: Heels.",
                f"Sandals: For travel. Try: Strappy. Avoid: Long walks.",
                f"Boots: For safari. Try: Leather. Avoid: Flats.",
                f"Flats: Dressy tour. Try: Loafers. Avoid: Uneven.",
                f"Wedges: Low for balance. Try: Block. Avoid: High."
            ]
    elif main_cat == "events":
        if sub_cat == "Concert":
            shoes_options = [
                f"Sneakers: Edgy for dancing. Try: Bold. Avoid: Heels.",
                f"Boots: Combat style. Try: Leather. Avoid: Flats.",
                f"Sandals: Platform for fun. Try: Heeled. Avoid: Delicate.",
                f"Wedges: Mid for standing. Try: Espadrilles. Avoid: Low.",
                f"Flats: Comfortable crowd. Try: Canvas. Avoid: Formal."
            ]
        elif sub_cat == "Gala":
            shoes_options = [
                f"Heels: Elegant stilettos. Try: Nude. Avoid: Flats.",
                f"Sandals: Strappy formal. Try: Crystal. Avoid: Sneakers.",
                f"Boots: Ankle for polish. Try: Leather. Avoid: Casual.",
                f"Wedges: Dressy mid. Try: Satin. Avoid: Low.",
                f"Flats: Ballet for comfort. Try: Silk. Avoid: Heels."
            ]
        else:
            shoes_options = [
                f"Flats: Professional. Try: Loafers. Avoid: Heels.",
                f"Sneakers: Comfortable standing. Try: Clean. Avoid: Bright.",
                f"Boots: Ankle for polish. Try: Leather. Avoid: Casual.",
                f"Sandals: Dressy open. Try: Low heel. Avoid: Flats.",
                f"Wedges: Low for balance. Try: Block. Avoid: High."
            ]
    elif main_cat == "festival":
        shoes_options = [
            f"Sandals: Colorful for fun. Try: Beaded. Avoid: Heels.",
            f"Sneakers: Comfortable dancing. Try: Neon. Avoid: Delicate.",
            f"Boots: Edgy for theme. Try: Leather. Avoid: Flats.",
            f"Wedges: Mid for standing. Try: Espadrilles. Avoid: Low.",
            f"Flats: Easy movement. Try: Canvas. Avoid: Formal."
        ]
    else:
        shoes_options = [
            f"Heels: Elegant for event. Try: Nude. Avoid: Flats.",
            f"Sandals: Strappy formal. Try: Heeled. Avoid: Sneakers.",
            f"Boots: Ankle for polish. Try: Leather. Avoid: Casual.",
            f"Wedges: Dressy mid. Try: Satin. Avoid: High.",
            f"Flats: Comfortable. Try: Ballet. Avoid: Heels."
        ]
    
    hair_options = []
    if main_cat == "outing" and sub_cat == "Beach":
        hair_options = [
            f"Beach Waves: Loose curls. Try: Salt spray. Avoid: Straight.",
            f"Ponytail: High for sun. Try: Waterproof. Avoid: Down.",
            f"Braids: For wind. Try: Fishtail. Avoid: Loose.",
            f"Updo: Elegant beach. Try: Chignon. Avoid: Messy.",
            f"Bun: Simple top. Try: Sleek. Avoid: Voluminous."
        ]
    elif main_cat == "tours and adventure" and sub_cat == "Hiking":
        hair_options = [
            f"Ponytail: Practical for activity. Try: High. Avoid: Loose.",
            f"Braids: For movement. Try: French. Avoid: Down.",
            f"Bun: Secure top. Try: Sleek. Avoid: Voluminous.",
            f"Waves: Light curls. Try: Quick. Avoid: Straight.",
            f"Updo: For sweat. Try: Chignon. Avoid: Messy."
        ]
    elif main_cat == "events" and sub_cat == "Concert":
        hair_options = [
            f"Waves: Edgy curls. Try: Bold. Avoid: Straight.",
            f"Braids: Fun weaves. Try: Crown. Avoid: Plain.",
            f"Ponytail: High energy. Try: Sleek. Avoid: Loose.",
            f"Bun: Top knot. Try: Messy. Avoid: Formal.",
            f"Updo: Glamorous. Try: Voluminous. Avoid: Simple."
        ]
    else:
        hair_options = [
            f"Ponytail: Simple high. Try: Sleek. Avoid: Messy.",
            f"Waves: Loose curls. Try: Beachy. Avoid: Straight.",
            f"Bun: Elegant top. Try: Chignon. Avoid: Loose.",
            f"Braids: Intricate. Try: Fishtail. Avoid: If short.",
            f"Updo: Voluminous. Try: Glam. Avoid: Simple."
        ]
    
    accessories_options = []
    if main_cat == "outing" and sub_cat == "Beach":
        accessories_options = [
            f"Sunglasses: UV protection. Try: Aviators. Avoid: None.",
            f"Hat: Wide brim. Try: Straw. Avoid: Small.",
            f"Jewelry: Gold for warm. Try: Studs. Avoid: Heavy.",
            f"Bag: Beach tote. Try: Waterproof. Avoid: Clutch.",
            f"Scarf: Light wrap. Try: Silk. Avoid: Wool."
        ]
    elif main_cat == "tours and adventure" and sub_cat == "Hiking":
        accessories_options = [
            f"Hat: Sun cap. Try: Baseball. Avoid: None.",
            f"Backpack: For gear. Try: Hydration. Avoid: Clutch.",
            f"Jewelry: Minimal. Try: Studs. Avoid: Dangly.",
            f"Sunglasses: Sporty. Try: Polarized. Avoid: Fashion.",
            f"Scarf: Neck gaiter. Try: Quick-dry. Avoid: Silk."
        ]
    elif main_cat == "events" and sub_cat == "Concert":
        accessories_options = [
            f"Jewelry: Bold. Try: Statement. Avoid: Minimal.",
            f"Bag: Crossbody. Try: Edgy. Avoid: Clutch.",
            f"Hat: Fun cap. Try: Beanie. Avoid: Formal.",
            f"Scarf: Colorful. Try: Bandana. Avoid: Plain.",
            f"Sunglasses: Cool. Try: Wayfarers. Avoid: None."
        ]
    else:
        accessories_options = [
            f"Jewelry: Gold/silver. Try: Studs. Avoid: Overload.",
            f"Bag: Clutch/handbag. Try: Structured. Avoid: Bulky.",
            f"Scarf: Silk. Try: Matching. Avoid: Clashing.",
            f"Belts: Leather. Try: For shape. Avoid: Wide if apple.",
            f"Hats: Sun hat. Try: Wide brim. Avoid: Windy."
        ]
    
    color_sugs = generate_color_suggestions(skin_color, undertone)
    
    outfit_str = "\n".join(f"{i+1}. {opt}" for i, opt in enumerate(outfit_options))
    makeup_str = "\n".join(f"{i+1}. {opt}" for i, opt in enumerate(makeup_options))
    shoes_str = "\n".join(f"{i+1}. {opt}" for i, opt in enumerate(shoes_options))
    hair_str = "\n".join(f"{i+1}. {opt}" for i, opt in enumerate(hair_options))
    accessories_str = "\n".join(f"{i+1}. {opt}" for i, opt in enumerate(accessories_options))

    full_look = f"""
        **{color_sugs}**

        ### Outfit Options
        {outfit_str}

        ### Makeup Options
        {makeup_str}

        ### Shoes Options
        {shoes_str}

        ### Hair Options
        {hair_str}

        ### Accessories Options
        {accessories_str}
    """
    
    avoid_list = "What to avoid: " + ", ".join(avoid) if avoid else "No major avoidances."
    
    return full_look, avoid_list


# --- Streamlit UI (main) ---
st.set_page_config(
    page_title="Personal Fashion Designer Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Welcome to your Personal Fashion Designer Assistant! What can I do for you today?")
st.markdown("Let's create the perfect look for your event.")
st.markdown("---")

## 1. Event Type Selection
st.header("1. Event Type Selection")
st.markdown("Let's start by choosing the event type.")

col1, col2 = st.columns(2)

with col1:
    main_cat_key = st.selectbox(
        "Choose a main category:",
        list(categories.keys()),
        format_func=lambda x: x.capitalize(),
        key="main_cat"
    )

with col2:
    sub_cats = categories.get(main_cat_key, [])
    sub_cat = st.selectbox(
        f"Subcategories for {main_cat_key.capitalize()}:",
        sub_cats,
        key="sub_cat"
    )

dress_preference = st.radio(
    "\nWhat dress style do you prefer?",
    ["Traditional (e.g., sarees, lehengas)", "Western (e.g., dresses, jeans)", "Indo-western (e.g., fusion styles)", "Professional (e.g., suits, blouses)"],
    key="dress_pref"
).split(" (")[0].lower()

st.markdown("---")

## 2. Personalized Details
st.header("2. Personalized Details")
st.markdown("Now, please provide more details for a personalized look:")

# Body Type
st.subheader("Body Type")
st.markdown("""
Body type refers to your overall shape (e.g., how weight is distributed). Common types:
- Hourglass: Balanced bust and hips, narrow waist.
- Pear: Wider hips, narrower shoulders.
- Athletic: Muscular, less curves.
- Rectangle: Straight up and down, little waist definition.
- Apple: Fuller midsection, slimmer legs.
- Inverted Triangle: Broad shoulders, narrower hips.
- Oval: Fuller figure, soft curves.
- Diamond: Wider hips, defined waist, narrower bust.
""")
body_type_options = ["I don't know", "Hourglass", "Pear", "Athletic", "Rectangle", "Apple", "Inverted Triangle", "Oval", "Diamond"]
body_type_raw = st.selectbox("Your body type:", body_type_options, index=0, key="body_type_select")

if body_type_raw == "I don't know":
    st.info("Tip: Stand in front of a mirror—measure bust, waist, hips. Or think of celebrities: hourglass like Marilyn Monroe, pear like Beyoncé.")
    body_type = st.text_input("Try again or pick one:", key="body_type_text").strip().lower()
else:
    body_type = body_type_raw.strip().lower()


# Skin Color and Undertone
col3, col4 = st.columns(2)
with col3:
    st.subheader("Skin & Undertone")
    st.markdown("Skin color refers to your overall tone (e.g., fair, medium, olive, dark). If unsure, think of your natural shade.")
    skin_color = st.text_input("Skin color (e.g., fair, medium, olive, dark):", key="skin_color").strip().lower()
    
with col4:
    st.markdown("Undertone is the subtle color beneath your skin: warm (yellow/golden undertones, like peachy veins), cool (pink/blue undertones, like bluish veins), neutral (mix of both).")
    undertone_options = ["I don't know", "Warm", "Cool", "Neutral"]
    undertone_raw = st.selectbox("Undertone:", undertone_options, index=0, key="undertone_select")
    
    if undertone_raw == "I don't know":
        st.info("Tip: Check vein color on your wrist or what makeup colors flatter you (e.g., if yellow looks good, warm).")
        undertone = st.text_input("Try again or pick one (warm, cool, neutral):", key="undertone_text").strip().lower()
    else:
        undertone = undertone_raw.strip().lower()


# Climate and Time
col5, col6 = st.columns(2)
with col5:
    st.subheader("Contextual Details")
    st.markdown("Climate affects fabric choices (e.g., hot = light, cold = warm).")
    climate = st.selectbox("Today's climate:", ["Hot", "Mild", "Cold", "Rainy"], key="climate_select").strip().lower()
    
with col6:
    st.markdown("Event time influences formality (e.g., evening = glamorous).")
    event_time = st.selectbox("Event time:", ["Morning", "Afternoon", "Evening", "Night"], key="event_time_select").strip().lower()

st.markdown("---")

## 3. Generate Look
if st.button("Get My Complete Personalized Look", use_container_width=True, type="primary"):
    
    if not (skin_color and undertone and body_type):
        st.error("Please ensure you have filled in your Skin Color, Body Type, and Undertone for the best results!")
    else:
        full_look, avoid_list = generate_suggestions(
            main_cat_key, sub_cat, dress_preference, body_type, skin_color, undertone, climate, event_time
        )
        
        st.success(f"Your Personalized Look for a {sub_cat} event at {event_time.capitalize()} in a {climate.capitalize()} climate is ready!")
        
        st.markdown(full_look)
        
        st.markdown("---")
        
        st.subheader("Important Styling Note")
        st.warning(avoid_list)
        

        # Feedback Section (mimicking your original logic)
        st.markdown("---")
        st.subheader("Refinement")
        st.markdown("Any suggestions or changes? (e.g., 'Choose option 2 for outfit'). Type 'none' if happy:")
        
        feedback = st.text_input("Feedback:", key="feedback").strip()
        
        if feedback:
            if feedback.lower() == "none":
                st.info("Perfect! Your look is ready. Thank you! Run again for another look.")
            else:
                st.info(f"Refined look: (Displayed above)\nAdjusted: **{feedback}**.")
                st.markdown("*(Note: The AI's full refinement logic is complex, but this acknowledges your request!)*")
