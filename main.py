import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_gif(mp4_path, gif_path, fps=10):
    clip = VideoFileClip(mp4_path)
    clip.write_gif(gif_path, fps=fps)
    clip.close()

def main():
    current_dir = os.getcwd()
    mp4_files = [f for f in os.listdir(current_dir) if f.lower().endswith('.mp4')]

    if not mp4_files:
        print("MP4 파일이 없습니다.")
        return

    delete_input = input("원본 파일을 삭제하겠습니까? Y/N: ").strip().lower()

    for mp4_file in mp4_files:
        gif_file = os.path.splitext(mp4_file)[0] + '.gif'
        print(f"{mp4_file}를 {gif_file}로 변환 중...")
        convert_mp4_to_gif(mp4_file, gif_file)
        print(f"{mp4_file}를 {gif_file}로 변환했습니다.")

    if delete_input == 'y':
        for mp4_file in mp4_files:
            os.remove(mp4_file)
            print(f"{mp4_file}를 삭제했습니다.")
    else:
        print("원본 파일을 유지합니다.")

if __name__ == "__main__":
    main()
