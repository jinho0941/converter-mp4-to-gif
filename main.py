import os
from moviepy.editor import VideoFileClip


def convert_mp4_to_gif(mp4_path, gif_path, fps=10, resize_factor=0.2):
    clip = VideoFileClip(mp4_path)

    # Resize the clip
    resized_clip = clip.resize(resize_factor)

    # Write the resized clip as a GIF
    resized_clip.write_gif(gif_path, fps=fps)

    # Close both clips
    clip.close()
    resized_clip.close()


def main():
    current_dir = os.getcwd()
    mp4_files = [f for f in os.listdir(current_dir) if f.lower().endswith('.mp4')]

    if not mp4_files:
        print("MP4 파일이 없습니다.")
        return

    delete_input = input("원본 파일을 삭제하겠습니까? Y/N: ").strip().lower()
    resize_factor = input("리사이즈 비율을 입력하세요 (예: 0.5): ").strip()
    if not resize_factor:
        resize_factor = 0.2
    else:
        float(resize_factor)

    for mp4_file in mp4_files:
        gif_file = os.path.splitext(mp4_file)[0] + '.gif'
        print(f"{mp4_file}를 {gif_file}로 변환 중...")
        convert_mp4_to_gif(mp4_file, gif_file, resize_factor=resize_factor)
        print(f"{mp4_file}를 {gif_file}로 변환했습니다.")

    if delete_input == 'y':
        for mp4_file in mp4_files:
            os.remove(mp4_file)
            print(f"{mp4_file}를 삭제했습니다.")
    else:
        print("원본 파일을 유지합니다.")


if __name__ == "__main__":
    main()