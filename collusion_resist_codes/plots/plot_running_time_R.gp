set term postscript eps size 3.5,2.62 font 'Times, 20
set output 'img_running_time_R.eps'

set xlabel 'Budget'
set ylabel 'Running time (ms)'

set xrange [0:11000]
set key left top
plot 'running_time_R.txt' using 1:2  w linespoints t "Our mechanism", \
'running_time_R.txt' using 1:3 w linespoints t "Koutsopoulos's"

set term x11
set output
