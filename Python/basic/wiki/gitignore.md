# gitignore 작성법

깃헙을 업데이트 하다보면, 불필요한 파일들이 업데이트 되어서 곤란하게 될 때가 많다. 그럴 때 사용하는 것이 `gitignore` 파일이다. `gitignore`를 설정해두면, 내가 원하는 폴더나 파일이 깃 업데이트 리스트에서 빠지게 되어 조금 더 편하게 깃 관리가 가능하다. 작성법은 구글에 gitignore 만 검색해도 잘 나오지만, 매번 찾기가 귀찮아 정리해 두기로 한다.

## 파일 위치

- 프로젝트 최상단에 위치해야 함

## 패턴

- ‘#’으로 시작되는 라인은 무시한다.
- 표준 Glob 패턴을 사용한다.
- 슬래시(/)로 시작하면, 하위 디렉토리에 적용되지 않는다.
- 디렉토리는 끝에 슬래시(/)를 사용하는 것으로 표현한다.
- 느낌표(!)로 시작하는 패턴의 파일은 무시하지 않는다.

```markup
# ignore all .class file
*.class

# exclude lib.class from "*.class", meaning all lib.class are still tracked
!lib.class

# ignore all json files whose name begin with 'temp-'
*temp-*.json

# only ignore the build.log file in current directory, 
# not those in its subdirectories
/build.log

# specify a folder with slash in the end
# ignore all files in any directory named temp
temp/

# ignore doc/notes.txt, but not doc/server/arch.txt
bin/*.txt

# ignore all .pdf files in the doc/ directory and any of its subdirectories
# /** matches 0 or more directories
doc/**/*.pdf
```