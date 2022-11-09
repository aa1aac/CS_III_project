import os
from supabase import create_client, Client

url: str = 'https://xnxjedytmfutvwvycojq.supabase.co'
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhueGplZHl0bWZ1dHZ3dnljb2pxIiwicm9sZSI6ImFub24iLCJpYXQiOjE2Njc2OTY2OTgsImV4cCI6MTk4MzI3MjY5OH0.YYKFIfM8DHWdbW4HI_iS1ysCL0bsvKAN75dDwQNpnCk"
supabase: Client = create_client(url, key)

loginDetails = None
def signIn(username, password):
    global loginDetails
    try:
        loginDetails = supabase.auth.sign_in(email=username, password=password)
        return True
    except Error:
        print(Error)
        return False
    
def signUp(username, password):
    global loginDetails
    loginDetails = supabase.auth.sign_up(email=username, password=password)
    return True
    

def isPlaylistValid(name):
    playlistNames = supabase.table("playlist").select("playlistname").execute()
    for k,v in playlistNames:
        if k == "data":
            for i in v:
                if name == i["playlistname"]:
                    return True
        return False

def createPlaylist(name):
    newPlaylist = supabase.table("playlist").insert({"createdby": str(loginDetails.user.id), "playlistname": name}).execute()
    return True

def deletePlaylist(name):
    if isPlaylistValid(name):
        supabase.table("playlist").delete().eq("createdby",str(loginDetails.user.id)).eq("playlist",name).execute()
        return True
    return False

def addSong(songName, playListName):
    if isPlaylistValid(playListName):
        songsTable = supabase.table("playlist").select("songs").eq("createdby", str(loginDetails.user.id)).eq("playlistname", playListName).execute()
        for k,v in songsTable:
            if k == "data":
                for i in v:
                    i["songs"].append(songName)
                    supabase.table("playlist").update({"songs":i["songs"]}).eq("playlistname",playListName).eq("createdby", str(loginDetails.user.id)).execute()
                    return True
    return False


def deleteSong(songName, playListName):
    if isPlaylistValid(playListName):
        songsTable = supabase.table("playlist").select("songs").eq("createdby", str(loginDetails.user.id)).eq("playlistname", playListName).execute()
        for k,v in songsTable:
            if k == "data":
                for i in v:
                    if songName not in i["songs"]:
                        return "\nSong is not in specificied playlist"
                    i["songs"].remove(songName)
                    supabase.table("playlist").update({"songs":i["songs"]}).eq("playlistname",playListName).eq("createdby", str(loginDetails.user.id)).execute()
                    return True
    return False

def viewPlaylists():
    playlistList = supabase.table("playlist").select("playlistname").eq("createdby", str(loginDetails.user.id)).execute()
    for i in playlistList.data:
        print(i["playlistname"])
    return

def viewSongsPerPlaylist(playListName):
    songsList = supabase.table("playlist").select("songs").eq("createdby", str(loginDetails.user.id)).eq("playlistname", playListName).execute()
    for i in songsList.data:
        for j in i["songs"]:
            print(j)
        break
    return 


