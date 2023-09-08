# 한 개의 회의실이 있다. 각 회의에 대해 시작 시간과 끝나는 시간이 주어져있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라
# 단, 회의는 한 번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.

# [{'idx': 2, 'start': 5, 'end': 6}, {'idx': 5, 'start': 8, 'end': 14}, {'idx': 4, 'start': 14, 'end': 17}]

def schedule_meeting(meetings):
    for i in range(len(meetings)):
        for j in range(i+1,len(meetings)):
            if meetings[i]['end'] > meetings[j]['end']:
                meetings[i], meetings[j] = meetings[j], meetings[i]
                
    fastest_end = meetings[0]
    res = [meetings[0]]     
    for meeting in meetings[1:]:
        if fastest_end['end'] <= meeting['start']:
            res.append(meeting)
            fastest_end = meeting
            
    return res

''''강사님 풀이
def schedule_meeting(meetings):
    res=[]
    sorted_meetings = sorted(meetings, key=lambda e:e['end'])
    res.append(sorted_meetings[0])
    
    for e in sorted_meetings[1:]:
        if res[-1]['end'] <= e['start']
            res.append(e)
            
    return res
'''

meetings = [
    {'idx':1,'start':1, 'end':10},
    {'idx':2,'start':5, 'end':6},
    {'idx':3,'start':13,'end':15},
    {'idx':4,'start':14,'end':17},
    {'idx':5,'start':8, 'end':14},
    {'idx':6,'start':3, 'end':12}
]

print(schedule_meeting(meetings))