import geopy.distance

hainan_chengmai=[19.825509, 109.932679]
beijing_home=[39.890376, 116.458305]
Japan_home=[35.693241, 139.741142]
christchurch=[-43.529975, 172.594261]
USA_LA=[33.770227, -118.194221]

coords_1 = (hainan_chengmai[0],hainan_chengmai[1])
coords_2 = (christchurch[0],christchurch[1])
coords_3 = (Japan_home[0],Japan_home[1])
coords_4 = (beijing_home[0],beijing_home[1])

distance1=geopy.distance.vincenty({coords_1}, {coords_2}).kilometers
distance2=geopy.distance.vincenty({coords_3}, {coords_4}).kilometers
print (' the distance based on World Geodetic System \n '
       ' is: {:.2f}'
       .format (distance1) +' km')
print (' the distance based on World Geodetic System \n '
       ' is: {:.2f}'
       .format (distance2) +' km')
# example output
# the distance based on World Geodetic System
# between my home in china and nowcast is: 2096.51 km
