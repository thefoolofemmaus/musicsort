from mutagen.easyid3 import EasyID3
from pathlib import Path
import shutil

source_dir = Path("/media/drive/media/video/music/google music")
destination_dir = Path("/media/drive/media/video/music/google music/sorted")

for file in source_dir.rglob("*.mp3"):
    try:
        tags = EasyID3(file)
        artist = tags.get('artist', ['Unknown Artist'])[0]
        album = tags.get('album', ['Unknown Album'])[0]

        artist_folder = "".join(c for c in artist if c.isalnum() or c in " _-").strip()
        album_folder = "".join(c for c in album if c.isalnum() or c in " _-").strip()

        dest_path = destination_dir / artist_folder /album_folder
        dest_path.mkdir(parents=True, exist_ok=True)

        shutil.copy2(file, dest_path / file.name)
    except Exception as e:
        print(f"Skipping {file}: {e}")
