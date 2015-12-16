set term postscript eps size 3.5,2.62 font 'Times, 20
set output 'img_running_time.eps'

set xlabel 'Number of participating users'
set ylabel 'Running time'

set xrange [0:1100]
set key left top
plot 'running_time.txt' using 1:2  w linespoints t "Our mechanism", \
'running_time.txt' using 1:3 w linespoints t "Koutsopoulos's"

set term x11
set output
