set term postscript eps size 3.5,2.62 font 'Times, 20
set output 'img_rtask.eps'

set xlabel 'Budget'
set ylabel 'Finished task ratio'

set xrange [0:11000]
set key off
set boxwidth 800
set style line 1 lc rgb "red" lw 3
set style fill solid 0.3 
plot 'rtask.txt' using 1:2:3  w boxerror ls 1

set term x11
set output
