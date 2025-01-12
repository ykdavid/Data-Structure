from os import walk, listdir, makedirs
from os.path import join, isfile, isdir, dirname
import shutil
import os

from hashtable import Hashtable, KeyValuePair


class Track:
    """
    A Track represents an audio file, with a name (including the extension, such as "01 Track.m4p") and a
    filename that includes a relative path to the file.
    """
    def __init__(self, name, path):
        self.name = name
        """The track name from the file, something like '04 Okay.m4p'"""
        self.file_with_path = path
        """The file path to the audio file for this track """

    def copy_track_to_new_directory(self, new_dir, prefix=''):
        """
        Copy the track audio file to the specified new location, with the specified prefix
        :param new_dir: The directory to write to
        :param prefix: A prefix (defaults to '') to write before the track name
        :return: Nothing, but writes a new file "<new_dir>/<prefix><track.name>"
        """
        makedirs(new_dir,exist_ok=True)
        new_file_path=join(new_dir,f"{prefix}{self.name}")
        shutil.copy(self.file_with_path,new_file_path)


class Album:
    """
    An album that has an Artist, AlbumName, ReleaseDate, and a set of Tracks.
    """
    def __init__(self, artist: str = '', release_date: str = '', album_name: str = '', tracks: [Track] = []):
        """
        Instantiates an Album.
        :param artist: The Artist
        :param release_date: The release date, "YYYY-MM" format
        :param album_name: The name of the album
        :param tracks: A list of Tracks on the album
        """
        self.artist = artist
        '''The Artist who produced this album'''
        self.release_date = release_date
        '''The Year/Month of the release of this album; YYYY-MM'''
        self.album_name = album_name
        '''Name of the Album'''
        self.tracks = tracks
        '''A list of the tracks on this album'''

    def __repr__(self):
        return f'"{self.album_name}" by ~{self.artist}~ released on [{self.release_date}]'

    def write_to_new_dir(self, new_dir):
        """
        Writes all the tracks for this album to the new specified directory.
        Writes all tracks to the new directory with the format "<release_date>_<artist>_<album_name>_<track_name>"
        :param new_dir: The new directory to write this albums tracks to.
        :return: None
        """
        prefix = f"{self.release_date}_{self.artist}_{self.album_name}_"
        for track in self.tracks:
            track.copy_track_to_new_directory(new_dir, prefix)



class MusicIndex(Hashtable):
    """
    A data structure that stores Albums efficiently, keyed by the release date.
    A MusicIndex extends a Hashtable, with a KVP where the Key is the ReleaseDate
    and the value is a list of Albums.
    """
    def __init__(self):
        super().__init__()

    def add_album(self, album: Album):
        """
        Adds an album to this MusicIndex, keyed by release_date.
        :param album: An album to put into the MusicIndex
        :return:
        """
        ## If there are already albums stored with the same release date as the new album,
        ##   get that list of albums
        ## Add this new album to the list
        ## Otherwise, put this album into a new list and store in the index.
        ## Hint: Be sure to use your Hashtable.get() and Hashtable.put() functions!
        # 找到目標 bucket
        if self.key_exists(album.release_date):
            albums = self.get(album.release_date)
            albums.append(album)
            self.put(album.release_date, albums)
            self.num_elements -= 1
        else:
            self.put(album.release_date, [album])
        '''
        target_bucket = hash(album.release_date) % self.num_buckets
        bucket = self.buckets[target_bucket]
        
        # 檢查該鍵是否已存在於 bucket 中
        for kvp in bucket:
            if kvp.key == album.release_date:
                # 如果找到相同的鍵，追加新值到現有列表
                kvp.value.append(album)
                return
        # 如果鍵不存在，新增一個 KeyValuePair 並用列表存儲值
        bucket.append(KeyValuePair(album.release_date, [album]))
        self.num_elements += 1  # 增加元素計數
    
        # 檢查是否需要調整大小
        if self.load_factor() >= self.alpha:
            self.resize()
        '''

    def get_albums(self, release_date: str) -> [Album]:
        """
        Returns all the albums with the specified release_date
        :param release_date: A release date of form "YYYY-MM"
        :return:
        """
        ## Return the list of albums released on the provided release date
        ## Input should be of the form YYYY-MM
        try:
            '''
            target_bucket = hash(release_date) % self.num_buckets
            bucket = self.buckets[target_bucket]

            # 收集 bucket 中所有符合鍵的值
            # 收集 bucket 中所有符合鍵的值並轉換為物件
            objects = []
            for kvp in bucket:
                if kvp.key == release_date:
                    return kvp.value
            return objects
            '''
            if self.key_exists(release_date):
                return self.get(release_date)
            else:
                return []
        except KeyError:
            return []
        
        

    def print(self):
        """
        Helper function to printout all the albums stored in this MusicIndex.
        :return:
        """
        for index, item in enumerate(self):
            print(f"Key: {item.key}")
            music_set = item.value
            music_set.print()

    def write_playlist(self, base_dir, start_date: str = "1900-01", end_date: str = "2025-01"):
        """
        Write out a playlist to a specified location. The playlist will be written to a folder
        of the format "Music {start_date} through {end_date}" in the base_dir folder.
        :param base_dir: Where the new playlist folder should be created
        :param start_date: The start date (inclusive) of albums to write, in YYYY-MM format
        :param end_date: The end date (inclusive) of albums to write, in YYYY-MM format
        :return:
        """
        playlist_dir = join(base_dir,f"Music {start_date} through {end_date}")
        makedirs(playlist_dir,exist_ok=True)
        for item in self:
            release_date=item.key
            if start_date <= release_date <= end_date:
                for album in item.value:
                    album.write_to_new_dir(playlist_dir)


