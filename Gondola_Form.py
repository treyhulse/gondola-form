import streamlit as st

# Title of the application
st.title("Parts List Generator")

# Configuration Selection
st.subheader("Configuration")
configuration = st.radio("Select Configuration", ["Island/Gondola", "Wall"], index=0, horizontal=True)

# Height Selection
st.subheader("Height")
heights = [48, 54, 60, 66, 72, 78, 84, 90, 96]
selected_height = st.selectbox("Select Height", heights)

# Width Selection
st.subheader("Width")
widths = [2, 3, 4]
selected_width = st.selectbox("Select Width", widths)

# Color Selection
st.subheader("Color")
color = st.radio("Select Color", ["CHR", "PLT"], index=0, horizontal=True)

# Side A Back Panel Type
st.subheader("Side A Back Panel Type")
side_a_panel = st.radio("Select Side A Panel Type", ["P", "M"], index=0, horizontal=True)

# Side B Back Panel Type
st.subheader("Side B Back Panel Type")
side_b_panel = st.radio("Select Side B Panel Type", ["P", "M", "None"], index=0, horizontal=True)

# Side A Base Depth
st.subheader("Side A Base Depth")
base_depth_a_options = [13, 16, 19, 22, 25, 28, 31]
selected_base_depth_a = st.selectbox("Select Side A Base Depth", base_depth_a_options)

# Side B Base Depth
st.subheader("Side B Base Depth")
selected_base_depth_b = st.selectbox("Select Side B Base Depth", base_depth_a_options)

# Upper Shelf Quantity
st.subheader("Upper Shelf Quantity")
upper_shelf_qty = st.selectbox("Select Upper Shelf Quantity", [0, 1, 2, 3, 4, 5, 6])

# Upper Shelf Type
st.subheader("Upper Shelf Type")
upper_shelf_type = st.radio("Select Upper Shelf Type", ["TL", "DL"], index=0, horizontal=True)

# Upper Shelf Depth
st.subheader("Upper Shelf Depth")
upper_shelf_depth_options = [7, 10, 13, 15, 16, 17, 19, 22, 25, 28, 31]
selected_upper_shelf_depth = st.selectbox("Select Upper Shelf Depth", upper_shelf_depth_options)

# Base Height
st.subheader("Base Height")
base_height = st.radio("Select Base Height", ["LB", "06"], index=0, horizontal=True)

# Generate Parts List Button
if st.button("Generate Parts List"):
    # Placeholder for parts list generation
    st.success("Parts List Generated Successfully!")
