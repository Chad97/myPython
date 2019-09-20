import pygal.maps.world

wm = pygal.maps.world.World()

wm.title = '世界人口分布'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf','gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.add('Asia', ['cn'])
wm.render_to_file('americas.svg')
