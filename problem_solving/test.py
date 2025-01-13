

t=int(input())
for i in range(t):
    required_run=int(input())
    current_run=int(input())
    ball=int(input())
    ball_played = 300 - ball
    required_run_rate = ((required_run - current_run + 1) / float(ball)) * 6
    current_run_rate=(current_run / float(ball_played)) * 6
    print("%.2f" % current_run_rate, "%.2f" %required_run_rate)