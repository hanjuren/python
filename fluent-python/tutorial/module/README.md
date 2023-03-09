### 모듈
파이썬에서 모듈이란 파이썬 코드로 이루어진 모든 파일을 의마한다.  
프로젝트내 .py 로 작성된 모든 파일이 모듈인 것이다. 이렇게 각각 파일에 작성된 클래스 혹은 메서드는 다른 파일이나 실행환경에서 import해서 사용할 수 있다.

모듈을 import 하는 방식
```python
import fibo

fibo.fib(3)

from fibo import fib, fib2

fib(3)
fib2(3)

import fibo as fib

fib.fib(3)
fib.fib2(3)
```