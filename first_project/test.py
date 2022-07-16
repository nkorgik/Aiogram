import pprint

arr_photos = ["https://travel.home.sndimg.com/content/dam/images/travel/fullset/2015/08/03/america-the-beautiful-ss/adirondack-park-new-york-state.jpg.rend.hgtvcom.616.462.suffix/1491580836599.jpeg",
              "https://i.ytimg.com/vi/u71QsZvObHs/maxresdefault.jpg",
              "https://images.unsplash.com/photo-1613967193490-1d17b930c1a1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8YmVhdXRpZnVsJTIwbGFuZHNjYXBlfGVufDB8fDB8fA%3D%3D&w=1000&q=80"]

photos = dict(zip(arr_photos, ['1', '2', '3']))

pprint.pprint(photos)
print(photos.keys())