def get_release_date_from_file(fileptr):
    """
    Given an open file pointer, read the first line and return it.
    :param fileptr: A fileptr to the open file (details.txt) that has the release date for an album.
    :return: The first line of the file, which should be the release date in YYYY-MM format.
    """
    try:

        line = fileptr.readline().strip()
        if not line:
            raise ValueError("The details.txt file is empty or contains no release date.")
        

        if len(line) != 7 or line[4] != '-' or not line[:4].isdigit() or not line[5:].isdigit():
            raise ValueError(f"Invalid release date format: {line}")
        
        return line
    except Exception as e:
        raise ValueError(f"Error reading release date from file: {e}")



def get_release_date(artist, album, music_library_folder='') -> str:
    """
    Gets the release date for a given artist and album.
    This is primarily a wrapper function: by using this function rather than the
    "get_release_date_from_file" function directly, this function can choose to query
    Spotify rather than read the file.
    :param artist: The artist who released the album
    :param album: The album name
    :param music_library_folder: The folder that holds the library/files-- defaults to ''
    :return: The release date for this album, in YYYY-MM format.
    """
    ## For the core implementation, this function should open a file to the relevant
    ##`details.txt' file for the release date.
    ## If you are doing the Spotify option this function should query Spotify (probably with
    ## some helper functions)
    
    album_folder = join(music_library_folder, album)  # 正確拼接 album 文件夾
    details_file = join(album_folder, "details.txt")

    # 檢查 details.txt 是否存在
    if not isfile(details_file):
        raise FileNotFoundError(f"Expected details file not found: {details_file}")

    # 讀取 details.txt 的第一行作為 release date
    with open(details_file, 'r') as f:
        return f.readline().strip()


def get_album_from_folder(album_name, album_folder, artist) -> Album:
    """
    Creates and returns an Album from the specified parameters.
    :param album_name: The album name
    :param album_folder: The folder holding all the album track files
    :param artist: The artist who released this album
    :return: An Album containing all the Tracks
    """
    release_date = get_release_date(artist, album_name, album_folder)
    tracks = [
        Track(name=track, path=join(album_folder, track))
        for track in listdir(album_folder)
        if isfile(join(album_folder, track)) and track != "details.txt"
    ]
    return Album(artist=artist, release_date=release_date, album_name=album_name, tracks=tracks)
    '''
    details_file = join(album_folder, "details.txt")
    if not os.path.isfile(details_file):
        return Album(artist=artist, release_date='', album_name=album_name, tracks=[])
    
    with open(join(album_folder,"details.txt"),'r') as f:
        release_date = get_release_date_from_file(f).strip()
    tracks=[
        Track(name=track,path=join(album_folder,track))
        for track in listdir(album_folder)
        if isfile(join(album_folder,track)) and track != "details.txt"
    ]
    return Album(artist=artist, release_date=release_date, album_name=album_name, tracks=tracks)
    '''
    
