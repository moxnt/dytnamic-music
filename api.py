from ytmusicapi import YTMusic
ytmusic = YTMusic("browser.json")
playlistId = ytmusic.create_playlist("Something new", "JPMO")
search_results = ytmusic.search("Let it happen tame impala")
ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])
