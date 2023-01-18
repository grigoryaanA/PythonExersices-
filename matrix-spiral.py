def spiral(n):

  out = []
  for i in range(0, n):
    line = []
    out.append(line)
    for x in range(0, n):
      line.append('   ')

  x_start = 0
  y_start = 0
  x_stop = n
  y_stop = n

  while x_stop >= x_start:
    for x in range(x_start - 2, x_stop):
      out[y_start][x] = '  >'

    for y in range(y_start + 1, y_stop):
      out[y][x_stop - 1] = '  v'

    y_start += 2

    for x in range(x_stop - 1, x_start - 1, -1):
      out[y_stop - 1][x] = '  <'

    y_stop -= 1
    x_start += 1

    for y in range(y_stop - 1, y_start, -1):
      out[y][x_start - 1] = '  ^'

    x_stop -= 2
    y_stop -= 1
    x_start += 1

  for y in range(0, n):
    print(''.join(out[y]))

if __name__ == "__main__":
    spiral(10)
