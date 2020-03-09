# _*_ encoding:utf-8 _*_
from django.shortcuts import render

import json
from .models import smartpipe,pipedetail

from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import View

#############
from random import randrange

from rest_framework.views import APIView

# import simplejson as json
import numpy as np
import pandas as pd
from pandas import DataFrame
import pymysql

# from __future__ import unicode_literals
# from pyecharts import Line, Pie, Grid, configure

from pyecharts.charts import Bar,Line, Pie, Grid

from pyecharts import options as opts
# configure(output_image=True)
# from pyecharts import online
# online() # 使用远程 jshost



from pyecharts.components import Image
from pyecharts.options import ComponentTitleOpts

#############

from pandasql import sqldf
import time
from datetime import datetime
import datetime

from pyecharts.commons.utils import JsCode
from pyecharts.faker import Collector, Faker
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType,ThemeType
from pyecharts.charts import Bar, Grid, Line, Page, Pie, Geo,Liquid
import json
import os
from pyecharts.components import Table

from pyecharts import options as opts
from pyecharts.charts import Page, Tree

from pandas import DataFrame
import numpy as np
import pandas as pd
