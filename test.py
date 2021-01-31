from parse import parse


mystring = '/html-default/avl_location.asp?current_route=1-1&message=2 MINS AHEAD&vehicle=1628&time=2:16 PM&ptime=2:16 PM&waypoint=EMPIRE AVE OPP KELLYS BROOK APT&latlon=47.558033,-52.737786&heading=ENE'

parse_data = '/html-default/avl_location.asp?{}&{}&{}&{}&p{}&{}&{}&{}'

route_info = parse(parse_data, mystring)

# print(route_info)

array = []
my_dict = {}
for info in route_info:

    new_info = info.split('=')
    my_dict[new_info[0]] = new_info[1]

array.append({my_dict.get('current_route'): my_dict})

print(array)
