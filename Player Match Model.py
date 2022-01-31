import streamlit as st

from datetime import datetime, date
from functions import load_data, pace, read_markdown_file, filedownload, summary_stats
from charts import radar_chart, time_series, clustering
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg
from matplotlib.figure import Figure
import seaborn as sns
import statsmodels
from statsmodels.nonparametric.smoothers_lowess import lowess
import streamlit as st