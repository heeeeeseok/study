from queue import PriorityQueue

def solution(k, n, reqs):
    available_time = [0 for _ in range(k + 1)]
    waiting_time = [0 for _ in range(k + 1)]
    worker_size = [1 for _ in range(k + 1)]
    time_table_per_type = [[] for _ in range(k + 1)]

    for start, time, req_type in reqs:
        # 타입 별로 시작 시각과 시간 저장
        time_table_per_type[req_type].append([start, time])

        if available_time[req_type] > start:
            waiting_time[req_type] += (available_time[req_type] - start)
            available_time[req_type] += time
        else:
            available_time[req_type] = start + time

    # 상담사 인원 수 만큼
    for _ in range(n - k):
        reduced_times = [0]
        for i in range(1, k + 1):
            reduced_waiting_time = 0
            worker_size[i] += 1

            pq = PriorityQueue()
            for start, time in time_table_per_type[i]:
                if pq.qsize() < worker_size[i]:
                    pq.put(start + time)
                else:
                    if start >= pq.queue[0]:
                        pq.get()
                        pq.put(start + time)
                    else:
                        reduced_waiting_time += (pq.queue[0] - start)
                        pq.put(pq.queue[0] + time)
                        pq.get()
            reduced_times.append(waiting_time[i] - reduced_waiting_time)
            worker_size[i] -= 1

        max_idx = reduced_times.index(max(reduced_times))
        worker_size[max_idx] += 1
        waiting_time[max_idx] -= reduced_times[max_idx]

    return sum(waiting_time[1:])
