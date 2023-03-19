import streamlit as st
from streamlit_ifc import ifc_viewer

ifc_file = st.file_uploader("Upload IFC file", type=["ifc", "ifczip"])
if ifc_file is not None:
    # Render the IFC model using IfcViewer
    ifc_viewer(ifc_file)
