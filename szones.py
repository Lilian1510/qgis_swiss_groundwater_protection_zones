# Create vector layers from WFS source

cadastre_uri = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:2056' typename='ms:RESF' url='https://geodienste.ch/db/av_0/fra' version='auto'"
surfaces_uri = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:2056' typename='ms:SOSF' url='https://geodienste.ch/db/av_0/fra' version='auto'"
lignes_uri = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:2056' typename='ms:SOLI' url='https://geodienste.ch/db/av_0/fra' version='auto'"
points_uri = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:2056' typename='ms:SOPT' url='https://geodienste.ch/db/av_0/fra' version='auto'"

cadastre_wfs = QgsVectorLayer(cadastre_uri, "Cadastre", "WFS")
surfaces_wfs = QgsVectorLayer(surfaces_uri, "Surfaces", "WFS")
lignes_wfs = QgsVectorLayer(lignes_uri, "Lignes", "WFS")
points_wfs = QgsVectorLayer(points_uri, "Points", "WFS")

# Style the layers
cadastre = QgsFillSymbol.createSimple({'color': '0,0,0,0'})
cadastre_wfs.renderer().setSymbol(cadastre)
surfaces = QgsFillSymbol.createSimple({'color': '0,0,0,255'})
surfaces_wfs.renderer().setSymbol(surfaces)
lignes = QgsLineSymbol.createSimple({'color': '0,0,0,255'})
lignes_wfs.renderer().setSymbol(lignes)
points = QgsMarkerSymbol.createSimple({'color': '0,0,0,255'})
points.setSize(1)
points_wfs.renderer().setSymbol(points)

# Add them to a group
root = QgsProject.instance().layerTreeRoot()
mensuration_group = root.addGroup("Mensuration officielle")
mensuration_list = [cadastre_wfs, surfaces_wfs , lignes_wfs, points_wfs]

for layer in mensuration_list:
    QgsProject.instance().addMapLayer(layer, False)
    mensuration_group.insertChildNode(1, QgsLayerTreeLayer(layer))


# Create vector layers from WFS source

ao_uri = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:2056' typename='ms:gewaesserschutzbereich_ao' url='https://geodienste.ch/db/planerischer_gewaesserschutz_v1_1_1' version='auto'"
au_uri = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:2056' typename='ms:gewaesserschutzbereich_au' url='https://geodienste.ch/db/planerischer_gewaesserschutz_v1_1_1' version='auto'"

zo_uri = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:2056' typename='ms:zustroembereich_zo' url='https://geodienste.ch/db/planerischer_gewaesserschutz_v1_1_1' version='auto'"
zu_uri = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:2056' typename='ms:zustroembereich_zu' url='https://geodienste.ch/db/planerischer_gewaesserschutz_v1_1_1' version='auto'"
zu_replace_uri = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:2056' typename='ms:zustroembereich_zu_anstelle_einer_s3_oder_sm_in_kraft' url='https://geodienste.ch/db/planerischer_gewaesserschutz_v1_1_1' version='auto'"

s3_uri = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:2056' typename='ms:grundwasserschutzzone_s3_in_kraft' url='https://geodienste.ch/db/planerischer_gewaesserschutz_v1_1_1' version='auto'"
s2_uri = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:2056' typename='ms:grundwasserschutzzone_s2_in_kraft' url='https://geodienste.ch/db/planerischer_gewaesserschutz_v1_1_1' version='auto'"
s1_uri = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:2056' typename='ms:grundwasserschutzzone_s1_in_kraft' url='https://geodienste.ch/db/planerischer_gewaesserschutz_v1_1_1' version='auto'"
s3_not_uri = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:2056' typename='ms:grundwasserschutzzone_s3_nicht_in_kraft' url='https://geodienste.ch/db/planerischer_gewaesserschutz_v1_1_1' version='auto'"
s2_not_uri = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:2056' typename='ms:grundwasserschutzzone_s2_nicht_in_kraft' url='https://geodienste.ch/db/planerischer_gewaesserschutz_v1_1_1' version='auto'"
s1_not_uri = "pagingEnabled='true' preferCoordinatesForWfsT11='false' restrictToRequestBBOX='1' srsname='EPSG:2056' typename='ms:grundwasserschutzzone_s1_nicht_in_kraft' url='https://geodienste.ch/db/planerischer_gewaesserschutz_v1_1_1' version='auto'"

