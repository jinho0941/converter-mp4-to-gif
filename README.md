- 해당 프로젝트는 온라인 변환기가 전부 유료 플렌에 갯수 제한이 있어서 무료로 gif로 변환시킬려고 만든 프로젝트 입니다.

https://github.com/ugaugaugaugaugauga/dragonball-poster-page

lang: python   
env: 3.8
```
pip install pillow==8.2.0
pip install moviepy==1.0.3
```


위 사이트의 readme를 작성하는 도중, 특성상 사전 녹화한 mp4 를 gif로 변환해야하는 작업이 많은데,   
이를 온라인에서 제공해주는 converter를 사용하는데 제한이 있어서 직접 converter를 만들어서 무료로 사용할려고 만든 프로젝트 입니다.

moviepy라는 라이브러리로 간단하게 구현하였으며, 주의사항은 moviepy는 2019년 이후로 업데이트를 안하여 레거시 에러가 발생합니다.   
해당 문제는 위에 알려준 명렁어로 설치하면 해결됩니다.

```
from moviepy.editor import VideoFileClip

def convert_mp4_to_gif(mp4_path, gif_path, fps=10):
    clip = VideoFileClip(mp4_path)
    clip.write_gif(gif_path, fps=fps)
    clip.close()
```


실행하는 폴더에 있는 mp4파일 전부를 gif로 바꾸어 줍니다.

![image](https://github.com/user-attachments/assets/b4449ba3-00e0-4aa4-b80f-b73da13fe00e)

위 이미지 처럼 시작 전에 원본파일 삭제 옵션 문구가 나옵니다.   
목적상 mp4파일은 필요없지만 필요할수도 있으니 옵션으로 넣었습니다. default는 N입니다.
```
if delete_input == 'y':
```
![image](https://github.com/user-attachments/assets/73fd38f3-e96c-4591-bcab-fe752524e0f7)

다음은 resize비율인데 default는 0.3입니다. 

### 11MB를 10FPS 0.3으로 만들면 3MB가 되지만 10FPS 1.0으로 만들면 88MB가 나오니 조심하셔야 합니다.

![image](https://github.com/user-attachments/assets/45893d17-e937-4019-a152-58c840f846c4)

![image](https://github.com/user-attachments/assets/db5a5d1d-942e-48c7-b693-6661a54df7cb)

이렇게 변환되면 gif파일이 만들어 지며,

기존에 있던 web에서 만든 gif랑 비교한 사진은 아래와 같습니다.
![image](https://github.com/user-attachments/assets/2b28d956-4f7a-48e4-9ff1-595f0849968c)

크기 차이가 안나고 용량도 별로 차이가 안나는것을 보니 비슷하게 만들은거 같습니다.

이제 해당 코드로 gif를 공짜로 만들어요 ^^
