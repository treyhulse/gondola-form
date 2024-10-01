import streamlit as st

# Set up layout with two columns: left for form, right for image
col1, col2 = st.columns([1, 1.5])

# Left Column: Form
with col1:
    st.title("Parts List Generator")

    # Configuration Selection
    st.subheader("Configuration")
    configuration = st.radio("Select Configuration", ["Island/Gondola", "Wall"], index=0, horizontal=True)

    # Height Selection with Slider
    st.subheader("Height")
    selected_height = st.slider("Select Height", min_value=48, max_value=96, step=6, value=48)

    # Width Selection with Slider
    st.subheader("Width")
    selected_width = st.slider("Select Width", min_value=2, max_value=4, step=1, value=2)

    # Color Selection
    st.subheader("Color")
    color = st.radio("Select Color", ["CHR", "PLT"], index=0, horizontal=True)

    # Side A Back Panel Type
    st.subheader("Side A Back Panel Type")
    side_a_panel = st.radio("Select Side A Panel Type", ["P", "M"], index=0, horizontal=True)

    # Side B Back Panel Type
    st.subheader("Side B Back Panel Type")
    side_b_panel = st.radio("Select Side B Panel Type", ["P", "M", "None"], index=0, horizontal=True)

    # Side A Base Depth with Slider
    st.subheader("Side A Base Depth")
    selected_base_depth_a = st.slider("Select Side A Base Depth", min_value=13, max_value=31, step=3, value=13)

    # Side B Base Depth with Slider
    st.subheader("Side B Base Depth")
    selected_base_depth_b = st.slider("Select Side B Base Depth", min_value=13, max_value=31, step=3, value=13)

    # Upper Shelf Quantity with Slider
    st.subheader("Upper Shelf Quantity")
    upper_shelf_qty = st.slider("Select Upper Shelf Quantity", min_value=0, max_value=6, step=1, value=0)

    # Upper Shelf Type
    st.subheader("Upper Shelf Type")
    upper_shelf_type = st.radio("Select Upper Shelf Type", ["TL", "DL"], index=0, horizontal=True)

    # Upper Shelf Depth with Slider
    st.subheader("Upper Shelf Depth")
    selected_upper_shelf_depth = st.slider("Select Upper Shelf Depth", min_value=7, max_value=31, step=3, value=7)

    # Base Height
    st.subheader("Base Height")
    base_height = st.radio("Select Base Height", ["LB", "06"], index=0, horizontal=True)

    # Generate Parts List Button
    if st.button("Generate Parts List"):
        st.success("Parts List Generated Successfully!")

# Right Column: Dynamic Image Rendering
with col2:
    st.subheader("Configuration Preview")

    # Placeholder to display dynamic image based on form selections
    # You can replace this with the logic to load and show images as per your requirement
    image_path = f"/mnt/data/config_{configuration.lower()}_{color.lower()}_{selected_height}_{selected_width}.png"

    try:
        st.image(image_path, caption=f"{configuration} Configuration - {color}", use_column_width=True)
    except:
        st.info("Image not available for the selected configuration.")

