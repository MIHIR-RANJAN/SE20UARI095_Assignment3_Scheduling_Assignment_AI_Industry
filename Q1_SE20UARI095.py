class Process:
    def _init_(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.turnaround_time = 0
        self.waiting_time = 0

def fcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.waiting_time = current_time - process.arrival_time
        process.turnaround_time = process.waiting_time + process.burst_time
        current_time += process.burst_time

def sjf(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.waiting_time = current_time - process.arrival_time
        process.turnaround_time = process.waiting_time + process.burst_time
        current_time += process.burst_time

def round_robin(processes, time_quantum):
    current_time = 0
    queue = []
    idx = 0
    while True:
        for process in processes:
            if process.arrival_time <= current_time and process.remaining_time > 0:
                queue.append(process)
        if not queue:
            break
        process = queue.pop(0)
        if process.remaining_time > time_quantum:
            process.remaining_time -= time_quantum
            current_time += time_quantum
            queue.append(process)
        else:
            current_time += process.remaining_time
            process.remaining_time = 0
            process.waiting_time = current_time - process.arrival_time - process.burst_time
            process.turnaround_time = process.waiting_time + process.burst_time

def priority_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, -x.priority))
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.waiting_time = current_time - process.arrival_time
        process.turnaround_time = process.waiting_time + process.burst_time
        current_time += process.burst_time

def calculate_average_times(processes):
    total_turnaround_time = sum(process.turnaround_time for process in processes)
    total_waiting_time = sum(process.waiting_time for process in processes)
    return total_turnaround_time / len(processes), total_waiting_time / len(processes)

if _name_ == "_main_":
    # Example processes
    processes = [
        Process(1, 0, 24, 3),
        Process(2, 4, 3, 1),
        Process(3, 5, 3, 4),
        Process(4, 6, 12, 2),
    ]

    time_quantum = 4

    print("FCFS:")
    fcfs(processes.copy())
    for process in processes:
        print(f"Process {process.pid}: Turnaround Time = {process.turnaround_time}, Waiting Time = {process.waiting_time}")
    fcfs_avg_turnaround, fcfs_avg_waiting = calculate_average_times(processes)
    print(f"Average Turnaround Time: {fcfs_avg_turnaround}")
    print(f"Average Waiting Time: {fcfs_avg_waiting}\n")

    print("SJF:")
   
    sjf(processes.copy())
    for process in processes:
        print(f"Process {process.pid}: Turnaround Time = {process.turnaround_time}, Waiting Time = {process.waiting_time}")
    sjf_avg_turnaround, sjf_avg_waiting = calculate_average_times(processes)
    print(f"Average Turnaround Time: {sjf_avg_turnaround}")
    print(f"Average Waiting Time: {sjf_avg_waiting}\n")

    print(f"Round Robin (Time Quantum={time_quantum}):")
    round_robin(processes.copy(), time_quantum)
    for process in processes:
        print(f"Process {process.pid}: Turnaround Time = {process.turnaround_time}, Waiting Time = {process.waiting_time}")
    rr_avg_turnaround, rr_avg_waiting = calculate_average_times(processes)
    print(f"Average Turnaround Time: {rr_avg_turnaround}")
    print(f"Average Waiting Time: {rr_avg_waiting}\n")

    print("Priority Scheduling:")
    
    priority_scheduling(processes.copy())
    for process in processes:
        print(f"Process {process.pid}: Turnaround Time = {process.turnaround_time}, Waiting Time = {process.waiting_time}")
    priority_avg_turnaround, priority_avg_waiting = calculate_average_times(processes)
    print(f"Average Turnaround Time: {priority_avg_turnaround}")
    print(f"Average Waiting Time: {priority_avg_waiting}\n")

    # Determine which algorithm is most effective based on average turnaround time
    min_avg_turnaround = min(fcfs_avg_turnaround, sjf_avg_turnaround, rr_avg_turnaround, priority_avg_turnaround)
    if min_avg_turnaround == fcfs_avg_turnaround:
        print("FCFS is the most effective algorithm.")
    elif min_avg_turnaround == sjf_avg_turnaround:
        print("SJF is the most effective algorithm.")
    elif min_avg_turnaround == rr_avg_turnaround:
        print("Round Robin is the most effective algorithm.")
    else:
        print("Priority Scheduling is the most effective algorithm.")