au_wfs = QgsVectorLayer(au_uri, "Au", "WFS")
ao_wfs = QgsVectorLayer(ao_uri, "Ao", "WFS")

zu_wfs = QgsVectorLayer(zu_uri, "Zu", "WFS")
zu_replace_wfs = QgsVectorLayer(zu_replace_uri, "Zu à la place de S3 ou S2", "WFS")
zo_wfs = QgsVectorLayer(zo_uri, "Zo", "WFS")

s3_wfs = QgsVectorLayer(s3_uri, "S3", "WFS")
s2_wfs = QgsVectorLayer(s3_uri, "S2", "WFS")
s1_wfs = QgsVectorLayer(s1_uri, "S1", "WFS")
s3_not_wfs = QgsVectorLayer(s3_not_uri, "S3 non en vigeur", "WFS")
s2_not_wfs = QgsVectorLayer(s2_not_uri, "S2 non en vigeur", "WFS")
s1_not_wfs = QgsVectorLayer(s1_not_uri, "S1 non en vigeur", "WFS")

# Style the layers
au = QgsFillSymbol.createSimple({'color': '219,39,51,90', 'outline_color': '0,0,0,0'})
au_wfs.renderer().setSymbol(au)
ao = QgsFillSymbol.createSimple({'color': '219,39,51,90', 'outline_color': '100,0,0,0'})
ao_wfs.renderer().setSymbol(ao)

zu = QgsFillSymbol.createSimple({'color': '0,0,0,0', 'outline_color': '133,199,231,110'})
zu_wfs.renderer().setSymbol(zu)
zu_replace = QgsFillSymbol.createSimple({'color': '0,0,0,0', 'outline_color': '133,199,231,110'})
zu_replace_wfs.renderer().setSymbol(zu_replace)
zo = QgsFillSymbol.createSimple({'color': '0,0,0,0', 'outline_color': '133,199,231,110'})
zo_wfs.renderer().setSymbol(zo)

s3 = QgsFillSymbol.createSimple({'color': '133,199,231,110', 'outline_color': '0,0,0,0'})
s3_wfs.renderer().setSymbol(s3)
s3_not = QgsFillSymbol.createSimple({'color': '133,199,231,90', 'outline_color': '0,0,0,0'})
s3_not_wfs.renderer().setSymbol(s3_not)
s2 = QgsFillSymbol.createSimple({'color': '84,137,229,110', 'outline_color': '0,0,0,0'})
s2_wfs.renderer().setSymbol(s2)
s2_not = QgsFillSymbol.createSimple({'color': '84,137,229,90', 'outline_color': '0,0,0,0'})
s2_not_wfs.renderer().setSymbol(s2_not)
s1 = QgsFillSymbol.createSimple({'color': '22,80,255,110', 'outline_color': '0,0,0,0'})
s1_wfs.renderer().setSymbol(s1)
s1_not = QgsFillSymbol.createSimple({'color': '22,80,255,110', 'outline_color': '0,0,0,0'})
s1_not_wfs.renderer().setSymbol(s1_not)

# Add them to a group
water_group = root.addGroup("Protection des eaux")
water_list = [au_wfs, ao_wfs, zu_wfs, zu_replace_wfs, zo_wfs, s3_wfs, s3_not_wfs, s2_wfs, s2_not_wfs, s1_wfs, s1_not_wfs]

for layer in water_list:
    QgsProject.instance().addMapLayer(layer, False)
    water_group.insertChildNode(1, QgsLayerTreeLayer(layer))


# Imagery layer from Google Satellite Services
imagery_url = "type=xyz&url=https://www.google.cn/maps/vt?lyrs%3Ds@189%26gl%3Dcn%26x%3D%7Bx%7D%26y%3D%7By%7D%26z%3D%7Bz%7D&zmax=18&zmin=0"
imagery_google = QgsRasterLayer(imagery_url, "Google Satellite Imagery", "wms")
QgsProject.instance().addMapLayer(imagery_google)