

t=int(input())
for i in range(t):
    required_run=int(input())
    current_run=int(input())
    ball=int(input())
    ball = ball*1.0
    remaining_over=ball / 6
    required_run_rate = (required_run - current_run + 1) / remaining_over
    current_run_rate=current_run / (50.0-remaining_over)
    print("%.2f" % current_run_rate, "%.2f" %required_run_rate)