def get_albums_for_artist(artist, artist_folder) -> [Album]:
    """
    Returns all the albums for a given artist with data in the given artist_folder
    :param artist: The Artist to load Albums for
    :param artist_folder: The folder where the artist's album live
    :return: A list of Albums
    """
    albums = []

    try:
        # 遍歷 artist_folder 下的所有專輯文件夾
        for album_name in listdir(artist_folder):
            album_folder = join(artist_folder, album_name)
            
            # 檢查是否為有效的專輯文件夾
            if isdir(album_folder):
                try:
                    # 嘗試從文件夾中加載專輯
                    album = get_album_from_folder(album_name, album_folder, artist)
                    albums.append(album)
                except FileNotFoundError as e:
                    # 專輯缺少 details.txt 或其他問題，忽略這個文件夾
                    print(f"Warning: Could not load album from {album_folder}: {e}")
                except Exception as e:
                    # 捕捉其他潛在問題
                    print(f"Error: Unexpected issue with {album_folder}: {e}")
    except FileNotFoundError as e:
        print(f"Error: Artist folder not found: {artist_folder}")
    except Exception as e:
        print(f"Error: Unexpected issue with artist folder {artist_folder}: {e}")

    return albums



def get_albums(starting_dir: str) -> [Album]:
    """
    Creates albums from the specified starting location. Assumes that
    the files and folders are as specified in the "MyMusic" example ("MyMusic" is starting_dir,
    which holds Artists; each Artist dir holders Albums; each Album dir holds "details.txt" and track files).
    :param starting_dir: The directory where all the Artist/Album/Track files are stored.
    :return: A list of Albums
    """
    '''
    albums = []
    for artist in listdir(starting_dir):
        artist_folder = join(starting_dir, artist)
        if isdir(artist_folder):
            for album_name in listdir(artist_folder):
                album_folder = join(artist_folder, album_name)
                if isdir(album_folder):
                    albums.append(get_album_from_folder(album_name, album_folder, artist))
    return albums
    '''
    albums = []
    for artist in listdir(starting_dir):
        artist_folder = join(starting_dir, artist)
        if isdir(artist_folder):
            albums.extend(get_albums_for_artist(artist, artist_folder))
    return albums


def create_index(music_library_dir: str) -> MusicIndex:
    """
    Starts in the directory that holds the Music Library and returns a
    MusicIndex, populated with all the albums in that library.
    :param music_library_dir: The folder that holds the music files (Artist/Album/Track)
    :return: A MusicIndex with all the albums from the Music Library directory
    """
    music_index = MusicIndex()
    albums = get_albums(music_library_dir)
    for album in albums:
        music_index.add_album(album)
    return music_index


## Examples of how this might be called
# music_index = create_index('MyMusic')
# music_index.write_playlist("MyPlaylists", "2004-01", "2004-12")
# music_index.write_playlist("MyPlaylists")

from unittest.mock import patch

if __name__ == "__main__":
        '''
        test_music_index = MusicIndex()
        album1 = Album()
        album1.artist = "Some Artist"
        album1.release_date = "2021-03"
        album1.album_name = "Album1"

        album2 = Album()
        album2.artist = "Artist2"
        album2.release_date = "2021-03"
        album2.album_name = "AlbumByArtist2"

        test_music_index.add_album(album1)
        test_music_index.add_album(album2)

        #assert test_music_index.num_elements == 1

        album_list = test_music_index.get_albums("2021-03")

        assert album_list is not None
        assert len(album_list) == 2
        for album in album_list:
            assert album.release_date == "2021-03"
        '''
        music_library_dir = input("Input the path to your Music Library directory: ")
        start_date = input("Input the start date in YYYY-MM format: ")
        end_date = input("Input the end date in YYYY-MM format: ")
        output_dir = input("Input the directory to create the playlist: ")

        index = create_index(music_library_dir)
        index.write_playlist(output_dir, start_date, end_date)
        print(f"Playlist Output Path: {output_dir}")