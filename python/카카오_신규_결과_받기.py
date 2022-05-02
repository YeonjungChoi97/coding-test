#link to the test: https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3


def solution(id_list, report, k):
    #remove any duplicate values in report list
    report = list(set(report))
    
    #create a dictionary for reported counter
    count_report = {}
    
    #loop through report to count the times that a user got reported
    for i in report:
        i = i.split(" ")
        count_report[i[1]] = count_report.get(i[1],0) + 1
    
    #sort by the value k
    final = {key:value for (key, value) in count_report.items() if value >= k}
    
    #create a dictionary so that we can count how many times reports are going to be sent to a user
    num_of_email = dict.fromkeys(id_list, 0)
    
    #loop through to count how many reports are sent!
    for i in report:
        i = i.split(" ")
        reporter = i[0]
        reportee = i[1]
        
        
        for key in final:
            if key == reportee:
                for j in id_list:
                    if j == reporter:
                        num_of_email[j] = num_of_email.get(j,0) + 1

    #voila! the answer was correct with given test time
    answer = list(num_of_email.values())

    return answer



