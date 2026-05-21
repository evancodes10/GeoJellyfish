from dotenv import load_dotenv
import os

load_dotenv()

NOAA_HAB_BASE_URL = "https://gis.ngdc.noaa.gov/arcgis/rest/services/EnvironmentalMonitoring/HABSOSViewBase/MapServer/0/query"
INATURALIST_BASE_URL = "https://api.inaturalist.org/v1"
NOAA_TIDES_BASE_URL = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"