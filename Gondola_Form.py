import streamlit as st

# Set up the layout with two equal columns
col1, col2 = st.columns([1, 1])

# Define image paths relative to the project directory
default_image = "./images/LogoWhite.png"
changed_image = "./images/LogoRed.png"

# Initialize session state to track changes and set default image
if "image_displayed" not in st.session_state:
    st.session_state.image_displayed = default_image

# Function to update image when any change occurs
def update_image():
    st.session_state.image_displayed = changed_image

# Left Column: Form (takes up 50% of the screen width)
with col1:
    st.title("Parts List Generator")

    # Configuration Selection
    st.subheader("Configuration")
    configuration = st.radio(
        "Select Configuration", ["Island/Gondola", "Wall"], index=0, horizontal=True, on_change=update_image
    )

    # Height Selection with Slider
    st.subheader("Height")
    selected_height = st.slider(
        "Select Height", min_value=48, max_value=96, step=6, value=48, on_change=update_image
    )

    # Width Selection with Slider
    st.subheader("Width")
    selected_width = st.slider(
        "Select Width", min_value=2, max_value=4, step=1, value=2, on_change=update_image
    )

    # Color Selection
    st.subheader("Color")
    color = st.radio(
        "Select Color", ["CHR", "PLT"], index=0, horizontal=True, on_change=update_image
    )

    # Side A Back Panel Type
    st.subheader("Side A Back Panel Type")
    side_a_panel = st.radio(
        "Select Side A Panel Type", ["P", "M"], index=0, horizontal=True, on_change=update_image
    )

    # Side B Back Panel Type
    st.subheader("Side B Back Panel Type")
    side_b_panel = st.radio(
        "Select Side B Panel Type", ["P", "M", "None"], index=0, horizontal=True, on_change=update_image
    )

    # Side A Base Depth with Slider using predefined options
    st.subheader("Side A Base Depth")
    base_depth_a_options = [13, 16, 19, 22, 25, 28, 31]
    selected_base_depth_a = st.select_slider(
        "Select Side A Base Depth", options=base_depth_a_options, value=base_depth_a_options[0], on_change=update_image
    )

    # Side B Base Depth with Slider using predefined options
    st.subheader("Side B Base Depth")
    selected_base_depth_b = st.select_slider(
        "Select Side B Base Depth", options=base_depth_a_options, value=base_depth_a_options[0], on_change=update_image
    )

    # Upper Shelf Quantity with Slider using predefined options
    st.subheader("Upper Shelf Quantity")
    upper_shelf_qty = st.slider(
        "Select Upper Shelf Quantity", min_value=0, max_value=6, step=1, value=0, on_change=update_image
    )

    # Upper Shelf Type
    st.subheader("Upper Shelf Type")
    upper_shelf_type = st.radio(
        "Select Upper Shelf Type", ["TL", "DL"], index=0, horizontal=True, on_change=update_image
    )

    # Upper Shelf Depth with Slider using predefined options
    st.subheader("Upper Shelf Depth")
    upper_shelf_depth_options = [7, 10, 13, 15, 16, 17, 19, 22, 25, 28, 31]
    selected_upper_shelf_depth = st.select_slider(
        "Select Upper Shelf Depth", options=upper_shelf_depth_options, value=upper_shelf_depth_options[0], on_change=update_image
    )

    # Base Height
    st.subheader("Base Height")
    base_height = st.radio(
        "Select Base Height", ["LB", "06"], index=0, horizontal=True, on_change=update_image
    )

    # Generate Parts List Button
    if st.button("Generate Parts List"):
        st.success("Parts List Generated Successfully!")

# Right Column: Display Image
with col2:
    st.subheader("Configuration Preview")

    # Display the image based on the session state
    st.image(st.session_state.image_displayed, caption="Configuration Image", use_column_width=True)
