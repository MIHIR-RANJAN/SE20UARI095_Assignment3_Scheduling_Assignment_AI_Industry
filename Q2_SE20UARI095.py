class Patient:
    def _init_(self, name, arrival_time, estimated_time, urgency_level):
        self.name = name
        self.arrival_time = arrival_time
        self.estimated_time = estimated_time
        self.urgency_level = urgency_level
        self.start_time = 0  # Added for turnaround time calculation

def fcfs_scheduling(patients):
    patients.sort(key=lambda x: x.arrival_time)
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    for patient in patients:
        if current_time < patient.arrival_time:
            current_time = patient.arrival_time
        patient.start_time = current_time
        waiting_time = current_time - patient.arrival_time
        total_waiting_time += waiting_time
        current_time += patient.estimated_time
        turnaround_time = current_time - patient.arrival_time
        total_turnaround_time += turnaround_time

    average_waiting_time = total_waiting_time / len(patients)
    average_turnaround_time = total_turnaround_time / len(patients)
    return average_waiting_time, average_turnaround_time

def sjf_scheduling(patients):
    patients.sort(key=lambda x: (x.arrival_time, x.estimated_time))
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    for patient in patients:
        if current_time < patient.arrival_time:
            current_time = patient.arrival_time
        patient.start_time = current_time
        waiting_time = current_time - patient.arrival_time
        total_waiting_time += waiting_time
        current_time += patient.estimated_time
        turnaround_time = current_time - patient.arrival_time
        total_turnaround_time += turnaround_time

    average_waiting_time = total_waiting_time / len(patients)
    average_turnaround_time = total_turnaround_time / len(patients)
    return average_waiting_time, average_turnaround_time

def ps_scheduling(patients):
    patients.sort(key=lambda x: (-x.urgency_level, x.arrival_time))
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    for patient in patients:
        if current_time < patient.arrival_time:
            current_time = patient.arrival_time
        patient.start_time = current_time
        waiting_time = current_time - patient.arrival_time
        total_waiting_time += waiting_time
        current_time += patient.estimated_time
        turnaround_time = current_time - patient.arrival_time
        total_turnaround_time += turnaround_time

    average_waiting_time = total_waiting_time / len(patients)
    average_turnaround_time = total_turnaround_time / len(patients)
    return average_waiting_time, average_turnaround_time

def rr_scheduling(patients, time_quantum):
    patients.sort(key=lambda x: x.arrival_time)
    queue = patients.copy()
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    while queue:
        patient = queue.pop(0)
        if current_time < patient.arrival_time:
            current_time = patient.arrival_time
        patient.start_time = current_time
        if patient.estimated_time <= time_quantum:
            waiting_time = current_time - patient.arrival_time
            total_waiting_time += waiting_time
            current_time += patient.estimated_time
        else:
            waiting_time = current_time - patient.arrival_time
            total_waiting_time += waiting_time
            current_time += time_quantum
            patient.estimated_time -= time_quantum
            queue.append(patient)

    total_turnaround_time = sum((p.start_time + p.estimated_time - p.arrival_time) for p in patients)
    average_waiting_time = total_waiting_time / len(patients)
    average_turnaround_time = total_turnaround_time / len(patients)
    return average_waiting_time, average_turnaround_time

# Define patient data
patients = [
    Patient("A", 0, 30, 3),
    Patient("B", 10, 20, 5),
    Patient("C", 15, 40, 2),
    Patient("D", 20, 15, 4),
]


# Calculate average waiting times and average turnaround times for each scheduling algorithm
fcfs_waiting_time, fcfs_turnaround_time = fcfs_scheduling(patients)
sjf_waiting_time, sjf_turnaround_time = sjf_scheduling(patients)
ps_waiting_time, ps_turnaround_time = ps_scheduling(patients)
rr_waiting_time, rr_turnaround_time = rr_scheduling(patients, 15)

# Determine the best algorithm based on both metrics (lower values are better)
metrics = {
    "FCFS": (fcfs_waiting_time, fcfs_turnaround_time),
    "SJF": (sjf_waiting_time, sjf_turnaround_time),
    "PS": (ps_waiting_time, ps_turnaround_time),
    "RR": (rr_waiting_time, rr_turnaround_time),
}

best_algorithm = min(metrics, key=lambda k: (metrics[k][0], metrics[k][1]))

# Print results
print(f"FCFS Average Waiting Time: {fcfs_waiting_time} minutes")
print(f"FCFS Average Turnaround Time: {fcfs_turnaround_time} minutes")
print(f"SJF Average Waiting Time: {sjf_waiting_time} minutes")
print(f"SJF Average Turnaround Time: {sjf_turnaround_time} minutes")
print(f"PS Average Waiting Time: {ps_waiting_time} minutes")
print(f"PS Average Turnaround Time: {ps_turnaround_time} minutes")
print(f"RR Average Waiting Time (Time Quantum = 15): {rr_waiting_time} minutes")
print(f"RR Average Turnaround Time (Time Quantum = 15): {rr_turnaround_time} minutes")

print(f"The best scheduling algorithm is: {best_algorithm}")