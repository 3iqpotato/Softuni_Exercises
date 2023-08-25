pool_volume = int(input())
pipe_1_debit = int(input())
pipe_2_debit = int(input())
worker_away = float(input())

pipe1_filled = pipe_1_debit * worker_away
pipe2_filled = pipe_2_debit * worker_away
pipes_filled = pipe2_filled + pipe1_filled
pipe_1_filled_percent = (pipe1_filled / pipes_filled) * 100
pipe_2_filled_percent = (pipe2_filled / pipes_filled) * 100
persent_full = (pipes_filled / pool_volume) * 100

if pipes_filled <= pool_volume:
    print(f'The pool is {persent_full:.2f}% full. Pipe 1: {pipe_1_filled_percent:.2f}%. '
          f'Pipe 2: {pipe_2_filled_percent:.2f}%.')
else:
    diff = pipes_filled - pool_volume
    print(f'For {worker_away} hours the pool overflows with {diff:.2f} liters.')


