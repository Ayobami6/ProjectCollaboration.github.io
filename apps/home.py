import streamlit as st
import pandas as pd
import base64
import datetime
import time


def app():
       # Adding Nav Bar
       st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">',
            unsafe_allow_html=True)
      st.markdown("""
      <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #291720;">
        <a class="navbar-brand" href="https://bit.ly/pinkdatahub" target="_blank">Pink Data Hub</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
          <div class="collapse navbar-collapse" id="navbarNav">
           <ul class="navbar-nav">
             <li class="nav-item active">
               <a class="nav-link disabled" href="#">Home<span class="sr-only">(curent)</span></a>
             </li>
             <li class="nav-item">
               <a class="nav-link" href="https://github.com/Ayobami6/ProjectCollaboration.github.io" target="_blank">GitHub</a>
             </li>
             <li class="nav-item">
               <a class="nav-link" href="https://github.com/Ayobami6" target="_blank">Ayobami's Page</a>
             </li>
             <li class="nav-item">
               <a class="nav-link" href="https://github.com/Designegycreatives" target="_blank">Designegy Creatives's Page</a>
             </li>
           </ul>
          </div>
      </nav>
      """, unsafe_allow_html=True)



