#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path, getcwd
from collections import defaultdict
import os


config = defaultdict(defaultdict)

config["importer"] = "spatialite"

config["styles_dir"] = os.environ["STYLES_DIR"]

# The name given to the style. This is the name it will have in the TileMill
# project list, and a sanitized version will be used as the directory name
# in which the project is stored
config["name"] = { "styles/osm-bright": "OSM Bright",
                   "styles/osm-bright-en": "OSM Bright English",
                   "styles/osm-bright-car": "OSM Bright Car",
                   "styles/osm-bright-car-en": "OSM Bright Car English",
                   "styles/mc": "Midnight Commander",
                   "styles/mc-en": "Midnight Commander English",
                   "styles/mc-car": "Midnight Commander Car",
                   "styles/mc-car-en": "Midnight Commander Car English",
}

# The absolute path to your MapBox projects directory. You should 
# not need to change this unless you have configured TileMill specially
config["path"] = os.environ["INSTALL_DIR"]
if not os.path.exists(config["path"]):
    os.makedirs(config["path"])

# SQLite connection setup 
config["sqlite"]["metadata"] = "mapnik_metadata"
config["sqlite"]["file"] = os.path.join(os.environ["DB_DIR"], os.environ["DB_NAME"])
config["sqlite"]["initdb"] = "PRAGMA cache_size = -20480;" # SELECT load_extension('mod_spatialite');"
config["sqlite"]["geometry_field"] = "geometry"
config["sqlite"]["wkb_format"] = "generic"
config["sqlite"]["use_spatial_index"] = "true"
config["sqlite"]["type"] = "sqlite"

# Increase performance if you are only rendering a particular area by
# specifying a bounding box to restrict queries. Format is "XMIN,YMIN,XMAX,YMAX"
# in the same units as the database (probably spherical mercator meters). The
# whole world is "-20037508.34 -20037508.34 20037508.34 20037508.34".
# Leave blank to let Mapnik estimate.
#config["sqlite"]["extent"] = "-20037508.34,-20037508.34,20037508.34,20037508.34"

# Land shapefiles required for the style. If you have already downloaded
# these or wish to use different versions, specify their paths here.
# You will need to unzip these files before running make.py
# These OSM land shapefiles are updated daily and can be downloaded at: 
# - http://data.openstreetmapdata.com/simplified-land-polygons-complete-3857.zip
# - http://data.openstreetmapdata.com/land-polygons-split-3857.zip

config["land-high"] = os.path.join(os.environ["DB_DIR"], "land_polygons.shp")
config["land-low"] = os.path.join(os.environ["DB_DIR"], "simplified_land_polygons.shp")
