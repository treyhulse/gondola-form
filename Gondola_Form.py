import streamlit as st

# Set up layout with two columns: left for form, right for image
col1, col2 = st.columns([1, 1.5])

# Left Column: Form
with col1:
    st.title("Parts List Generator")

    # Configuration Selection
    st.subheader("Configuration")
    configuration = st.radio("Select Configuration", ["Island/Gondola", "Wall"], index=0, horizontal=True)

    # Height Selection with Slider using predefined options
    st.subheader("Height")
    heights = [48, 54, 60, 66, 72, 78, 84, 90, 96]
    selected_height = st.slider("Select Height", min_value=min(heights), max_value=max(heights), step=6, value=min(heights), format="%d")

    # Width Selection with Slider using predefined options
    st.subheader("Width")
    widths = [2, 3, 4]
    selected_width = st.select_slider("Select Width", options=widths, value=widths[0])

    # Color Selection
    st.subheader("Color")
    color = st.radio("Select Color", ["CHR", "PLT"], index=0, horizontal=True)

    # Side A Back Panel Type
    st.subheader("Side A Back Panel Type")
    side_a_panel = st.radio("Select Side A Panel Type", ["P", "M"], index=0, horizontal=True)

    # Side B Back Panel Type
    st.subheader("Side B Back Panel Type")
    side_b_panel = st.radio("Select Side B Panel Type", ["P", "M", "None"], index=0, horizontal=True)

    # Side A Base Depth with Slider using predefined options
    st.subheader("Side A Base Depth")
    base_depth_a_options = [13, 16, 19, 22, 25, 28, 31]
    selected_base_depth_a = st.select_slider("Select Side A Base Depth", options=base_depth_a_options, value=base_depth_a_options[0])

    # Side B Base Depth with Slider using predefined options
    st.subheader("Side B Base Depth")
    selected_base_depth_b = st.select_slider("Select Side B Base Depth", options=base_depth_a_options, value=base_depth_a_options[0])

    # Upper Shelf Quantity with Slider using predefined options
    st.subheader("Upper Shelf Quantity")
    upper_shelf_qty = st.slider("Select Upper Shelf Quantity", min_value=0, max_value=6, step=1, value=0, format="%d")

    # Upper Shelf Type
    st.subheader("Upper Shelf Type")
    upper_shelf_type = st.radio("Select Upper Shelf Type", ["TL", "DL"], index=0, horizontal=True)

    # Upper Shelf Depth with Slider using predefined options
    st.subheader("Upper Shelf Depth")
    upper_shelf_depth_options = [7, 10, 13, 15, 16, 17, 19, 22, 25, 28, 31]
    selected_upper_shelf_depth = st.select_slider("Select Upper Shelf Depth", options=upper_shelf_depth_options, value=upper_shelf_depth_options[0])

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
