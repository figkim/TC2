class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        '''
        다른 사람의 풀이를 참고하여 설명을 추가합니다.
        
        BFS를 사용하여 탐색을 진행합니다.
        문자열을 앞부터 잘라서 문제 조건에 맞는지 판별하고, 맞으면 큐에 넣습니다
        이를 반복합니다.
        
        그리고 0으로 시작하는 숫자를 제거하기 위해서 0으로 시작하고, 길이가 2이상인 경우는 제외해줍니다
        '''
        queue = [([], S)]

        while queue:
            tmp, rest = queue.pop(0)

            if not rest and len(tmp) > 2:
                return tmp
            
            for i in range(1, len(rest)+1):
                if int(rest[:i]) > 2**31 - 1:
                    break
                    
                if rest[0] == '0' and i > 1:
                    continue

                if len(tmp) < 2:
                    queue.append((tmp + [int(rest[:i])], rest[i:]))
                else:
                    if tmp[-1] + tmp[-2] == int(rest[:i]):
                        queue.append((tmp + [int(rest[:i])], rest[i:]))
                        
        return []
